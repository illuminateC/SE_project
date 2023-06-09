<template>

    <div id="register" class="register">
      <img class="bgbox" id="bgbox" alt="" src="../../src/assets/ys2.png">
      <div class="wrap">
        <h1>注 册</h1>
        <el-form :model="form" ref="form" class="form">
          <el-form-item prop="username">
            <el-tooltip effect="dark" content="请输入长度小于16位的用户名" placement="bottom" >
              <el-input placeholder="用户名" type="text" v-model="form.username" autocomplete="off" maxlength="16" show-word-limit></el-input>
            </el-tooltip>
          </el-form-item>
          <el-form-item id="password" prop="password">
            <el-tooltip effect="dark" content="请保证密码长度在6-16之间，且包含数字和大小写字母" placement="bottom" >
              <el-input
              placeholder="密码"
              show-password
              type="password"
              v-model="form.password"
              autocomplete="off"
              ></el-input>
            </el-tooltip>
          </el-form-item>
          <el-form-item id="confirmPassword" prop="confirmPassword">
            <el-input
              placeholder="确认密码"
              show-password
              type="password"
              v-model="form.confirmPassword"
              autocomplete="off"
              :disabled="!(/^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,16}$/.test(form.password))"
            ></el-input>
          </el-form-item>
          <el-form-item class="btn_register">
            <el-button type="primary" @click="register">注&nbsp;&nbsp;册</el-button>
          </el-form-item>
        </el-form>
        <div class="suffix">
          <div class="login" @click="toLogin">点我登录</div><span id="hava">已有账号？</span>
        </div>
      </div>
    </div>    
</template>
  
  <script>
  import qs from "qs";
  export default {
    name: "NewRegister",
    data() {
      return {
        form: {
          username: '',
          password: '',
          confirmPassword: ''
        }
      }
    },
    methods: {
      register: function () {
        // 检查表单是否有填写内容
        if (this.form.username === '' || this.form.password === '' || this.form.confirmPassword === '') {
          this.$message.warning("请填写完整的注册信息！");
          return;
        }
  
        if (this.form.password !== this.form.confirmPassword) {
          this.$message.warning("两次输入的密码不一致！");
          return;
        }
        
        let passwordReg = /^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,16}$/;
          if (!passwordReg.test(this.form.password)) {
            this.$message.warning("密码必须为6到16位数字和英文的组合！");
            return;
          }

        this.$axios({
          method: 'post',
          url: '/user/register',
          data: qs.stringify({
            username: this.form.username,
            password: this.form.password
          })
        })
        .then(res => {
          switch (res.data.status_code) {
            case 200:
              this.$message.success("注册成功！");
              this.$router.push('/login');
              break;
            case 401:
              this.$message.error("用户名已存在！");
              break;
            default:
              this.$message.error("注册失败，请重试！");
          }
        })
        .catch(err => {
          console.log(err);
        })
      },
      toLogin: function () {
        // 跳转登录的路由
        this.$router.push('/login');
      }
    }
  }
  </script>
  
  <style scoped>
  #register {
    font-family: 'Noto Serif SC', serif;
    margin-top: 60px;
  }
  #register >>> .el-input__inner {
    font-family: 'Noto Serif SC', serif;
  }
  #register .bgbox {
    display: block;
    opacity: 0.7;
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
  #register .wrap {
    width: 300px;
    height: 375px;
    padding: 0 25px 0 25px;
    line-height: 40px;
    position: relative;
    display: inline-block;
    background-color: rgba(255, 255, 255, 0.85);
    border-radius: 20px;
  }
  #register .btn_register {
    margin-top: 25px;
    text-align: center;
  }
  #register .btn_register button{
    line-height: 10px;
    font-family: 'Noto Serif SC', serif;
    width: 100%;
    height: 38px;
  }
  #register .suffix .login {
    display: inline;
    margin-left: 5px;
    font-size: 14px;
    line-height: 10px;
    color: #999;
    cursor: pointer;
    float:right;
  }
  #register .suffix span{
    display: inline;
    margin: 0;
    padding: 0;
    font-size:12px;
    line-height:8px;
    color:#999;
    float:right;
  }
  </style>