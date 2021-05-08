package com.test;


import io.netty.bootstrap.ServerBootstrap;
import io.netty.buffer.Unpooled;
import io.netty.channel.ChannelFuture;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelPipeline;
import io.netty.channel.DefaultChannelPromise;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.SocketChannel;
import io.netty.channel.socket.nio.NioServerSocketChannel;
import io.netty.handler.codec.*;
import io.netty.handler.codec.string.StringDecoder;
import io.netty.handler.codec.string.StringEncoder;

import java.nio.charset.StandardCharsets;

public class ServerService {
    private static final int PORT = 5300;

    public static void main(String[] args) {
        NioEventLoopGroup parentGroup = new NioEventLoopGroup();
        NioEventLoopGroup childGroup = new NioEventLoopGroup();

        try {
            ServerBootstrap bootstrap = new ServerBootstrap();
            bootstrap.group(parentGroup, childGroup)
                    .channel(NioServerSocketChannel.class)
                    .childHandler(new ChannelInitializer<SocketChannel>() {
                        @Override
                        protected void initChannel(SocketChannel ch) throws Exception {
                            ChannelPipeline pipeline = ch.pipeline();
                            // 1、LineBasedFrameDecoder 基于行的解码器，最大长度为5kb，LineBasedFrameDecoder 一定要放在StringDecoder前面
                            //pipeline.addLast(new LineBasedFrameDecoder(5*1024));

                            // 2、DelimiterBasedFrameDecoder 基于指定分隔符 "|" 的解码器，最大长度为5kb，DelimiterBasedFrameDecoder 一定要放在StringDecoder前面
                            //pipeline.addLast(new DelimiterBasedFrameDecoder(5 * 1024, Unpooled.copiedBuffer("|".getBytes(StandardCharsets.UTF_8))));

                            // 3、FixedLengthFrameDecoder 基于固定长度帧解码器，固定长度为1024 byte， FixedLengthFrameDecoder 一定要放在StringDecoder前面
                            //pipeline.addLast(new FixedLengthFrameDecoder(1024));

                            // 4、LengthFieldBasedFrameDecoder 基于长度域的帧解码器， LengthFieldBasedFrameDecoder 一定要放在StringDecoder前面
                            pipeline.addLast(new LengthFieldBasedFrameDecoder(5 * 1024, 0, 4, 0, 4));
                            pipeline.addLast(new LengthFieldPrepender(4));

                            pipeline.addLast(new StringDecoder());  // StringDecoder：字符串解码器，将Channel中的ByteBuf数据解码为String
                            pipeline.addLast(new StringEncoder());  // StringEncoder：字符串编码器，将String编码为要发送到Channel中的ByteBuf
                            pipeline.addLast(new ServerChannelHandler());  // 添加自定义的过滤器
                        }
                    });

            ChannelFuture future = bootstrap.bind(PORT).sync();
            System.out.println("服务器已启动，监听端口号：" + PORT);
            future.channel().closeFuture().sync();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 优雅关闭
            parentGroup.shutdownGracefully();
            childGroup.shutdownGracefully();
        }
    }
}
