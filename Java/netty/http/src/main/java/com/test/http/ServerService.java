package com.test.http;


import io.netty.bootstrap.ServerBootstrap;
import io.netty.channel.ChannelFuture;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelPipeline;
import io.netty.channel.EventLoopGroup;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.SocketChannel;
import io.netty.channel.socket.nio.NioServerSocketChannel;
import io.netty.handler.codec.http.HttpServerCodec;

public class ServerService {
    private static final int PORT = 5100;

    public static void main(String[] args) {

        // 用于处理客户端连接请求，将请求发送给childEventGropup 中的 evnetLoop
        EventLoopGroup parentEventGroup = new NioEventLoopGroup();
        EventLoopGroup childEventGropup = new NioEventLoopGroup();

        try {
            ServerBootstrap serverBootstrap = new ServerBootstrap();
            serverBootstrap.group(parentEventGroup, childEventGropup) // 指定evnetLoop
                    .channel(NioServerSocketChannel.class)// 指定使用NIO进行通信
                    .childHandler(new ChannelInitializer<SocketChannel>() {

                                      @Override
                                      protected void initChannel(SocketChannel socketChannel) throws Exception {
                                          // 从Channel中获取pipeline
                                          ChannelPipeline pipeline = socketChannel.pipeline();
                                          // 将 HttpServerCodec 处理器放入到pipeline的最后
                                          // HttpServerCodec 是 HttpServerRequestDecoder 和 HttpServerResponseEncoder的复合体
                                          // HttpServerRequestDecoder: http请求解码器，将Channel中的ByteBuffer数据解码为HttpRequst对象
                                          // HttpServerResponseEncoder：http响应解码器，将HttpResponse对象编码为将要在Channel中发送的ByteBuffer数据
                                          pipeline.addLast(new HttpServerCodec());
                                          // 将自定义的处理器放入到 pipeline 的最后
                                          pipeline.addLast(new HttpServerHandler());
                                      }
                                  }
                    );

            ChannelFuture future = serverBootstrap.bind(PORT).sync();  // bind()是异步的,但sync() 方法会使 bind（）操作与后续的代码的执行由异步变为同步
            System.out.println("服务器启动成功，监听端口号:" + PORT);
            // 关闭 chanel，closeFuture() 的执行也是异步的。当 Chanel 调用了 close（）方法并关闭成功后才会触发 closeFuture（）方法的执行
            // sync() 方法使 closeFuture() 变为同步
            future.channel().closeFuture().sync();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            // 优雅关闭，就是等着执行完后才去关闭
            parentEventGroup.shutdownGracefully();
            childEventGropup.shutdownGracefully();

        }
    }
}
