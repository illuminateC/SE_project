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
            <VideoList :videos="videoList"/>
            <!-- <VideoList :videos="testList"/> -->
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
  // import VideoList from '@/components/TestTest.vue'
  export default {
    components: {
      HeaderVue, AsideVue, VideoList
    },
    data() {
      return {
        videoList: [],
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
        }),
        id2block: ["jsjsjsj","二次元","游戏","影视","音乐","运动","美食","科技"]
      }
    },
    methods: {
    },
    created() {
      var id = this.$route.params.blockID;
      console.log(this.id2block[id] + "BlockName");
      this.$axios({
        method: "get",
        url: "http://127.0.0.1:8000/index/getzone/",
        headers: { "content-type": "application/x-www-form-urlencoded" },
        params: { zone: this.id2block[id] }
      }).then((res) => {
        this.videoList = res.data.videos;
        if (res.data.status == 401) {
          this.$message.error("视频不存在");
        }
      }).catch(err => {
        console.log(err);
      });
    },
    watch: {
      "$route.params.blockID"(newval, oldval) {
        var id = this.$route.params.blockID;
        console.log(this.id2block[id] + "BlockName and Change Block");
        this.$axios({
          method: "get",
          url: "http://127.0.0.1:8000/index/getzone/",
          headers: { "content-type": "application/x-www-form-urlencoded" },
          params: { zone: this.id2block[id] }
        }).then((res) => {
          this.videoList = res.data.videos;
          if (res.data.status == 401) {
            this.$message.error("视频不存在");
          }
          this.$router.go(0);
        }).catch(err => {
          console.log(err);
        });
      },
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
  