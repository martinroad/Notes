package com.test;

import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;

import java.util.UUID;
import java.util.concurrent.TimeUnit;

/**
 * ChannelInboundHandlerAdapter 中的 channelRead（）方法不会自动释放接受到的来自于对方的msg所占用的所有资源
 */
public class ServerChannelHandler extends ChannelInboundHandlerAdapter {
    int counter;

    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        counter++;
        // 将来自于客户端的数据显示在服务端的控制台
        System.out.println(counter + "from client：" + msg);
        // 向客户端发送数据
        ctx.channel().writeAndFlush("from server：" + UUID.randomUUID());
        // 让线程暂停500ms
        TimeUnit.MILLISECONDS.sleep(500);
    }

    @Override
    public void channelActive(ChannelHandlerContext ctx) throws Exception {
        System.out.println("连接的客户端地址:" + ctx.channel().remoteAddress());
    }

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) throws Exception {
        cause.printStackTrace();
        ctx.close();
    }
}
