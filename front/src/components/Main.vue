<template>
  <div :style="{ width: width + 'px' }" id="pageDiv">
    <h2>评论</h2>

    <!-- 登录前显示的界面 -->
    <el-card :style="{ display: loginDivDisplay }">
      <div style="text-align: center; font-size: 22px; margin-bottom: 10px">
        <p>登录后才可发表评论</p>
      </div>
      <!-- 登录表单区域 -->
      <div>
        <el-form
          ref="loginFormRef"
          :model="loginForm"
          :rules="loginFormRules"
          label-width="0px"
          class="login_form"
        >
          <el-row :gutter="20">
            <el-col :span="8">
              <!-- 用户名 -->
              <el-form-item prop="username">
                <el-input
                  v-model="loginForm.username"
                  prefix-icon="iconfont icon-user"
                ></el-input>
              </el-form-item>
            </el-col>

            <el-col :span="8">
              <!-- 密码 -->
              <el-form-item prop="password">
                <el-input
                  v-model="loginForm.password"
                  prefix-icon="iconfont icon-3702mima"
                  type="password"
                ></el-input>
              </el-form-item>
            </el-col>

            <el-col :span="8">
              <!-- 按钮区域 -->
              <el-form-item class="btns">
                <el-button type="primary" @click="login">登录</el-button>
                <el-button type="info" @click="signin">注册</el-button>
              </el-form-item>
            </el-col>
          </el-row>
          <el-row :gutter="20">
            <el-col :span="8">
              <!-- 博客用户名 -->
              <el-form-item prop="blogusername">
                <el-input
                  v-model="loginForm.blogusername"
                  prefix-icon="iconfont icon-user"
                ></el-input>
              </el-form-item>
            </el-col>

            <el-col :span="8">
              <!-- 博客名 -->
              <el-form-item prop="blogname">
                <el-input
                  v-model="loginForm.blogname"
                  prefix-icon="iconfont icon-danju"
                ></el-input>
              </el-form-item>
            </el-col>
          </el-row>
        </el-form>
      </div>
    </el-card>

    <!-- 登录后显示的界面 -->
    <el-card :style="{ display: commentDivDisplay }">
      <!-- 发表评论区域 -->
      <el-input
        type="textarea"
        placeholder="请输入内容"
        v-model="textarea"
        maxlength="200"
        show-word-limit
        :autosize="{ minRows: 4, maxRows: 6 }"
        id="commentInputArea"
      >
      </el-input>

      <el-row :gutter="20" style="margin-top: 10px">
        <el-col :span="8">
          <el-input
            v-model="loginForm.username"
            prefix-icon="iconfont icon-user"
            disabled
          ></el-input>
        </el-col>
        <el-col :span="8">
          <el-button type="info" @click="logout" id="logoutButton">
            退出登录
          </el-button>
        </el-col>
        <el-col :span="8">
          <el-button type="primary" @click="comment" id="commentButton">
            发表评论
          </el-button>
        </el-col>
      </el-row>
    </el-card>

    <!-- 评论列表 -->
    <div style="margin-top: 10px"></div>

    <el-card>
      <div v-for="comment in commentList" :key="comment.id">
        <p style="font-size: 22px; font-weight: bold">{{ comment.username }}</p>
        <p style="font-size: 12px; font-weight: 100; color: gray">
          {{ comment.time }}
        </p>
        <p style="font-size: 18px; padding-left: 5%; padding-right: 5%">
          {{ comment.content }}
        </p>
        <el-divider></el-divider>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  created() {
    window.addEventListener('resize', this.handleResize)
    this.getCommentList()
  },

  mounted() {
    this.width = document.documentElement.clientWidth * 0.9
  },

  beforeDestroy: function () {
    window.removeEventListener('resize', this.handleResize)
  },

  data() {
    return {
      // 查询的信息
      // queryInfo: {
      //   username: null,
      //   password: null,
      //   blogusername: null,
      //   blogname: null,
      // },

      // // 博客信息
      // blogInfo: {
      //   blogusername: null,
      //   blogname: null,
      // },

      // 页面div的width
      width: 1000,

      // 登录表单的数据绑定对象
      loginForm: {
        username: 'admin',
        password: '123456',
        blogusername: '',
        blogname: '',
      },

      // 表单的验证规则对象
      loginFormRules: {
        // 验证用户名是否合法
        username: [
          { required: true, message: '请输入登录名称', trigger: 'blur' },
          {
            min: 3,
            max: 20,
            message: '用户名长度在 3 到 20 个字符',
            trigger: 'blur',
          },
        ],
        // 验证密码是否合法
        password: [
          { required: true, message: '请输入登录密码', trigger: 'blur' },
          {
            min: 6,
            max: 30,
            message: '密码长度在 6 到 30 个字符',
            trigger: 'blur',
          },
        ],
      },

      // 登录部分的 display 属性
      loginDivDisplay: 'block',

      // 评论部分的 display 属性
      commentDivDisplay: 'none',

      // 评论输入区域
      textarea: '',

      // 评论列表
      commentList: [
        { username: 'dcvx1', time: '2012/1/1', content: 'haha' },
        {
          username: 'dcvx2',
          time: '2012/1/2',
          content: 'hahadsfasdfasdfasdfa',
        },
        {
          username: 'dcvx3',
          time: '2012/1/3',
          content:
            'haasdfasdfas手动阀阿斯顿发射点发生发撒打发撒旦i企鹅喷雾区位u日期哦i为肉i完全日哦请问u人哦物品手动阀手动阀十分ha',
        },
      ],
    }
  },

  methods: {
    // 根据修改窗口大小的事件修改页面宽度
    handleResize(event) {
      this.width = document.documentElement.clientWidth * 0.9
      //   console.log(document.documentElement.clientWidth)
    },

    // 登录
    login() {
      this.$refs.loginFormRef.validate(async (valid) => {
        // 前端验证输入数据的合法性
        if (!valid) {
          return
        }
        // 向 API 发起请求
        console.log(this.loginForm)
        const { data: res } = await this.$http.post('login_front', this.loginForm)
        // 根据请求结果进行处理
        if (res.meta.status !== 200) {
          this.$message.error('登录失败！')
        } else {
          window.sessionStorage.setItem('token', res.data.token)
          window.sessionStorage.setItem('username', res.data.username)
          // 登录后隐藏login界面并显示comment界面
          this.loginDivDisplay = 'none'
          this.commentDivDisplay = 'block'
          this.getCommentList()
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
        const { data: res } = await this.$http.post('signin_front', this.loginForm)
        // 根据请求结果进行处理
        if (res.meta.status !== 200) {
          this.$message.error('注册博客失败，两个用户名需要相同！')
        } else {
          window.sessionStorage.setItem('token', res.data.token)
          window.sessionStorage.setItem('username', res.data.username)
          // 注册后隐藏login界面并显示comment界面
          this.loginDivDisplay = 'none'
          this.commentDivDisplay = 'block'
          this.getCommentList()
        }
      })
    },

    // 退出登录
    logout() {
      window.sessionStorage.clear()
      // 退出登录后隐藏comment界面并显示login界面
      this.loginDivDisplay = 'block'
      this.commentDivDisplay = 'none'
    },

    // 获取评论列表
    async getCommentList() {
      console.log(this.loginForm)
      const { data: res } = await this.$http.get('comments1', {
        params: this.loginForm,
      })
      if (res.meta.status !== 200)
        return this.$message.error('获取评论列表失败！')
      this.commentList = res.data.comments
    },

    // 发布评论
    async comment() {
      let params = this.loginForm
      params.comment = this.textarea
      const { data: res } = await this.$http.put('comments1', params)
      if (res.meta.status !== 200) return this.$message.error('发送评论失败！')
      this.getCommentList()
    },
  },
}
</script>

<style>
#pageDiv {
  margin-left: 5%;
}

#commentButton {
  float: right;
}
</style>