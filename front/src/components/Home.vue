<template>
  <!-- 布局容器 -->
  <el-container class="home-container">
    <!-- 头部区域 -->
    <el-header>
      <div>
        <img src="../assets/heima.png" alt="" />
        <span>云评论后台管理系统</span>
      </div>
      <el-button type="info" @click="logout">退出</el-button>
    </el-header>

    <!-- 主体区域 -->
    <el-container>
      <!-- 左侧边栏 -->
      <el-aside :width="isCollapese ? '64px' : '200px'">
        <!-- 折叠按钮 -->
        <div class="toggle-button" @click="toggleCollapse">|||</div>

        <!-- 侧边栏菜单区域 -->
        <el-menu
          background-color="#333744"
          text-color="#fff"
          active-text-color="#409eff"
          :unique-opened="true"
          :collapse="isCollapese"
          :collapse-transition="false"
          :router="true"
          :default-active="activePath"
        >
          <el-submenu
            :index="item.id + ''"
            v-for="item in menulist"
            :key="item.id"
          >
            <!-- 一级菜单模板区域 -->
            <template slot="title">
              <!-- 图标 -->
              <i :class="item.iconfont"></i>
              <!-- 文本 -->
              <span>{{ item.authName }}</span>
            </template>

            <!-- 二级菜单 -->
            <el-menu-item
              :index="'/' + subItem.path"
              v-for="subItem in item.children"
              :key="subItem.id"
              @click="saveNavState('/' + subItem.path)"
            >
              <!-- 图标 -->
              <i class="el-icon-menu"></i>
              <!-- 文本 -->
              <span>{{ subItem.authName }}</span>
            </el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>

      <!-- 右侧主体 -->
      <el-main>
        <!-- 路由占位符 -->
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  created() {
    this.getMenuList()
    this.activePath = window.sessionStorage.getItem('activePath')
  },

  data() {
    return {
      // 左侧菜单数据
      menulist: [
        {
          id: 100,
          authName: '评论管理',
          iconfont: 'iconfont icon-user',
          path: 'comment',
          children: [
            {
              id: 101,
              authName: '评论列表',
              iconfont: 'iconfont icon-tijikongjian',
              path: 'comment',
              children: [],
            },
          ],
        },
        {
          id: 110,
          authName: '评论统计',
          iconfont: 'iconfont icon-baobiao',
          path: '',
          children: [
            {
              id: 111,
              authName: '评论统计',
              iconfont: 'iconfont icon-tijikongjian',
              path: 'statistic',
              children: [],
            },
            {
              id: 112,
              authName: '评论分析',
              iconfont: 'iconfont icon-tijikongjian',
              path: 'analysis',
              children: [],
            },
          ],
        },
        {
          id: 120,
          authName: '评论分析',
          iconfont: 'iconfont icon-danju',
          path: '',
          children: [
            {
              id: 121,
              authName: '评论统计',
              iconfont: 'iconfont icon-tijikongjian',
              path: 'statistic',
              children: [],
            },
            {
              id: 122,
              authName: '评论分析',
              iconfont: 'iconfont icon-tijikongjian',
              path: 'analysis',
              children: [],
            },
          ],
        },
        {
          id: 130,
          authName: '分类管理',
          iconfont: 'iconfont icon-tijikongjian',
          path: 'comments',
          children: [
            {
              id: 131,
              authName: '分类管理',
              iconfont: 'iconfont icon-tijikongjian',
              path: 'comments',
              children: [],
            },
          ],
        },
      ],

      // 是否折叠
      isCollapese: false,

      // 被激活的链接地址
      activePath: '',
    }
  },

  methods: {
    logout() {
      window.sessionStorage.clear()
      this.$router.push('/login')
    },

    // 获取菜单
    async getMenuList() {
      // const { data: res } = await this.$http.get('menus')
      // if (res.meta.status !== 200) return this.$message.error(res.meta.msg)
      // this.menulist = res.data
      // console.log(res)
    },

    // 点击按钮，切换菜单的折叠与展开
    toggleCollapse() {
      this.isCollapese = !this.isCollapese
    },

    // 保存链接的激活状态，即当前所在的路由
    saveNavState(activePath) {
      window.sessionStorage.setItem('activePath', activePath)
      this.activePath = activePath
    },
  },
}
</script>

<style lang="less" scoped>
.home-container {
  height: 100%;
}

.el-header {
  background-color: #373d41;
  display: flex;
  justify-content: space-between;
  padding-left: 0;
  align-items: center;
  color: #fff;
  font-size: 20px;
  > div {
    display: flex;
    align-items: center;
    span {
      margin-left: 15px;
    }
  }
}

.el-aside {
  background-color: #333744;
  .el-menu {
    border-right: none;
  }
}

.el-main {
  background-color: #eaedf1;
}

.iconfont {
  margin-right: 10px;
}

.toggle-button {
  background-color: #4a5064;
  font-size: 10px;
  line-height: 24px;
  color: #fff;
  text-align: center;
  letter-spacing: 0.2em;
  cursor: pointer;
}
</style>