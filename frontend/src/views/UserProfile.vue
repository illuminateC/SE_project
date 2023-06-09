<template>
  <el-container>
    <el-header>
      <HeaderVue/>
    </el-header>
    <el-main>
      <div class="user-profile">
      <div class="header">
        <div class="avatar-container">
          <input type="file" id="avatarInput" @change="uploadAvatar" hidden accept="image/*">
          <img :src="avatar" @click="changeAvatar" class="avatar">
        </div>
        <div class="user-info">
          <h2>{{username}}</h2>
          <textarea placeholder="这个人很懒，什么也没留下~" v-model="sign" class="user-info-background" maxlength="16" @blur="saveSign"></textarea>
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
          <el-menu-item index="4">
            <i class="el-icon-chat-dot-round"></i>
            评论
          </el-menu-item>
          <el-menu-item index="5">
            <i class="el-icon-message"></i>
            消息
          </el-menu-item>
          <el-menu-item index="6" v-if="isSuperAdmin">
            <i class="el-icon-bell"></i>
            待审核
          </el-menu-item>
        </el-menu>
      </div>
        <div class="video-container">
          <VideoList :videos="videoList" v-if="activeIndex === '1'" />
        </div>
        <div class="video-container">
          <VideoList :videos="videoList" v-if="activeIndex === '2'" />
        </div>

      
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
                <el-button class="follow-button" :type="follow.isFollow ? 'info' : 'primary'" @click="toggleFollow(follow)">
                  {{ follow.isFollow ? '取消关注' : '关注' }}
                </el-button>
              </div>
            </div>
            
          </template>
      </el-skeleton>

      <el-skeleton :loading="loading" style="width: 100%" animated v-if="activeIndex === '4'">
        <template slot="template">
          <div class="comments-container" v-if="comments == undefined ||comments == null || comments.length <= 0">
            <div class="comment">
              <el-skeleton-item variant="text" style="width: 60px; margin-top: 0px; " />
              <el-skeleton-item variant="text" style="width: 30%; margin-top: 0px; margin-left: 5%; " />
              <el-skeleton-item variant="button" style="width: 40px; height: 40px;  border-radius: 50%; margin-top:0px; margin-left: 58%;" />
            </div>
          </div>
          <div class="comments-container" v-for="comment in comments">
            <div class="comment">
              <el-skeleton-item variant="text" style="width: 60px; margin-top: 0px; " />
              <el-skeleton-item variant="text" style="width: 30%; margin-top: 0px; margin-left: 5%; " />
              <el-skeleton-item variant="button" style="width: 40px; height: 40px;  border-radius: 50%; margin-top:0px; margin-left: 58%;" />
            </div>
          </div>
        </template>
        <template>
          <div class="comments-container" v-for="comment in comments">
            <div class="comment" >
              <span class="created-time">{{comment.createdTime.split("T")[0]}}</span>
              <div class="comment-content"><router-link :to='"/video/"+ comment.videoID ' style="text-decoration: none"><a>{{comment.content}}</a></router-link></div>
              <el-button type="danger" icon="el-icon-delete" circle @click="deleteComment(comment)"></el-button>
            </div>
          </div>
        </template>
      </el-skeleton>

      <el-skeleton :loading="loading" style="width: 100%" animated v-if="activeIndex === '5'">
        <template slot="template">
          <div class="messages-container" v-if="messages == undefined ||messages == null || messages.length <= 0">
            <div class="message">
              <div class="message-username"><el-skeleton-item variant="text" style="width: 100px; margin-top: 0px; " /></div>
              <div class="message-info">
                <el-skeleton-item variant="text" style="width: 160px; margin-top: 0px; " />
                <el-skeleton-item variant="text" style="width: 80px; margin-top: 0px; " />
              </div>
            </div>
          </div>
          <div class="messages-container" v-for="message in messages">
            <div class="message">
              <div class="message-username"><el-skeleton-item variant="text" style="width: 100px; margin-top: 0px; " /></div>
              <div class="message-info">
                <el-skeleton-item variant="text" style="width: 160px; margin-top: 0px; " />
                <el-skeleton-item variant="text" style="width: 80px; margin-top: 0px; " />
              </div>
            </div>
          </div>
        </template>
        <template>
          <div class="messages-container" v-for="message in messages">
            <div class="message">
              <div class="message-username">来自<span class="message-username-color">{{message.fromName}}</span>的信息：</div>
              <div class="message-info">
                <div class="message-content">{{message.content}}</div>
                <span class="message-time">{{message.createdTime.split("T")[0]}}</span>
              </div>
            </div>
          </div>
        </template>
      </el-skeleton>

      <div class="messages-container" v-if="activeIndex === '6'" v-for="complain in complains">
        <div class="message">
          <div class="message-username">对视频<router-link :to='"/video/"+ complain.videoID ' style="text-decoration: none"><a class="message-username-color" >{{complain.title}}</a></router-link>的投诉：</div>
          <div class="message-info">
            <div class="message-content">{{complain.content}}</div>
            <span class="message-time">投诉用户：{{complain.username}}</span>
          </div>
        </div>
      </div>
    </div>
    </el-main>
  </el-container>
