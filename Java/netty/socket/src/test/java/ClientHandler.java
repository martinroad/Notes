import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.channel.SimpleChannelInboundHandler;

import java.time.LocalTime;
import java.util.Date;
import java.util.concurrent.TimeUnit;

/**
 * SimpleChannelInboundHandler 中的 channelRead0（）方法会自动释放接受到的来自于对方的msg所占用的所有资源
 */
public class ClientHandler extends SimpleChannelInboundHandler<String> {

    /**
     * msg的消息类型与类中的范型类型是一致的
     * @param ctx
     * @param msg
     * @throws Exception
     */
    @Override
    protected void channelRead0(ChannelHandlerContext ctx, String msg) throws Exception {
        System.out.println(ctx.channel().remoteAddress()+ " ， " + msg);
        ctx.channel().writeAndFlush("from client：" + LocalTime.now());
        TimeUnit.MILLISECONDS.sleep(500);
    }

    /**
     * 当channel 被激活后会触发该方法的执行
     * @param ctx
     * @throws Exception
     */
    @Override
    public void channelActive(ChannelHandlerContext ctx) throws Exception {
        ctx.channel().writeAndFlush("client active");
    }

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) throws Exception {
        cause.printStackTrace();
        ctx.close();
    }
}
