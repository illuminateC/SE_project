<template>
    <el-row :gutter="10" class="col-center">
        <el-col :span="6">
            <div class="my-logo">
                <router-link to="/homepage">               
                    <img
                    src="@/assets/logo.png"
                    width="150px"
                    height="50px"
                    style="margin-right: 16vw; margin-left: 20px"
                    />
                </router-link>
            </div>
        </el-col>
        <el-col :span="15">
            <el-input 
                class="search-box"
                v-model="inputContext" 
                placeholder="搜索你感兴趣的内容" 
                prefix-icon="el-icon-search"
                clearable
                @keyup.enter.native="searchContext()"
            >
        </el-input>
        <el-button type="primary" icon="el-icon-search" circle @click="searchContext"></el-button>           
        </el-col>
        <el-col :span="3">
            <el-col :span="12">
                <div class="avatar" @mouseenter="showCard" @mouseleave="hideCard" ref="avatarCard">
                    <router-link to="/userprofile"> 
                        <el-avatar shape="circle" :size="size" :src="avatarUrl"></el-avatar>
                    </router-link>
                </div>
                <div class="card" v-show="showCardFlag" @mouseenter="cardHover" @mouseleave="cardLeave" ref="card">
                    <div style="padding: 14px;">
                        <h3 style="color:deeppink;"> {{ username }} </h3>
                        <div>
                            <i style="font-weight: bold"> {{ followNum }} </i> 关注  
                            <i style="font-weight: bold"> {{ fanNum }} </i>  粉丝
                        </div>
                    </div>
                    <div>
                        <router-link to="/userprofile">
                            <el-button type="text" icon = "el-icon-user" style="font-size: 18px;"> 个人中心 </el-button>
                        </router-link>
                    </div>
                    <div>
                        <el-button type="text" icon = "el-icon-arrow-right" @click="logOut()" style="font-size: 18px;" v-if="isLogIn === true"> 退出登录 </el-button>
                    </div>
                </div>                
            </el-col>
            <el-col :span="12">
                <router-link to="/uploadview">
                    <el-button type="danger" round>投稿</el-button>
                </router-link>
            </el-col>
        </el-col>
    </el-row>
</template>

<script>
import qs from "qs"
export default {
    data() {
        return {
            avatarUrl: "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png",
            username: "游客",
            fanNum: 0,
            followNum: 0,
            inputContext: "",
            logoUrl: "@/assets/logo.png",
            showCardFlag: false,
            isLogIn: false,
        }
    },
    computed: {
    },
    methods: {
        searchContext: function () {
            console.log(this.inputContext);
            if (this.inputContext === "") {
                this.$message({
                    type: "error",
                    message: "输入点东西呀QAQ",
                });
                return;
            }
            localStorage.removeItem("searchContent"); // 每次搜索到结果之后将旧的搜索结果删除存入新的搜索结果
            localStorage.setItem("searchContent", this.inputContext);
            console.log("header search desu");
            if (this.$route.path === '/search') {
                console.log("Already in searchPage");
                this.$router.go(0);
            } else {
                console.log("Not in searchPage");
                this.$router.push("/search");
            }
        },
        showCard() {
            this.showCardFlag = true;
            // this.$message({
            //     type: "error",
            //     message: "展示card",
            // });
        },
        hideCard() {
            if (!this.$refs.card.contains(event.relatedTarget)) {
            this.showCardFlag = false;
            }
        },
        cardHover() {
            this.showCardFlag = true;
        },
        cardLeave() {
            if (!this.$refs.avatarCard.contains(event.relatedTarget)) {
            this.showCardFlag = false;
            }
        },
        logOut() {
            this.$confirm('确认退出登录吗？', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                localStorage.removeItem("user");
                this.isLogIn = false;
                this.avatarUrl = "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png";
                this.username = "游客";
                this.fanNum = 0;
                this.followNum = 0;
                this.$router.push("/");
            })
        }
    },
    created() {
        var user_id;
        if (localStorage.getItem("user") == null) {
            user_id = null;
        }
        else {
            let user_id = JSON.parse(localStorage.getItem("user")).id;
            console.log(user_id + 'header userID');
        }
        this.$axios({
            method: "get",
            url: "http://127.0.0.1:8000/user/userprofile/",
            headers: { "content-type": "application/x-www-form-urlencoded" },
            params: {id: JSON.parse(localStorage.getItem("user")).id}
        }).then((res) => {
            var userData = res.data.userData;
            this.avatarUrl = userData.avatarUrl;
            this.username = userData.username;
            this.fanNum = userData.fanNum;
            this.followNum = userData.followNum;
            this.isLogIn = true;
        });
    }
}
</script>

<style>
.my-logo {
    max-width: 100%;
    max-height: 100%;
}

.search-line {
    right: 0%;
    display: flex;
    align-items: center;
}

.search-box {
    width: 500px;
    margin-right: 10px;
}

.avatar {
    right: 0px;
}

.col-center {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  box-shadow: 0 2px 0px rgba(0, 0, 0, 0.1);
}

.card {
  position: absolute;
  top: calc(100% - 5px);
  right: -8%;
  transform: translateX(-50%);
  width: 240px;
  background-color:rgb(227, 237, 240);
  /* background-color: #fff; */
  border-radius: 4px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  padding: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  border-radius:18px
}
</style>
