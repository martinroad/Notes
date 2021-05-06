package com.test.http;

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
public class HttpServerHandler extends ChannelInboundHandlerAdapter {

    /**
     * 当Channel中有来自于客户端的数据时，就会触发该方法的执行
     *
     * @param ctx 上下文对象
     * @param msg 来自于客户端的数据
     * @throws Exception
     */
    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) {
        System.out.println(msg);
        if (msg instanceof HttpRequest) {
            HttpRequest httpRequest = (HttpRequest) msg;
            try {
                System.out.println("请求方式：" + httpRequest.method().name());
                System.out.println("请求URI：" + httpRequest.uri());

                if ("/favicon.ico".equals(httpRequest.uri())) {
                    System.out.println("不处理/favicon.ico请求");
                    return;
                }

                // 构造response的响应体
                String result = "hello netty world";
                ByteBuf body = Unpooled.copiedBuffer(result, CharsetUtil.UTF_8);
                // 生成响应对象
                FullHttpResponse response = new DefaultFullHttpResponse(HttpVersion.HTTP_1_1, HttpResponseStatus.OK, body);
                // 获取到response的头部进行初始化
                HttpHeaders headers = response.headers();
                headers.set(HttpHeaderNames.CONTENT_TYPE, "text/plain;charset=utf-8");
                headers.set(HttpHeaderNames.CONTENT_LENGTH, body.readableBytes());

                // 将响应体写入到channel
                //ctx.write(body);
                //ctx.flush();
                //ctx.writeAndFlush(response);
                ctx.writeAndFlush(response).addListener(ChannelFutureListener.CLOSE);  // 添加监听器，关闭channel
            } catch (Exception e) {
                e.printStackTrace();
                System.out.println("处理请求失败...");
            }
        }
    }

    /**
     * 建立连接时，打印客户端地址
     *
     * @param ctx
     * @throws Exception
     */
    @Override
    public void channelActive(ChannelHandlerContext ctx) throws Exception {
        System.out.println("连接的客户端地址:" + ctx.channel().remoteAddress());
    }

    @Override
    public void channelReadComplete(ChannelHandlerContext ctx) {
        ctx.flush();
    }

    /**
     * 当Channel中的数据在处理过程中出现异常时会执行该方法
     *
     * @param ctx
     * @param cause
     * @throws Exception
     */
    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) {
        cause.printStackTrace();
        // 关闭Channel
        ctx.close();
    }
}
