import io.netty.bootstrap.Bootstrap;
import io.netty.channel.ChannelFuture;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelPipeline;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.SocketChannel;
import io.netty.channel.socket.nio.NioSocketChannel;
import io.netty.handler.codec.LineBasedFrameDecoder;
import io.netty.handler.codec.string.StringDecoder;
import io.netty.handler.codec.string.StringEncoder;
import io.netty.util.CharsetUtil;
import org.jcp.xml.dsig.internal.dom.Utils;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;

public class TestClient {
    private static final int PORT = 8080;

    public static void main(String[] args) {
        NioEventLoopGroup group = new NioEventLoopGroup();
        try {
            Bootstrap bootstrap = new Bootstrap();
            bootstrap.group(group)
                    .channel(NioSocketChannel.class)
                    .handler(new ChannelInitializer<SocketChannel>() {
                        @Override
                        protected void initChannel(SocketChannel ch) throws Exception {
                            ChannelPipeline pipeline = ch.pipeline();
                            pipeline.addLast(new LineBasedFrameDecoder(2 * 1024));
                            pipeline.addLast(new StringDecoder());
                            pipeline.addLast(new StringEncoder());
                            pipeline.addLast((new TestClientHandler()));
                        }
                    });

            ChannelFuture future = bootstrap.connect("localhost", PORT).sync();

            // 获取键盘输入
            InputStreamReader inputStream = new InputStreamReader(System.in, CharsetUtil.UTF_8);
            BufferedReader br = new BufferedReader(inputStream);

            future.channel().writeAndFlush(br.readLine() + "\r\n");
            //future.channel().closeFuture().sync();

        } catch (Exception e) {
            e.printStackTrace();
        }
        //} finally {
        //    group.shutdownGracefully();
        //}
    }
}
