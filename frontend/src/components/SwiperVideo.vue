<template>
    <div>
      <div class="block_warp" style="margin-top: 30px">
        <el-carousel :interval="3000" type="card" height="400px">
          <el-carousel-item v-for="(item, index) in videos" :key="index">
            <router-link :to='"/video/"+item.videoID'>
              <div class="video_warp">
                <div class="cover_warp">
                  <img
                    class="cover_img"
                    width="480px"
                    height="400px"
                    :src="item.coverUrl"
                    style="
                      border-radius: 30px;
                      -webkit-border-radius: 30px;
                      -moz-border-radius: 30px;
                    "
                  />
                  <div class="cover_footer">
                    <ul>
                      <li class="title">{{ item.title }}</li>
                      <li style="float: right; margin-right: 10px; font-size: 18px">
                        {{ item.createdTime.split("T")[0] }}
                      </li>
                      <li style="float: right; margin-right: 10px; font-size: 18px">
                          <i class="iconfont icondianshizhiboguankanshipinbofangmeiti" style="font-size: 16px;"></i> {{ item.viewNum }}
                      </li>
                      <li style="float: right; margin-right: 10px; font-size: 18px">
                          <i class="iconfont icondianzan" style="font-size: 16px;"></i> {{ item.likeNum }}
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </router-link>
          </el-carousel-item>
        </el-carousel>
      </div>
    </div>
</template>
<script>
export default {
props: {
    videos: {
    type: Array,
    default() {
        return [
        {
          videoID: 190026,
          title: "【维多利亚3】法兰西的野望",
          description: "Vive La France",
          videoUrl:
            "http://43.143.140.26/videos/190026.mp4",
          coverUrl:
            "http://43.143.140.26/covers/190026.jpg",
          likeNum: 0,
          collectNum: 0,
          viewNum: 0,
          zone: "二刺猿",
          tag: "",
          userID: 5,
          createdTime: "2022-04-21T03:17:44.603Z",
          needAudit: 0
        },
        {
          videoID: 23,
          title: "Slide2",
          description: "测试",
          videoUrl:
            "https://video-1309504341.cos.ap-beijing.myqcloud.com/24.mp4",
          coverUrl:
            "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
          likeNum: 0,
          collectNum: 0,
          viewNum: 0,
          zone: "二刺猿",
          tag: "",
          userID: 5,
          createdTime: "2022-04-21T03:17:44.603Z",
          needAudit: 0
        },
        {
          videoID: 24,
          title: "Slide3",
          description: "测试",
          videoUrl:
            "https://video-1309504341.cos.ap-beijing.myqcloud.com/24.mp4",
          coverUrl:
            "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
          likeNum: 0,
          collectNum: 0,
          viewNum: 0,
          zone: "二刺猿",
          tag: "",
          userID: 5,
          createdTime: "2022-04-21T03:17:44.603Z",
          needAudit: 0
        },
        ];
    },
    },
},
created() {
},
methods: {
},
};
</script>
<style scoped>
.el-carousel__item h3 {
color: #475669;
font-size: 14px;
opacity: 0.75;
line-height: 200px;
margin: 0;
}

.el-carousel__item:nth-child(2n) {
background-color: none;
}

.el-carousel__item:nth-child(2n + 1) {
background-color: none;
}
.cover_img {
width: 100%;
height: 100%;
}
.video_warp {
width: 100%;
height: 100%;
display: flex;
align-content: center;
justify-content: center;
}
.cover_warp {
width: auto;
height: auto;
border-radius: 30px;
position: relative;
}
.cover_footer {
width: 100%;
line-height: 40px;
font-size: 20px;
position: absolute;
z-index: 2;
bottom: 0px;
background-image: linear-gradient(
    180deg,
    rgba(0, 0, 0, 0) 0%,
    rgba(0, 0, 0, 0.8) 100%
);
border-bottom-right-radius: 30px;
border-bottom-left-radius: 30px;
}
.cover_footer ul {
line-height: 40px;
padding-left: 30px;
color: white;
}
.cover_footer li {
line-height: 40px;
display: inline-block;
float: left;
margin-left: 5px;
list-style: none;
vertical-align: middle;
color: white;
}
/* title貌似改不了 最好限制字数在15以内*/
.title {
height: 40px;
width: 60%;
line-height: 40px;
font-size: 20px;
display: block;
text-align: left;
word-break: break-all;
word-wrap: break-word;
}
.sender {
height: 60px;
width: 238px;
line-height: 34px;
vertical-align: middle;
}
</style>