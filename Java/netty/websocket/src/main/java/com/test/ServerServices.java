package com.test;

import io.netty.bootstrap.ServerBootstrap;
import io.netty.channel.*;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.SocketChannel;
import io.netty.channel.socket.nio.NioServerSocketChannel;
import io.netty.handler.codec.LineBasedFrameDecoder;
import io.netty.handler.codec.http.HttpObjectAggregator;
import io.netty.handler.codec.http.HttpServerCodec;
import io.netty.handler.codec.http.websocketx.WebSocket00FrameDecoder;
import io.netty.handler.codec.http.websocketx.WebSocket00FrameEncoder;
import io.netty.handler.codec.http.websocketx.WebSocketServerProtocolHandler;
import io.netty.handler.stream.ChunkedWriteHandler;

public class ServerServices {
    private static final int PORT = 8080;

    public static void main(String[] args) {
        EventLoopGroup parentGroup = new NioEventLoopGroup();
        EventLoopGroup childGroup = new NioEventLoopGroup();

        try {
            ServerBootstrap bootstrap = new ServerBootstrap();
            bootstrap.group(parentGroup, childGroup)
                    .channel(NioServerSocketChannel.class)
                    .childHandler(new ChannelInitializer<SocketChannel>() {
                        @Override
                        protected void initChannel(SocketChannel ch) throws Exception {
                            ChannelPipeline pipeline = ch.pipeline();
                            // 添加一个基于行的帧解码器
                            pipeline.addLast(new LineBasedFrameDecoder(2*1024));
                            // 添加Http编解码处理器
                            pipeline.addLast(new HttpServerCodec());
                            // 添加大块数据流Chunk处理器
                            pipeline.addLast(new ChunkedWriteHandler());
                            // 大块数据聚合，添加 Chunk 聚合处理器，maxContentLength：聚合内容的最大长度
                            pipeline.addLast(new HttpObjectAggregator(4 * 1024));
                            // 添加websocket 协议转换器
                            pipeline.addLast(new WebSocketServerProtocolHandler("/some")); // websokcetPath
                            // 自定义处理器
                            pipeline.addLast(new WebSocketHandler());
                        }
                    });
            ChannelFuture future = bootstrap.bind(PORT).sync();
            System.out.println("服务器启动成功，监听端口号：8080");
            future.channel().closeFuture().sync();

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            parentGroup.shutdownGracefully();
            childGroup.shutdownGracefully();
        }
    }
}
