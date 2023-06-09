<template>

<div id="login">
<video autoplay loop muted id="bgvid">
  <source src="../assets/官网.mp4" type="video/mp4">
</video>
<el-container>
<el-header class="my-header">
  <HeaderVue />
</el-header>
<el-main>
<!-- <img class="bgbox" src="../assets/ys.png"> -->
<div class="container" :class="{'right-panel-active': isRightPanelActive}" id="login-box">
  <div class="form-container sign-up-container">
    <form>
      <h1>注册</h1>
      <div class="txtb">
        <input type="text" v-model="signupUsername" @focus="onFocus" @blur="onBlur"  maxlength="8">
        <span data-placeholder="用户名"></span>
      </div>
      <div class="txtb">
        <input type="password" v-model="signupPassword" @focus="onFocus" @blur="onBlur"  maxlength="16">
        <span data-placeholder="密码"></span>
      </div>
      <div class="txtb">
        <input type="password" v-model="signupConfirmPassword" @focus="onFocus" @blur="onBlur" maxlength="16">
        <span data-placeholder="确认密码"></span>
      </div>
      <button @click.prevent="onSignUp">注册</button>
    </form>
  </div>
  <div class="form-container sign-in-container">
    <form>
      <h1>登录</h1>
      <div class="txtb">
        <input type="email" v-model="signinUsername" @focus="onFocus" @blur="onBlur">
        <span data-placeholder="用户名"></span>
      </div>
      <div class="txtb">
        <input type="password" v-model="signinPassword" @focus="onFocus" @blur="onBlur">
        <span data-placeholder="密码"></span>
      </div>
      <button @click.prevent="onSignIn">登录</button>
    </form>
  </div>
  <div class="overlay-container">
    <div class="overlay">
      <div class="overlay-panel overlay-left">
        <h1>已有账号？</h1>
        <p>快来打开新世界的大门吧~</p>
        <button class="ghost" @click="isRightPanelActive = false">登录</button>
      </div>
      <div class="overlay-panel overlay-right">
        <h1>没有账号?</h1>
        <p>加入我们，和大家愉快玩耍吧owo</p>
        <button class="ghost" @click="isRightPanelActive = true">注册</button>
      </div>
    </div>
  </div>
