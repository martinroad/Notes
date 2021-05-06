package com.test.server;

import io.netty.buffer.ByteBuf;
import io.netty.buffer.Unpooled;
import io.netty.channel.ChannelFutureListener;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.handler.codec.http.*;
import io.netty.util.CharsetUtil;

/**
 * 自定义服务端处理器
 * 需求：用户提交一个请求后，返回结果
 */
public class ServerHandler extends ChannelInboundHandlerAdapter {

    /**
     * 当Channel中有来自于客户端的数据时，就会触发该方法的执行
     *
     * @param ctx 上下文对象
     * @param msg 来自于客户端的数据
     * @throws Exception
     */
    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        //System.out.println("msg = " + msg.getClass());
        //System.out.println("客户端的地址：" + ctx.channel().remoteAddress());

        try {
            if (msg instanceof HttpRequest) {
                HttpRequest request = (HttpRequest) msg;
                System.out.println("请求方式：" + request.method().name());
                System.out.println("请求URI：" + request.uri());

                if ("/favicon.ico".equals(request.uri())) {
                    System.out.println("不处理/favicon.ico请求");
                    return;
                }

                // 构造response的响应体
                ByteBuf body = Unpooled.copiedBuffer("hello netty world", CharsetUtil.UTF_8);
                // 生成响应对象
                //DefaultFullHttpResponse response = new DefaultFullHttpResponse(HttpVersion.HTTP_1_1, HttpResponseStatus.OK, body);
                //// 获取到response的头部进行初始化
                //HttpHeaders headers = response.headers();
                //headers.set(HttpHeaderNames.CONTENT_TYPE, "text/plain");
                //headers.set(HttpHeaderNames.CONTENT_LENGTH, body.readableBytes());

                // 将响应体写入到channel
                //ctx.write(body);
                //ctx.flush();
                ctx.writeAndFlush(body);
                //ctx.writeAndFlush(msg).addListener(ChannelFutureListener.CLOSE);  // 添加监听器，关闭
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * 当Channel中的数据在处理过程中出现异常时会执行该方法
     *
     * @param ctx
     * @param cause
     * @throws Exception
     */
    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) throws Exception {
        cause.printStackTrace();
        // 关闭Channel
        ctx.close();
    }
}
