<template>
    <el-card :body-style="{ padding: '0px' }" class="user-card">
      <router-link :to="checkRouterLink(singleUser.id)">
        <el-col :span="6">
            <el-avatar shape="circle" :size="100" :src="singleUser.avatarUrl"></el-avatar>
        </el-col>
      </router-link>
      <el-col :span="18">
          <div class="user-information">
              <el-row class="username"> {{ singleUser.username }} </el-row>
              <el-row class="detail"> {{ singleUser.fanNum }}粉丝 · {{ singleUser.videoNum }}视频   {{ singleUser.description }}</el-row>
              <el-row class="follow-button"> 
                <el-button type="info" v-if="this.singleUser.id === tmpID">你自己 desu</el-button>
                <el-button type="info" v-else-if="isFollowed" @click="cancelFollow"> - 取消关注</el-button>
                <el-button type="primary" v-else @click="follow"> + 关注</el-button>
              </el-row>
          </div>
      </el-col>
    </el-card>
</template>
<script>
import router from '@/router';

  export default {
    props: {
        singleUser: {
            type: Object,
            default() {
                return {
                    id: 24,
                    avatarUrl: "https://cover-1309504341.cos.ap-beijing.myqcloud.com/69.jpg",
                    username: "usertest",
                    description: "测试hhhh",
                    videoNum: 5,
                    fanNum: 0,
                };
            },
        },
    },
    data() {
      return {
        isFollowed: false,
        tmpID: 0
      }
    },
    methods: {
      checkRouterLink(id) {
        console.log("id:" + id);
        let userInfo = JSON.parse(localStorage.getItem("user"));
        let user_id = 0;
        if (userInfo === null) {
          user_id = 0;
        } else {
          user_id = userInfo.id;
          this.tmpID = userInfo.id;
        }
        if (this.singleUser.id === user_id) {
            return '/userprofile';
        } else {
            return '/otherUser/' + id;
        }
      },
      follow() {
        let formData = new FormData();
        let userInfo = JSON.parse(localStorage.getItem("user"));
        if (userInfo === null) {
          this.$message.warning("请先登录！");
          this.$router.push('/login');
          return;
        }
        formData.append('userID', userInfo.id);
        formData.append('fanId', this.singleUser.id);
        this.$axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/user/follow/',
          headers: { "content-type": "application/x-www-form-urlencoded" },
          data: formData,
        })
        .then((res) => {
          this.$message.success("关注成功！");
          this.isFollowed = true;
          this.singleUser.fanNum++;
        })
        .catch((err) => {
          console.log(err);
        });
      },
      cancelFollow() {
        let formData = new FormData();
        let userInfo = JSON.parse(localStorage.getItem("user"));
        if (userInfo === null) {
          this.$message.warning("请先登录！");
          this.$router.push('/login');
          return;
        }
        formData.append('userID', userInfo.id);
        formData.append('fanId', this.singleUser.id);
        console.log(this.singleUser.id + "disfollow");
        this.$axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/user/disfollow/',
          headers: { "content-type": "application/x-www-form-urlencoded" },
          data: formData,
        })
        .then((res) => {
          console.log(res);
          this.$message.success("取消关注成功！");
          this.isFollowed = false;
          this.singleUser.fanNum--;
        })
        .catch((err) => {
          console.log(err);
        });
      },
    },
    components: { router },
    created() {
      let userInfo = JSON.parse(localStorage.getItem("user"));
      let userID = 0;
      if (userInfo === null) {
        console.log("游客搜索");
      } else {
        console.log("用户搜索");
        userID = userInfo.id;
      }
      this.$axios({
        method: 'get',           
        url: 'http://127.0.0.1:8000/index/isfollowed/',      
        headers: { "content-type": "application/x-www-form-urlencoded" },
        params:{      
          userID: userID,
          queryID: this.singleUser.id
        }
      }).then(res => {              /* res 是 response 的缩写 */
        this.isFollowed=res.data.isFollowed;
        console.log("query=" + this.singleUser.id + " and user=" + userID);
      })
      .catch(err => {
        console.log("query=" + this.singleUser.id + " and user=" + userID);
      })
      console.log("搜索完成, isFollowed的值为:" + this.isFollowed);
      console.log("搜索完成, singleUser的值为:" + this.singleUser.id);
    }
};
</script>
<style>
  .image {
    width: 200px;
    height: 100px;
    display: block;
  }

  .user-card {
    height: 120px;
    width: 700px;
  }

  .username {
    text-align: left;
    font-size: 20px;
    font-weight: bold;
  }

  .detail {
    text-align: left;
    color:dimgrey;
    font-size: 14px;
  }

  .follow-button {
    text-align: left;
  }

  .user-information {
    line-height: 2em;
  }

</style>
