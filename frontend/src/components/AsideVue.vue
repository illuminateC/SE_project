<template>
    <div>
        <el-menu
            default-active="2"
            class="el-menu-vertical"
            @open="handleOpen"
            @close="handleClose"
            background-color="#e9e9e9"
            text-color="#4A4A4A"
            active-text-color="#000000"
            :router="true">
            <el-menu-item index="/homepage">
                <i class="el-icon-s-home"></i>
                <span slot="title">首页</span>
            </el-menu-item>
            <el-menu-item index="/followpage">
                <i class="el-icon-s-custom"></i>
                <span slot="title">关注</span>
            </el-menu-item>
            <el-menu-item index="/userprofile">
                <i class="el-icon-user"></i>
                <span slot="title">我的</span>
            </el-menu-item>
            <el-divider></el-divider>
            <el-menu-item index="/block/1">
                <!-- <i class="el-icon-document"></i> -->
                <i class="iconfont icondongman" style="font-size: 25px;"></i>
                <span slot="title">二刺猿</span>
            </el-menu-item>
            <el-menu-item index="/block/2">
                <i class="iconfont iconyouxi" style="font-size: 22px;"></i>
                <span slot="title">   游戏</span>
            </el-menu-item>
            <el-menu-item index="/block/3">
                <i class="iconfont icondianying" style="font-size: 22px;"></i>
                <span slot="title">   影视</span>
            </el-menu-item>
            <el-menu-item index="/block/4">
                <i class="iconfont iconbeijingyinle" style="font-size: 20px;"></i>
                <span slot="title">   音乐</span>
            </el-menu-item>
            <el-menu-item index="/block/5">
                <i class="iconfont iconlanqiu1" style="font-size: 29px;"></i>
                <span slot="title">运动</span>
            </el-menu-item>
            <el-menu-item index="/block/6">
                <i class="iconfont iconmeishi" style="font-size: 25px;"></i>
                <span slot="title"> 美食</span>
            </el-menu-item>
            <el-menu-item index="/block/7">
                <i class="iconfont icon10kejichuangxin-keji" style="font-size: 25px;"></i>
                <span slot="title"> 科技</span>
            </el-menu-item>
            <!-- <el-menu-item index="/block/6">
                <i class="iconfont icon10kejichuangxin-keji" style="font-size: 25px;"></i>
                <span slot="title"> 科技</span>
            </el-menu-item><el-menu-item index="/block/6">
                <i class="iconfont icon10kejichuangxin-keji" style="font-size: 25px;"></i>
                <span slot="title"> 科技</span>
            </el-menu-item><el-menu-item index="/block/6">
                <i class="iconfont icon10kejichuangxin-keji" style="font-size: 25px;"></i>
                <span slot="title"> 科技</span>
            </el-menu-item>
            <el-menu-item index="/block/6">
                <i class="iconfont icon10kejichuangxin-keji" style="font-size: 25px;"></i>
                <span slot="title"> 科技</span>
            </el-menu-item><el-menu-item index="/block/6">
                <i class="iconfont icon10kejichuangxin-keji" style="font-size: 25px;"></i>
                <span slot="title"> 科技</span>
            </el-menu-item><el-menu-item index="/block/6">
                <i class="iconfont icon10kejichuangxin-keji" style="font-size: 25px;"></i>
                <span slot="title"> 科技</span>
            </el-menu-item> -->
        </el-menu>
    </div>
</template>

<script>
export default {
    data() {
        return {
        }
    }
}
</script>

<style>
.el-menu-vertical {
    overflow: hidden;
    position: fixed;
    top: 60px;
    height: 100%;
    width: 200px;
    margin-left: -7px;
}
.el-menu-vertical ::-webkit-scrollbar {
  width: 0; /* 去掉滚动条的宽度 */
  background: transparent; /* 设置背景透明 */
}
</style>
