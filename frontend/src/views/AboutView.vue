<template>
  <div id="home">
    <el-container class="my-home">
      <el-header class="my-header">
        <HeaderVue/>
      </el-header>
      <el-container>
        <div>
          <el-aside width = "200px" class="my-aside">
            <AsideVue/>
          </el-aside>
        </div>
        <el-main class = "my-main">
          <!-- <VideoList :videos="videoList"/> -->
          <div>
            <Swiper />
          </div>
          <div>
            <VideoList :videos="testList"/>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import qs from "qs"
import HeaderVue from '@/components/HeaderVue.vue'
import AsideVue from '@/components/AsideVue.vue'
import VideoList from '@/components/VideoList.vue'
import Swiper from '@/components/SwiperVideo.vue'
// import VideoList from '@/components/TestTest.vue'
export default {
  components: {
    HeaderVue, AsideVue, VideoList, Swiper
    // HeaderVue, AsideVue, VideoList
  },
  data() {
    return {
      videoList: [
        {
          videoID: 24,
          title: "####",
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
          videoID: 23,
          title: "####",
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
          title: "####",
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
          videoID: 23,
          title: "####",
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
          title: "####",
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
          videoID: 23,
          title: "####",
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
      ],
      testVideo: {
          videoID: 24,
          title: "####",
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
      testList: Array(29).fill({
          videoID: 24,
          title: "####",
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
      })
    }
  },
  methods: {
  },
  created() {
    this.$axios({
      method: "get",
      url: "/index/getzone",
      data: qs.stringify({
        zone: null
      })
    }).then((res) => {
      this.videoList = res.data.List;
    });
  }
}
</script>

<style>
.my-home {
  position: relative;
}

.my-header {
  position: fixed;
  top: 0;
  /* height: 200vh; */
  /* left: 0; */
  width: 100%;
  /* height: 10vh; */
  background-color: #ffffff;
  /* background-color:bisque; */
  z-index: 999;
}

.my-main {
  z-index: 1;
  margin-left: 200px;
  margin-top: 20px;
}

.my-aside {
  z-index: 2;
  position: absolute; 
  top: 0; 
  left: 0; 
  height: 100%;
  bottom: 0; 
  /* background-color: aqua; */
  /* width: 200px;  */
}

.el-aside::-webkit-scrollbar {
    display: none;
}

.el-main::-webkit-scrollbar {
    display: none;
}

.Aside {
  width: 100vh;
}
</style>
