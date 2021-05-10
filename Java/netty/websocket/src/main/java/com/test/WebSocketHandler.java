package com.test;

import io.netty.channel.Channel;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.channel.group.ChannelGroup;
import io.netty.channel.group.DefaultChannelGroup;
import io.netty.handler.codec.http.websocketx.TextWebSocketFrame;
import io.netty.util.concurrent.GlobalEventExecutor;

public class WebSocketHandler extends ChannelInboundHandlerAdapter {
    // 创建一个所有客户端的channel的集合， 是一个线程安全的集合，存放着与所有客户端建立连接的Active状态的Channel
    // GlobalEventExecutor 是一个单例、单线程的 EventExecutor，是为了保证对当前group中的所有Channel的处理线程是同一个线程
    ChannelGroup channels = new DefaultChannelGroup(GlobalEventExecutor.INSTANCE);

    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        String text = ((TextWebSocketFrame) msg).text();
        ctx.channel().writeAndFlush(new TextWebSocketFrame("from clinet：" + text));

        // 将当前消息广播给所有客户端channel
        //channels.writeAndFlush(msg)

        // 发送给自己的消息与发送给别人的消息显示不一样
        Channel channel = ctx.channel();
        channels.forEach(ch -> {
            if (ch != channel) {
                ch.writeAndFlush(channel.remoteAddress() + ": " + msg + "\n");
            } else {
                ch.writeAndFlush("me: " + msg + "\n");
            }
        });
        channels.writeAndFlush(msg);
    }

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) throws Exception {
        cause.printStackTrace();
        ctx.close();
    }

    /**
     * 获取到与服务端连接成功的channle
     *
     * @param ctx
     * @throws Exception
     */
    @Override
    public void channelActive(ChannelHandlerContext ctx) throws Exception {
        Channel channel = ctx.channel();
        channels.writeAndFlush(channel.remoteAddress() + "已上线\n");
        // 将当前channel添加到channels中
        channels.add(channel);
    }

    /**
     * 只要有客户端channel断开与服务端的连接就会触发该方法的执行
     *
     * @param ctx
     * @throws Exception
     */
    @Override
    public void channelInactive(ChannelHandlerContext ctx) throws Exception {
        Channel channel = ctx.channel();
        channels.writeAndFlush(channel.remoteAddress() + "下线，当前在线人数 " + channels.size()+ "\n");

        // group 中存放的都是Active状态的客户端channel，一旦某个channle 的状态不再是Active，channels会自动从集合中踢出，所以不需要手动调用 remove() 方法
        //channels.remove(channel);
    }
}
