<template>
  <div>
    <div class="card_wrap">
      <div class="card_body">
        <ul>
          <li style="vertical-align: middle; line-height: 50px" @click="toUserHome(user.id)">
            <el-avatar :size="50" :src="user.avatarUrl" style="cursor: pointer">
            </el-avatar>
          </li>
          <li>
            <div class="title_profile">
              <span class="name" @click="toUserHome(user.id)">{{
                user.username
              }}</span>
            </div>
          </li>
          <li style="float: right; vertical-align: middle; line-height: 50px">
            <el-button type="warning" size="small" plain @click="toUserHome(user.id)" v-if="user.id === userId"><i
                class="el-icon-s-promotion" />进入我的空间</el-button>
            <el-button type="warning" size="small" plain @click="follow" v-else-if="user.isFollowed === false"><i
                class="el-icon-plus" /> 关注up主</el-button>
            <el-button type="warning" size="small" plain @click="cancelFollow" v-else><i class="el-icon-minus" />
              取消关注</el-button>
          </li>
        </ul>
      </div>
      <div class="card_footer">
        <ul>
          <li>
            <span class="foot_text">
              粉丝数量: {{ user.fanNum }}
            </span>
          </li>
          <li>
            <span class="foot_text">
              视频数量: {{ user.videoNum }}
            </span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
  
<script>
export default {
  props: {
    user: {
      type: Object,
      default() {
        return {
        };
      },
    },
    listType: {
      type: Number,
      default() {
        return 1;
      },
    },
  },
  data() {
    return {
      isfollow: this.user.isFollowed,
      userId: JSON.parse(localStorage.getItem("user")).id
    };
  },
  methods: {
    cancelFollow() {
      let formData = new FormData();
      let userInfo = JSON.parse(localStorage.getItem("user"));
      if (userInfo === null) {
        this.$message.warning("请先登录！");
        this.$router.push('/login');
        return;
      }
      formData.append('userID', userInfo.id);
      formData.append('fanId', this.user.id);
      console.log(this.user.id + "disfollow");
      this.$axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/user/disfollow/',
        headers: { "content-type": "application/x-www-form-urlencoded" },
        data: formData,
      })
        .then((res) => {
          console.log(res);
          switch (res.status) {
            case 200:
              this.$message.success("取消关注成功！");
              this.user.isFollowed = false;
              this.user.fanNum--;
              break;

            default:
              this.$message.warning("取消关注失败！");
              break;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    toUserHome(id) {
      if (localStorage.getItem("user") != null) {
        var user_id = JSON.parse(localStorage.getItem("user")).id;
        if (id == user_id) this.$router.push('/userprofile');
        else this.$router.push('/otherUser/' + id);
      } else this.$router.push('/otherUser/' + id);
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
      formData.append('fanId', this.user.id);
      console.log(this.user.id + "user.id");
      this.$axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/user/follow/',
        headers: { "content-type": "application/x-www-form-urlencoded" },
        data: formData,
      })
        .then((res) => {
          console.log(res);
          switch (res.status) {
            case 200:
              this.$message.success("关注成功！");
              this.user.isFollowed = true;
              this.user.fanNum++;
              break;

            default:
              this.$message.warning("关注失败！");
              break;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  mounted() {
    this.isfollow = this.user.isFollowed;
  },
  watch: {
    user(newValue, oldValue) {
      this.isfollow = newValue.isfollow;
    },
  },
};
</script>

<style scoped>
.card_wrap {
  height: 85px;
  border-radius: 10px;
  /* border: solid 2px rgb(233, 196, 214); */
  border: solid 0.5px #ffb4441b;
  padding-top: 10px;
  box-shadow: 0 0.5px 0 0.5px #ffb44414;
}

.card_body {
  height: 50px;
  width: 100%;
  top: 0;
}

.card_body ul {
  padding-left: 10px;
  margin: 0;
}

.card_body li {
  list-style: none;
  float: left;
  margin-right: 20px;
  display: inline-block;
  height: 50px;
  vertical-align: middle;
}

.title_profile {
  height: 50px;
}

.name {
  font-size: 17px;
  height: 30px;
  line-height: 30px;
  cursor: pointer;
  text-align: left;
  display: block;
  color: #e6a23c;
}

.profile {
  font-size: 13px;
  color: grey;
  line-height: 20px;
  text-align: left;
  height: 20px;
  display: block;
  word-break: break-all;
  word-wrap: break-word;
}

.follow {
  font-size: 13px;
  color: grey;
}

.card_footer {
  height: 20px;
  margin-top: 3px;
}

.card_footer ul {
  margin: 0;
  padding-left: 10px;
  line-height: 20px;
}

.card_footer li {
  list-style: none;
  float: left;
  margin-right: 10px;
  display: inline-block;
  height: 20px;
  vertical-align: middle;
  line-height: 20px;
}

.foot_text {
  font-size: 13px;
  color: grey;
}
</style>