</div>
</el-main>
</el-container>
</div>
</template>
<script>
import qs from "qs"
import HeaderVue from '@/components/UploadHeader.vue'
export default {
  data() {
    return {
      isRightPanelActive: false,
      signupUsername: '',
      signupPassword: '',
      signupConfirmPassword: '',
      signinPassword: '',
      signinUsername: '',
    }
  },
  components: { HeaderVue },
  methods: {
    onSignIn: function() {
      // 检查表单是否有填写内容
      if (this.signinUsername === '' || this.signinPassword === '') {
        this.$message.warning("请输入用户名和密码！");
        return;
      }

      this.$axios({
        method: 'get',           /* 指明请求方式，可以是 get 或 post */
        url: 'http://127.0.0.1:8000/user/login/',       /* 指明后端 api 路径，由于在 main.js 已指定根路径，因此在此处只需写相对路由 */
        headers: { "content-type": "application/x-www-form-urlencoded" },
        params: {      /* 需要向后端传输的数据，此处使用 qs.stringify 将 json 数据序列化以发送后端 */
          username: this.signinUsername,
          password: this.signinPassword
        }
        // data: qs.stringify({      /* 需要向后端传输的数据，此处使用 qs.stringify 将 json 数据序列化以发送后端 */
        //   // username: this.signinUsername,
        //   // password: this.signinPassword
        //   username: "测试用户1",
        //   password: "123"
        // })
      })
      .then(res => {              /* res 是 response 的缩写 */
        switch (res.status) {
          case 200:
            localStorage.setItem("user",JSON.stringify(res.data.userData));
            const history_pth = localStorage.getItem('preRoute');
            /* 若保存的路由为空或为注册路由，则跳转首页；否则跳转前路由（setTimeout表示1000ms后执行） */
            this.$message.success("登录成功！");
            console.log(history_pth + " history_path");
            console.log(res.data.userData.id + " return id");
            console.log(JSON.parse(localStorage.getItem("user")).id + " userID desu");
            setTimeout(() => {
              if (history_pth == null) {
                this.$router.push('/');
              } else {
                this.$router.push({ path: history_pth });
              }
            }, 1000);
            
            break;
          case 401:
            this.$message.error("用户名不存在！");
            break;
          case 402:
            this.$message.error("密码错误！");
            break;
          default:
            this.$message.error("default");
            break;
        }
      })
      .catch(err => {
        // console.log(res.status);         /* 若出现异常则在终端输出相关信息 */
        this.$message.error("登陆失败，请检查用户名或密码！");
      })
    },
    onSignUp: function() {
      if (this.signupUsername === '' || this.signupPassword === '' || this.signupConfirmPassword === '') {
          this.$message.warning("请填写完整的注册信息！");
          return;
        }
  
        if (this.signupPassword!== this.signupConfirmPassword) {
          this.$message.warning("两次输入的密码不一致！");
          return;
        }
        
        let passwordReg = /^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,16}$/;
          if (!passwordReg.test(this.signupPassword)) {
            this.$message.warning("密码必须为6到16位数字和英文的组合！");
            return;
          }
        this.$axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/user/register/',
          headers: { "content-type": "application/x-www-form-urlencoded" },
          // params: {}
          data: qs.stringify({
            username: this.signupUsername,
            password: this.signupPassword
          })
        })
        .then(res => {
          switch (res.status) {
            case 200:
              this.$message.success("注册成功！");
              this.isRightPanelActive = false;
              break;
            case 401:
              this.$message.error("用户名已存在！");
              break;
          }
        })
        .catch(err => {
          console.log(err);
        })
    },
    onFocus: function(event) {
      event.target.classList.add('focus');
    },
    onBlur: function(event) {
      if (event.target.value === '') {
          vent.target.classList.remove('focus');
      }
    }
  }
}
</script>

<style scoped>
.my-header {
    position: fixed;
    margin-left: -10px;
    top: 0;
    /* height: 200vh; */
    /* left: 0; */
    width: 100%;
    /* height: 10vh; */
    background-color: transparent;
    /* background-color:bisque; */
    z-index: 999;
}
source {
  min-width: 100%;
  min-height: 100%;
  height: auto;
  width: auto;
}
 
video {
  object-fit:cover;
  position: fixed;
  right: 0px;
  bottom: 0px;
  min-width: 100%;
  max-height: 100%;
  height: auto;
  width: auto;
  background-size: cover;
  /*加滤镜*/
  /* filter: blur(15px); //背景模糊设置 */
  /*-webkit-filter: grayscale(100%);*/
  /*filter:grayscale(100%); //背景灰度设置*/
  z-index: -11;
}

* {
    box-sizing: border-box;
}

h1 {
    font-weight: bold;
    margin: 0;
}
p {
    font-size: 14px;
    line-height: 20px;
    letter-spacing: .5px;
    margin: 20px 0 30px;
}
span {
    font-size: 12px;
}
a {
    color: #333;
    font-size: 14px;
    text-decoration: none;
    margin: 15px 0;
}
.container {
    background: #fff;
    border-radius: 10px;
    box-shadow: 0 14px 28px rgba(0, 0, 0, .25), 0 10px 10px rgba(0, 0, 0, .22);
    position: absolute;
    top: 50%;
    transform: translate(-50%, -50%);
    overflow: hidden;
    width: 768px;
    max-width: 100%;
    min-height: 480px;
    left: 50%;
    margin: 0 auto;

}

