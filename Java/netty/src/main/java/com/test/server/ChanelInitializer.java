package com.test.server;

import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelPipeline;
import io.netty.channel.socket.SocketChannel;
import io.netty.handler.codec.http.HttpServerCodec;

public class ChanelInitlializer extends ChannelInitializer<SocketChannel> {

    // 当 Chanel 初始创建完毕后就会触发该方法的执行，用于初始化Channel
    @Override
    protected void initChannel(SocketChannel socketChannel) throws Exception {
        // 从Channel中获取pipeline
        ChannelPipeline pipeline = socketChannel.pipeline();
        // 将 HttpServerCodec 处理器放入到pipeline的最后
        // HttpServerCodec 是 HttpServerRequestDecoder 和 HttpServerResponseEncoder的复合体
        // HttpServerRequestDecoder: http请求解码器，将Channel中的ByteBuffer数据解码为HttpRequst对象
        // HttpServerResponseEncoder：http响应解码器，将HttpResponse对象编码为将要在Channel中发送的ByteBuffer数据
        pipeline.addLast("HttpServerCodec", new HttpServerCodec());
        // 将自定义的处理器放入到 pipeline 的最后
        pipeline.addLast("ServerHandler",new ServerHandler());

    }
}
