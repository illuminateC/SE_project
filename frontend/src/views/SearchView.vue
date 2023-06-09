<template>
  <div id="home">
    <el-container>
      <el-header class="my-header">
        <HeaderVue/>
      </el-header>
      <el-container>
        <el-main class="search-main">
          <el-tabs class="search-tabs">
            <el-tab-pane>
              <span slot="label" style="font-size: 20px;">视频</span>
              <VideoList :videos="videoList" style="justify-content: space-around;" />
            </el-tab-pane>
            <el-tab-pane>
              <span slot="label" style="font-size: 20px;">用户</span>
              <UserList :users="userList" />
            </el-tab-pane>
          </el-tabs>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import qs from "qs"
import HeaderVue from '@/components/HeaderVue.vue'
import VideoList from '@/components/VideoList.vue'
import UserList from "@/components/UserList.vue"
export default {
  components: {
    HeaderVue,
    VideoList,
    UserList
},
  data() {
    return {
      videoList: [],
      userList: [
        // {
        //   id: 24,
        //   avatarUrl: "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
        //   username: "usertest",
        //   description: "测试hhhh",
        //   videoNum: 5,
        //   fanNum: 0,
        // },
        // {
        //   id: 24,
        //   avatarUrl: "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
        //   username: "usertest",
        //   description: "测试hhhh",
        //   videoNum: 5,
        //   fanNum: 0,
        // },
        // {
        //   id: 24,
        //   avatarUrl: "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
        //   username: "usertest",
        //   description: "测试hhhh",
        //   videoNum: 5,
        //   fanNum: 0,
        // },
        // {
        //   id: 24,
        //   avatarUrl: "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
        //   username: "usertest",
        //   description: "测试hhhh",
        //   videoNum: 5,
        //   fanNum: 0,
        // },
        // {
        //   id: 24,
        //   avatarUrl: "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
        //   username: "usertest",
        //   description: "测试hhhh",
        //   videoNum: 5,
        //   fanNum: 0,
        // },
        // {
        //   id: 24,
        //   avatarUrl: "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
        //   username: "usertest",
        //   description: "测试hhhh",
        //   videoNum: 5,
        //   fanNum: 0,
        // },
      ],
      testList: Array(48).fill({
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
    getVideos() {
        var data = this.searchContent;
        return this.$axios({
            method: "get",
            url: "http://127.0.0.1:8000/index/video/",
            headers: { "content-type": "application/x-www-form-urlencoded" },
            params: {
              search_str: this.searchContent
            }
        });
    },
    getUsers() {
        var data = this.searchContent;
        return this.$axios({
          method: "get",
          url: "http://127.0.0.1:8000/index/user/",
          headers: { "content-type": "application/x-www-form-urlencoded" },
          params: {
            search_str: this.searchContent
          }
        });
    },
    searchData() {
        if (this.searchContent === "") {
            this.$message({
            type: "error",
            message: "输入点东西呀QAQ",
            });
            return;
        }
        localStorage.removeItem("searchContent");
        localStorage.setItem("searchContent", this.searchContent);
        var that = this;
        this.$axios
          .all([that.getVideos(), that.getUsers()])
          .then(
            this.$axios.spread(function (res1, res2) {
                console.log(res1 + "res1");
                console.log(res2 + "res2");
                that.userList = res2.data.users;
                that.videoList = res1.data.videos;
                console.log("that.userList" + that.userList);
                that.$message({
                    type: "success",
                    message: "搜索成功！",
                });
            })
          )
          .catch((err) => {
          console.log(err);
          that.$message({
              type: "error",
              message: "服务器被玩坏了QAQ！",
          });
          });
    }
  },
  created() {
    this.searchContent = localStorage.getItem("searchContent");
    this.searchData();
  }
}
</script>

<style>
.my-header {
  position: fixed;
  top: 0;
  width: 100%;
  background-color: #ffffff;
  /* background-color: aqua; */
  z-index: 999;
}

.search-main {
  position: relative;
  top: 40px;
  z-index: 1;
}

/* .search-tabs {
  font-size: 100px;
} */

.el-aside::-webkit-scrollbar {
    display: none;
}

</style>