</template>

<script>
import qs from "qs";
import VideoList from '@/components/VideoList.vue'
import HeaderVue from "@/components/HeaderVue.vue";
import router from "@/router";
export default {
  components: {
    HeaderVue,
    VideoList,
    router
},
  data() {
    return {
      sign: '',
      avatar: '',
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
    toggleFollow(follow) {
      console.log(follow);
      if(follow.isFollow==true){
        follow.isFollow=false;
        this.$axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/user/disfollow/',
          headers: { "content-type": "application/x-www-form-urlencoded" },       
          data: ({      
            userID:this.id,
            fanId:follow.id,
          })
        })
        .catch(err => {
          console.log(err); 
        })
      }else if(follow.isFollow==false){
        follow.isFollow=true;
        this.$axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/user/follow/',    
          headers: { "content-type": "application/x-www-form-urlencoded" },     
          data:({      
            userID:this.id,
            fanId:follow.id,
          })
        })
        .catch(err => {
          console.log(err); 
        })
      }
    },
    jumpOtheruser(id){
      this.$router.push('/otherUser/' + id);
    },
    changeAvatar() {
      document.getElementById('avatarInput').click();
    },
    uploadAvatar(event) {
      if (event.target.files && event.target.files[0]) {
        const reader = new FileReader();
        reader.onload = e => {
          this.avatar = e.target.result;
        };
        reader.readAsDataURL(event.target.files[0]);
        const formData = new FormData();
        formData.append('avatar', event.target.files[0]);
        formData.append('id', this.id);
        this.$axios({
          method: 'post',           /* 指明请求方式，可以是 get 或 post */
          url: 'http://127.0.0.1:8000/user/avatar/',       /* 指明后端 api 路径，由于在 main.js 已指定根路径，因此在此处只需写相对路由 */
          headers: { "content-type": "application/x-www-form-urlencoded" },
          data:formData,
        })
        .catch(err => {
          console.log(err);         /* 若出现异常则在终端输出相关信息 */
        })
      }
    },
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
    fetchComments() {
      this.loading = true;
      setTimeout(() => (this.loading = false), 1000);
      this.$axios({
        method: 'get',           /* 指明请求方式，可以是 get 或 post */
        url: 'http://127.0.0.1:8000/user/getwords/',       /* 指明后端 api 路径，由于在 main.js 已指定根路径，因此在此处只需写相对路由 */
        headers: { "content-type": "application/x-www-form-urlencoded" },
        params:{      /* 需要向后端传输的数据，此处使用 qs.stringify 将 json 数据序列化以发送后端 */
          id: this.id,
        }
      })
      .then(res => {              /* res 是 response 的缩写 */
        switch (res.status) {
          case 200:
            this.comments=res.data.commentsDetails;
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
    fetchMessages() {
      this.loading = true;
      setTimeout(() => (this.loading = false), 1000);
      this.$axios({
        method: 'get',           /* 指明请求方式，可以是 get 或 post */
        url: 'http://127.0.0.1:8000/user/getmessage/',       /* 指明后端 api 路径，由于在 main.js 已指定根路径，因此在此处只需写相对路由 */
        headers: { "content-type": "application/x-www-form-urlencoded" },
        params: ({      /* 需要向后端传输的数据，此处使用 qs.stringify 将 json 数据序列化以发送后端 */
          id: this.id,
        })
      })
      .then(res => {              /* res 是 response 的缩写 */
        switch (res.status) {
          case 200:
            this.messages=res.data.messagesDetails;
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
    deleteComment(comment) {
      this.$axios({
        method: 'post',           /* 指明请求方式，可以是 get 或 post */
        url: 'http://127.0.0.1:8000/user/deletecontent/',       /* 指明后端 api 路径，由于在 main.js 已指定根路径，因此在此处只需写相对路由 */
        headers: { "content-type": "application/x-www-form-urlencoded" },
        data: ({      /* 需要向后端传输的数据，此处使用 qs.stringify 将 json 数据序列化以发送后端 */
          id: comment.id,
        })
      })
      .then(res => {              /* res 是 response 的缩写 */
        switch (res.status) {
          case 200:
            this.fetchComments();
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
    fetchComplains(){
      this.$axios({
        method: 'get',           /* 指明请求方式，可以是 get 或 post */
        url: 'http://127.0.0.1:8000/user/getcomplain/',       /* 指明后端 api 路径，由于在 main.js 已指定根路径，因此在此处只需写相对路由 */
        headers: { "content-type": "application/x-www-form-urlencoded" },
      })
      .then(res => {              /* res 是 response 的缩写 */
        switch (res.status) {
          case 200:
            this.complains=res.data.complaintList;
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
    saveSign(){
      this.$axios({
        method: 'post',           /* 指明请求方式，可以是 get 或 post */
        url: 'http://127.0.0.1:8000/user/sign/',       /* 指明后端 api 路径，由于在 main.js 已指定根路径，因此在此处只需写相对路由 */
        headers: { "content-type": "application/x-www-form-urlencoded" },
        
        data: ({      /* 需要向后端传输的数据，此处使用 qs.stringify 将 json 数据序列化以发送后端 */
          id: this.id,
          sign: this.sign
        })
      })
      .then(res => {              /* res 是 response 的缩写 */
        switch (res.data.result) {
          case 200:
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
      }else if (key === "4") {
        this.fetchComments();
      }else if(key === "5") {
        this.fetchMessages();
      }else if(key === "6"){
        this.fetchComplains();
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
    },
    handleLogout() {
      this.$confirm('确认退出登录吗？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        localStorage.removeItem('user');
        this.$router.push('/login');
      }).catch(() => {});
    }
  },
  created() {
    this.mess = JSON.parse(localStorage.getItem("user")).id;
    this.$axios({
        method: 'get',           /* 指明请求方式，可以是 get 或 post */
        url: 'http://127.0.0.1:8000/user/userprofile/',
        headers: { "content-type": "application/x-www-form-urlencoded" },
        params: {      /* 需要向后端传输的数据，此处使用 qs.stringify 将 json 数据序列化以发送后端 */
          id: this.mess,
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
  margin-top: 5px;
  width: 100%;
}
.comment {

  display: flex;
  align-items: center;
  border-bottom: 1px solid #ccc;
  padding-bottom: 5px; /* 新增 */
  margin-bottom: 10px; /* 新增 */
}

.created-time {
  font-size: 12px;
  color: #888;
  margin-right: 10px;
}

.comment-content {
  flex-grow: 1;
  color: #141414;
  text-align: left;
  margin-left: 5%;
}

.logout-button {
  position: absolute;
  top: 1%;
  right: 0.5%;
  font-size:x-small;
}

.video-container {
  width: 100%;
  /* background-color: aqua; */
}
</style>