.form-container form {
    background: #fff;
    display: flex;
    flex-direction: column;
    padding: 0 50px;
    height: 100%;
    justify-content: center;
    text-align: center;
}
.social-container {
    margin: 20px 0;
}

.social-container a {
    border: 1px solid #ddd;
    border-radius: 50%;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    margin: 0 5px;
    height: 40px;
    width: 40px;
}

.social-container a:hover {
    background-color: #eee;

}

.txtb {
    border-bottom: 2px solid #adadad;
    position: relative;
    margin: 10px 0;
}

.txtb input {
    font-size: 15px;
    color: #333;
    border: none;
    width: 100%;
    outline: none;
    background: none;
    padding: 0 3px;
    height: 35px;
}

.txtb span::before {
    content: attr(data-placeholder);
    position: absolute;
    top: 50%;
    left: 5px;
    color: #adadad;
    transform: translateY(-50%);
    transition: .5s;
}
.txtb span::after {
    content: '';
    position: absolute;
    left: 0%;
    top: 100%;
    width: 0%;
    height: 2px;
    background-image: linear-gradient(120deg,#3498db,#8e44ad);
    transition: .5s;
}

.focus + span::before {
    top: -5px;
}

.focus + span::after {
    width: 100%;
}

button {
    border-radius: 20px;
    border: 1px solid #ff4b2b;
    background: #ff4b2b;
    color: #fff;
    font-size: 12px;
    font-weight: bold;
    padding: 12px 45px;
    letter-spacing: 1px;
    text-transform: uppercase;
    transition: transform 80ms ease-in;
    cursor: pointer;
}

button:active {
    transform: scale(.95);
}

button:focus {
    outline: none;
}

button.ghost {
    background: transparent;
    border-color: #fff;
}

.form-container {
    position: absolute;
    top: 0;
    height: 100%;
    transition: all .6s ease-in-out;
}

.form-container button {
    background: linear-gradient(120deg, #3498db, #8e44ad);
    border: none;
    background-size: 200%;
    color: #fff;
    transition: .5s;
}

.form-container button:hover {
    background-position: right;
}

.sign-in-container {
    left: 0;
    width: 50%;
    z-index: 2;
}
.sign-in-container form a {
    position: relative;
    left: 100px;
}
.sign-up-container {
    left: 0;
    width: 50%;
    z-index: 1;
    opacity: 0;
}
.sign-up-container button {
    margin-top: 20px;
}
.overlay-container {
    position:absolute;
    top: 0;
    left: 50%;
    width: 50%;
    height: 100%;
    overflow: hidden;
    transition: transform .6s ease-in-out;
    z-index: 100;
}
.overlay {
    background-image: linear-gradient(120deg,#3498db,#8e44ad);
    color: #fff;
    position: relative;
    left: -100%;
    height: 100%;
    width: 200%;
    transform: translateY(0);
    transition: transform .6s ease-in-out;
}
.overlay-panel {
    position: absolute;
    top: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0 40px;
    height: 100%;
    width: 50%;
    text-align: center;
    transform: translateY(0);
    transition: transform .6s ease-in-out;
}
.overlay-right {
    right: 0;
    transform: translateY(0);
    
}

.overlay-left {
    transform: translateY(-20%);
}

.container.right-panel-active .sign-in-container {
    transform: translateY(100%);
}

.container.container.right-panel-active .overlay-container {
    transform: translateX(-100%);
}
.container.right-panel-active .sign-up-container {
    transform: translateX(100%);
    opacity: 1;
    z-index: 5;
}
.container.container.right-panel-active .overlay {
    transform: translateX(50%);
}
.container.container.right-panel-active .overlay-left {
    transform: translateY(0);
}
.container.container.right-panel-active .overlay-right {
    transform: translateY(20%);
}

.bgbox {
  display: block;
  opacity: 0.9;
  z-index: -3;
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: opacity 1s,transform .25s,filter .25s;
  backface-visibility: hidden;
}
</style>
