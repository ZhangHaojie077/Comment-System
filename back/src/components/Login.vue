<template>
  <div class="login_container">
    <div class="login_box">
      <!-- 头像区域 -->
      <div class="avator_box">
        <img src="../../src/assets/logo.png" alt="" />
      </div>
      <!-- 登录表单区域 -->
      <el-form
        ref="loginFormRef"
        :model="loginForm"
        :rules="loginFormRules"
        label-width="0px"
        class="login_form"
      >
        <!-- 用户名 -->
        <el-form-item prop="username">
          <el-input
            v-model="loginForm.username"
            prefix-icon="iconfont icon-user"
          ></el-input>
        </el-form-item>
        <!-- 密码 -->
        <el-form-item prop="password">
          <el-input
            v-model="loginForm.password"
            prefix-icon="iconfont icon-3702mima"
            type="password"
          ></el-input>
        </el-form-item>
        <!-- 按钮区域 -->
        <el-form-item class="btns">
          <el-button type="primary" @click="login">登录</el-button>
          <el-button type="info" @click="signin">注册</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {

      // 登录表单的数据绑定对象
      loginForm: {
        username: 'admin',
        password: '123456',
      },

      // 表单的验证规则对象
      loginFormRules: {
        // 验证用户名是否合法
        username: [
          { required: true, message: '请输入登录名称', trigger: 'blur' },
          {
            min: 3,
            max: 20,
            message: '长度在 3 到 20 个字符',
            trigger: 'blur',
          },
        ],
        // 验证密码是否合法
        password: [
          { required: true, message: '请输入登录密码', trigger: 'blur' },
          {
            min: 6,
            max: 30,
            message: '长度在 6 到 30 个字符',
            trigger: 'blur',
          },
        ],
      },
    }
  },

  methods: {
    // login() {
    //   window.sessionStorage.setItem('token', '123')
    //   this.$router.push('/home')
    // },

    // signin() {
    //   window.sessionStorage.setItem('token', '123')
    //   this.$router.push('/home')
    // },

    // 登录
    login() {
      this.$refs.loginFormRef.validate(async (valid) => {
        // 前端验证输入数据的合法性
        if (!valid) {
          return
        }
        // 向 API 发起请求
        const { data: res } = await this.$http.post('login', this.loginForm)
        // 根据请求结果进行处理
        if (res.meta.status !== 200) {
          this.$message.error('登录失败！')
        } else {
          this.$message.success('登录成功！')
          // 1. 将登录成功之后的 token 保存客户端的 sessionStorage 中
          //  1.1 项目中除了登陆之外的其他API接口必须在登录后才能访问
          //  1.2 token 只应当在当前网站打开期间生效，所以将 token 保存在 sessionStorage 中而非 localStorage 中
          window.sessionStorage.setItem('token', res.data.token)
          window.sessionStorage.setItem('username', res.data.username)
          // 2. 通过编程式导航跳转到后台主页，路由地址是 /home
          this.$router.push('/home')
        }
      })
    },

    // 注册
    signin() {
      this.$refs.loginFormRef.validate(async (valid) => {
        // 前端验证输入数据的合法性
        if (!valid) {
          return
        }
        // 向 API 发起请求
        const { data: res } = await this.$http.post('signin', this.loginForm)
        // 根据请求结果进行处理
        if (res.meta.status !== 200) {
          this.$message.error('注册失败！')
        } else {
          this.$message.success('注册成功！')
          window.sessionStorage.setItem('token', res.data.token)
          window.sessionStorage.setItem('username', res.data.username)
          this.$router.push('/home')
        }
      })
    },
  },
}
</script>

<style lang="less" scoped>
.login_container {
  background-color: #2b4b6b;
  height: 100%;
}

.login_box {
  width: 450px;
  height: 300px;
  background-color: #fff;
  border-radius: 3px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.avator_box {
  height: 130px;
  width: 130px;
  border: 1px solid #eeeeee;
  border-radius: 50%;
  padding: 10px;
  box-shadow: 0 0 10px #dddddd;
  position: absolute;
  left: 50%;
  background-color: #fff;
  transform: translate(-50%, -50%);
  img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background-color: #eeeeee;
  }
}

.login_form {
  position: absolute;
  bottom: 0;
  width: 100%;
  padding: 0 20px;
  box-sizing: border-box;
}

.btns {
  display: flex;
  justify-content: flex-end;
}
</style>
