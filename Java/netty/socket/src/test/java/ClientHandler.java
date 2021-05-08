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
     *
     * @param ctx
     * @param msg
     * @throws Exception
     */
    @Override
    protected void channelRead0(ChannelHandlerContext ctx, String msg) throws Exception {
        //System.out.println(ctx.channel().remoteAddress()+ " ， " + msg);
        //ctx.channel().writeAndFlush("from client：" + LocalTime.now());
        //TimeUnit.MILLISECONDS.sleep(500);
    }

    /**
     * 当channel 被激活后会触发该方法的执行
     *
     * @param ctx
     * @throws Exception
     */
    @Override
    public void channelActive(ChannelHandlerContext ctx) throws Exception {
        String msg = "中新经纬客户端5月7日电 银保监会网站消息，为规范统一银行业保险业许可证管理规则，进一步强化银行保险机构许可证管理要求，中国银保监会制定了《银行保险机构许可证管理办法》(以下简称《办法》)。" +
                "据介绍，《办法》共二十二条，主要内容包括：一是将银保监会向银行保险机构颁发的许可证整合为金融许可证、保险许可证和保险中介许可证三类，明确各类许可证的适用对象。二是统一许可证记载内容。许可证载明下列内容：机构名称、业务范围、批准日期、机构住所、颁发许可证日期、发证机关。三是优化统一银行保险机构新领、换领、缴回许可证相关管理规定及时限要求。四是明确银保监会及其派出机构许可证管理职责及要求。五是对存在未按规定使用或管理许可证相关情形的，明确依照有关法律法规进行处罚。" +
                "银保监会指出，《办法》自2021年7月1日起施行。下一步，我会将稳妥开展存量金融许可证和保险类许可证换发工作，督促银行保险机构加强许可证管理，依法合规开展经营活动。" +
                "此外，中国银保监会有关部门负责人就《银行保险机构许可证管理办法》答记者问。该负责人介绍，目前我会向银行保险机构颁发的许可证种类较多，各类许可证记载事项、管理要求等存在差异，难以适应机构改革后银行保险机构许可证统一管理的需要。此外，检查中发现银行保险机构在许可证使用管理工作中存在一些问题，需强化相关管理要求。针对上述问题，为规范统一许可证管理规定，督促银行保险机构进一步加强许可证管理，依法合规开展经营活动，银保监会制定出台了《办法》。" +
                "《办法》对银行保险机构许可证管理作出了哪些新规定？该负责人介绍，一是将银行保险机构持有的许可证整合为金融许可证、保险许可证和保险中介许可证3类。二是统一许可证记载内容。许可证载明下列内容：机构名称、业务范围、批准日期、机构住所、颁发许可证日期、发证机关。三是在新领、换领、遗失许可证相关公告要求中不再指定公告媒介。四是对银行保险机构违反《办法》规定、存在相关情形的，明确依照《中华人民共和国银行业监督管理法》《中华人民共和国商业银行法》《中华人民共和国保险法》有关规定进行处罚。" +
                "根据《办法》规定，银行保险机构许可证使用和管理中有哪些公示、公告要求？该负责人指出，公示方面，一是要求银行保险机构在营业场所的显著位置公示许可证原件。对于不持有许可证的保险中介机构分支机构，要求其在营业场所的显著位置公示加盖法人机构公章的许可证复印件。二是为进一步保护金融消费者知情权，要求银行保险机构依据行政许可决定文件和上级管理单位授权文件，在营业场所的显著位置以适当方式公示其业务范围、经营区域、主要负责人。对于通过网络平台开展业务的，银行保险机构应当在相关网络页面及功能模块以清晰、醒目的方式展示上述内容。" +
                "公告方面，一是明确需要进行公告的情形和时限要求。新领、换领许可证，银行保险机构应于30日内进行公告。许可证遗失，银行保险机构应于发现之日起7日内发布遗失声明公告。二是明确可采取的公告方式及效果要求。银行保险机构可在公开发行报刊上公告、在银行保险机构官方网站上公告，或采取其他有效便捷的公告方式。公告的知晓范围应至少与机构开展业务经营的地域范围相匹配。银行保险机构应保留相关公告材料备查。" +
                "《办法》向社会公开征求意见的情况如何？该负责人答复称，《办法》公开征求意见期间，银行保险机构从业人员、专家学者等从条款理解、实践做法、文字表述等方面提出了很好的意见和建议，我们对这些意见和建议都进行了认真研究，对《办法》部分条款内容进行了修改。需要重点说明的是，部分机构提出有些业务办理需要携带许可证原件外出，期间无法在营业场所公示许可证原件。经研究，我们认为，银行保险机构因业务办理需要暂时无法在营业场所公示许可证原件，情况属实的，不属于《办法》规定的处罚情形。银行保险机构应当在业务办理完毕后，及时在营业场所的显著位置公示许可证原件。(中新经纬APP) " +
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc";

        System.out.println("msg.length:" + msg.length());

        // 1、LineBasedFrameDecoder 使用行结束符作为标识:System.getProperty("line.separator")
        //for (int i = 0; i < 3; i++) {
        //    ctx.channel().writeAndFlush(msg + System.getProperty("line.separator"));
        //}


        // 2、DelimiterBasedFrameDecoder 使用指定分隔符 "|"，对数据尽心拆包粘包
        //for (int i = 0; i < 3; i++) {
        //    ctx.writeAndFlush(msg + "|");
        //    //ctx.channel().writeAndFlush(msg + "|");
        //}

        // 3、FixedLengthFrameDecoder 基于固定长度帧解码器， 对数据尽心拆包粘包
        for (int i = 0; i < 3; i++) {
            ctx.writeAndFlush(msg);
        }

    }

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) throws Exception {
        cause.printStackTrace();
        ctx.close();
    }
}
