<template>
    <el-container>
      <el-header>
        <HeaderVue/>
      </el-header>
      <el-main>
        <div class="user-profile">
          <div class="header">
            <div class="avatar-container">
              <input type="file" id="avatarInput"  hidden accept="image/*">
              <img :src="avatar"  class="avatar">
            </div>
            <div class="user-info">
              <h2>{{username}}</h2>
              <!-- <textarea placeholder="这个人很懒，什么也没留下~" v-model="sign" class="user-info-background" maxlength="16" @blur="saveSign"></textarea> -->
              <span placeholder="这个人很懒，什么也没留下~" class="user-info-background">{{ sign }}</span>
            </div>
          </div>
          <div class="menu-container">
            <el-menu mode="horizontal" :default-active="activeIndex" @select="handleSelect">
              <el-menu-item index="1">
                <i class="el-icon-video-play"></i>  
                作品
              </el-menu-item>
              <el-menu-item index="2">
                <i class="el-icon-star-off"></i>    
                收藏
              </el-menu-item>
              <el-menu-item index="3">
                <i class="el-icon-user"></i>
                关注
              </el-menu-item>
            </el-menu>
          </div>
      
          <VideoList :videos="videoList" v-if="activeIndex === '1'" />
      
          <VideoList :videos="videoList" v-if="activeIndex === '2'" />
      
          <!-- <div class="follows-container" v-if="activeIndex === '3'" >
            <div class="follow-container" >
              <img :src=avatar class="follow-avatar">
              <div class="user-info">
                <sapn class="follow-username">{{username}}</sapn>
                <span class="follow-sign">这个人很懒，什么也没留下</span>
              </div>
              <el-button class="follow-button" :type="followed ? 'info' : 'primary'" @click="toggleFollow">
                {{ followed ? '取消关注' : '关注' }}
              </el-button>
            </div>
            
            <div class="follow-container" >
              <img :src=avatar class="follow-avatar">
              <div class="user-info">
                <sapn class="follow-username">{{username}}</sapn>
                <span class="follow-sign">这个人很懒，什么也没留下</span>
              </div>
              <el-button class="follow-button" :type="followed ? 'info' : 'primary'" @click="toggleFollow">
                {{ followed ? '取消关注' : '关注' }}
              </el-button>
            </div>
          </div> -->
          <el-skeleton :loading="loading" style="width: 100%" animated v-if="activeIndex === '3'">
            <template slot="template">
              <div class="follows-container" v-if="follows == undefined ||follows == null || follows.length <= 0">
                <div class="follow-container">
                  <el-skeleton-item variant="image" style="width: 50px; height: 50px; border-radius: 50%;" />
                  <div class="user-info">
                    <el-skeleton-item variant="h3" style="width: 5%;  margin-bottom: 10px; margin-left: 10px;" />
                    <el-skeleton-item variant="text" style="width: 30%; margin-left: 10px;" />
                  </div>
                  <el-skeleton-item variant="button" style="width: 100px; height: 40px; margin-left: auto; margin-right: 0;" />
                </div>
              </div>
              <div class="follows-container" v-for="follow in follows">
                <div class="follow-container">
                  <el-skeleton-item variant="image" style="width: 50px; height: 50px; border-radius: 50%;" />
                  <div class="user-info">
                    <el-skeleton-item variant="h3" style="width: 5%;  margin-bottom: 10px; margin-left: 10px;" />
                    <el-skeleton-item variant="text" style="width: 30%; margin-left: 10px;" />
                  </div>
                  <el-skeleton-item variant="button" style="width: 100px; height: 40px; margin-left: auto; margin-right: 0;" />
                </div>
              </div>  
            </template>
            <template>
              <div class="follows-container" v-for="follow in follows">
              <div class="follow-container" >
                <router-link :to='"/otherUser/"+ follow.id ' style="text-decoration: none"><img :src=follow.avatarUrl class="follow-avatar" ></router-link>
                <div class="user-info">
                  <sapn class="follow-username">{{follow.username}}</sapn>
                  <span class="follow-sign">{{follow.sign}}</span>
                </div>
              </div>
            </div>
              
            </template>
          </el-skeleton>
        </div>
      </el-main>
    </el-container>
    
  </template>
  
  <script>
  import qs from "qs";
  import VideoList from '@/components/VideoList.vue'
  import HeaderVue from "@/components/HeaderVue.vue";
  export default {
    components: {
      VideoList, HeaderVue
    },
    data() {
      return {
        sign: '',
      avatar: 'https://via.placeholder.com/150',
      username: '未登录',
      isSuperAdmin:  false,
      favorites: [],
      follows: [],
      activeIndex: 0,
      comments: [],
      videoList: [],
      messages: [],
      complains: [],
      followed: true,
      loading:true,
      id:0,
      }
    },
    methods: {
      fetchVedios(){
        this.$axios({
          method: 'get',           /* 指明请求方式，可以是 get 或 post */
          url: 'http://127.0.0.1:8000/user/getvideo/',       /* 指明后端 api 路径，由于在 main.js 已指定根路径，因此在此处只需写相对路由 */
          headers: { "content-type": "application/x-www-form-urlencoded" },
          params:({      /* 需要向后端传输的数据，此处使用 qs.stringify 将 json 数据序列化以发送后端 */
            id: this.id,
          })
        })
        .then(res => {              /* res 是 response 的缩写 */
          switch (res.status) {
            case 200:
            // this.videoList=JSON.stringify(res.data.videos);
            this.videoList=res.data.videos;
              break;
            case 401:
              this.$message.error("未知错误");
              break;
          }
        })
        .catch(err => {
          console.log(err);         /* 若出现异常则在终端输出相关信息 */
        })
      },
      fetchFavorites(){
        this.$axios({
          method: 'get',           /* 指明请求方式，可以是 get 或 post */
          url: 'http://127.0.0.1:8000/user/getlike/',       /* 指明后端 api 路径，由于在 main.js 已指定根路径，因此在此处只需写相对路由 */
          headers: { "content-type": "application/x-www-form-urlencoded" },
          params:{      /* 需要向后端传输的数据，此处使用 qs.stringify 将 json 数据序列化以发送后端 */
            id: this.id,
          }
        })
        .then(res => {              /* res 是 response 的缩写 */
          switch (res.status) {
            case 200:
            this.videoList=res.data.videoDetails;
              break;
            case 401:
              this.$message.error("未知错误");
              break;
          }
        })
        .catch(err => {
          console.log(err);         /* 若出现异常则在终端输出相关信息 */
        })
      },
      fetchFollows() {
        this.loading = true;
        setTimeout(() => (this.loading = false), 1000);
        this.$axios({
          method: 'get',           /* 指明请求方式，可以是 get 或 post */
          url: 'http://127.0.0.1:8000/user/getfollow/',       /* 指明后端 api 路径，由于在 main.js 已指定根路径，因此在此处只需写相对路由 */
          headers: { "content-type": "application/x-www-form-urlencoded" },
          params:{      /* 需要向后端传输的数据，此处使用 qs.stringify 将 json 数据序列化以发送后端 */
            id: this.id,
          }
        })
        .then(res => {              /* res 是 response 的缩写 */
          switch (res.status) {
            case 200:
              this.follows=res.data.followings;
              break;
            case 401:
              this.$message.error("未知错误");
              break;
          }
        })
        .catch(err => {
          console.log(err);         /* 若出现异常则在终端输出相关信息 */
        })
      },
      handleSelect(key, keyPath) {
        this.activeIndex = key; // 更新activeIndex的值
        if (key === "1") {
          this.fetchVedios();
        } else if (key === "2") {
          this.fetchFavorites();
        } else if (key === "3") {
          this.fetchFollows();
        }
        console.log(key, keyPath);
      },
      startEditing() {
        this.editing = true;
        this.$nextTick(() => {
          this.$refs.signatureInput.focus();
        });
      },
      stopEditing() {
        this.editing = false;
      }
    },
    created() {
      // this.mess = JSON.parse(localStorage.getItem("otheruser"));
      var userID = this.$route.params.userID;
      this.$axios({
        method: 'get',           /* 指明请求方式，可以是 get 或 post */
        url: 'http://127.0.0.1:8000/user/userprofile/',
        headers: { "content-type": "application/x-www-form-urlencoded" },
        params: {      /* 需要向后端传输的数据，此处使用 qs.stringify 将 json 数据序列化以发送后端 */
          id: userID,
        }
      })
      .then(res => {              /* res 是 response 的缩写 */
        switch (res.status) {
          case 200:
            this.username = res.data.userData.username;
            this.sign = res.data.userData.sign;
            this.avatar = res.data.userData.avatarUrl;
            this.isSuperAdmin=res.data.userData.isSuperAdmin;
            this.id=res.data.userData.id;
            break;
          case 401:
            this.$message.error("未知错误");
            break;
        }
      })
      .catch(err => {
        console.log(err);         /* 若出现异常则在终端输出相关信息 */
      })
    },
    watch: {
      "$route.params.userID"(newval, oldval) {
        var userID = this.$route.params.userID;
        this.$axios({
          method: 'get',           /* 指明请求方式，可以是 get 或 post */
          url: 'http://127.0.0.1:8000/user/userprofile/',
          headers: { "content-type": "application/x-www-form-urlencoded" },
          params: {      /* 需要向后端传输的数据，此处使用 qs.stringify 将 json 数据序列化以发送后端 */
            id: userID,
          }
        })
        .then(res => {              /* res 是 response 的缩写 */
          switch (res.status) {
            case 200:
              this.username = res.data.userData.username;
              this.sign = res.data.userData.sign;
              this.avatar = res.data.userData.avatarUrl;
              this.isSuperAdmin=res.data.userData.isSuperAdmin;
              this.id=res.data.userData.id;
              this.$router.go(0);
              break;
            case 401:
              this.$message.error("未知错误");
              break;
          }
        })
        .catch(err => {
          console.log(err);         /* 若出现异常则在终端输出相关信息 */
        })
      },
    }
  };
  </script>
  
  <style scoped>
  /* 消息容器 */
  .messages-container {
    width:100%;
  }
  
  
  .message {
    display: flex;
    flex-direction: column;
    padding: 10px;
    border-bottom: 1px solid #ccc;
  }
  
  .message-username {
    font-size: 12px;
    margin-bottom: 5px;
    text-align:left
  
  }
  .message-username-color{
    color: rgb(57, 141, 214);
  }
  .message-info {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .message-content {
    font-size: 14px;
  }
  
  .message-time {
    font-size: 12px;
    color: #999;
  }
  .user-profile {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .user-info-background{
    background-color: rgba(255,255,255,0.33);
    border: none;
    width: 300px;
    height: 50px;
    resize: none;
    font-family:"PingFang SC";
  }
  .header {
    background-image: url('../assets/card_after_training\ \(1\).png');
    width:100%;
    display: flex;
    margin-bottom: 2rem;
    /* margin-left: -60%; */
  }
  
  .avatar-container {
    position: relative;
    margin-right: 1rem;
  }
  
  .avatar {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    object-fit: cover;
    cursor: pointer;
  }
  
  .user-info {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }
  
  
  .menu-container {
    width: 100%;
    display: flex;
    justify-content: center;
  }
  
  .el-menu {
    width: 100%;
  }
  
  .el-menu-item {
    width: 15%;
    text-align: center;
  }
    .favorites-container {
      display: flex;
      flex-wrap: wrap;
      width: 100%;
    }
  
    .favorite-video {
      margin-left: 2.5%;
      margin-right: 2.5%;
      margin-top: 3.5%;
      
      width: 20%;    
      display: inline-flex;
      flex-direction: column;
      align-items: center;
    }
  
    .video-cover {
      width: 200px;
      height: 112px;
      object-fit: cover;
      cursor: pointer;
    }
  
    .video-title {
      margin-top: 8px;
      text-align: center;
    }
    
    .follows-container {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-around;
      width: 100%;
    }
    .follow-container:last-child{
      border-bottom: none;
      padding-bottom: 0;
      margin-bottom: 0;
    }
    .follow-container {
    border-bottom: 1px solid #EBEEF5;
    padding-bottom: 15px;
    display: flex;
    align-items: center;
    margin-bottom: 10px;
    margin-top: 10px;
    width: 100%;
    }
    .follow-avatar {
      width: 50px;
      height: 50px;
      border-radius: 50%;
      object-fit: cover;
      margin-right: 10px;
  
    }
    .follow-container .user-info{
      display: flex; 
      flex-direction: column;
      flex: 1;
    }
    .follow-username {
      font-size: 16px;
      margin-bottom: 10px;
      /* margin-right: 230px; */
    }
    .follow-sign{
      font-family:"PingFang SC";
      color: rgb(142, 148, 148);
      font-size: smaller;
      margin-right: 230px;
      
    }
    .follow-button {
      margin-left: auto;
    }
    .comments-container {
    margin-top: 20px;
    width: 100%;
  }
  .comment {
    display: flex;
    align-items: center;
  }
  
  .created-time {
    font-size: 12px;
    color: #888;
    margin-right: 10px;
  }
  
  /* .delete-button {
    background-color: red;
    color: white;
    padding: 5px 10px;
    border-radius: 5px;
    cursor: pointer;
  } */
  
  .comment-content {
    flex-grow: 1;
    color: #141414;
  }
  
  .logout-button {
    position: absolute;
    top: 1%;
    right: 0.5%;
    font-size:x-small;
  }
  </style>