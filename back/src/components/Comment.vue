<template>
  <div>
    <h3>评论列表</h3>

    <!-- 面包屑导航区 -->
    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>评论管理</el-breadcrumb-item>
      <el-breadcrumb-item>评论列表</el-breadcrumb-item>
    </el-breadcrumb>

    <!-- 卡片视图区 -->
    <el-card>
      <!-- 搜索与添加区域 -->
      <el-row :gutter="20">
        <el-col :span="8">
          <el-input
            placeholder="请输入内容"
            v-model="queryInfo.blog"
            clearable
            @clear="getCommentList"
          >
            <el-button
              slot="append"
              icon="el-icon-search"
              @click="getCommentList"
            ></el-button>
          </el-input>
        </el-col>
        <el-col :span="4">
          <el-button type="primary" @click="getCommentList()">
            刷新评论列表
          </el-button>
        </el-col>
      </el-row>

      <!-- 用户列表区域 -->
      <el-table :data="commentsInCurrentPage" border stripe>
        <!-- 表格的索引列 -->
        <el-table-column type="index"></el-table-column>
        <el-table-column label="用户名" prop="username"></el-table-column>
        <el-table-column label="评论时间" prop="time"></el-table-column>
        <el-table-column label="评论博客" prop="blog"></el-table-column>
        <el-table-column
          label="评论内容"
          prop="content"
          width="400px"
        ></el-table-column>
        <el-table-column
          label="点赞数量"
          prop="likes"
          width="100px"
        ></el-table-column>
        <!-- 使用作用域插槽将状态类渲染为开关 -->
        <el-table-column label="评论状态" width="80px">
          <template slot-scope="scope">
            <el-switch
              v-model="scope.row.visible"
              @change="changeCommentVisible(scope.row)"
            >
            </el-switch>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="70px">
          <template slot-scope="scope">
            <!-- 删除按钮 -->
            <el-button
              type="danger"
              icon="el-icon-delete"
              size="mini"
              @click="removeCommentById(scope.row.id)"
            ></el-button>
          </template>
        </el-table-column>
      </el-table>

      <!-- 分页区域 -->
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="pagination.currentpage"
        :page-sizes="[1, 2, 5, 10]"
        :page-size="pagination.pagesize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
      >
      </el-pagination>
    </el-card>
  </div>
</template>

<script>
export default {
  // 生命周期
  // 初始化
  created() {
    this.getCommentList()
  },

  data() {
    return {
      // 评论列表中评论的数量
      total: 5,

      // 评论列表
      commentList: [
        {
          id: 1,
          username: 'dcvx',
          time: '2021/1/11',
          blog: '技术文档写作',
          content:
            '我是来测试一下是不是能正常评论，能否在后台看到评论内容，好像真的可以看到唉~~~~~',
          likes: 11,
          visible: true,
        },
        {
          id: 2,
          username: '杰尼龟',
          time: '2021/1/12',
          blog: '技术文档写作',
          content: '杰尼杰尼',
          likes: 2,
          visible: true,
        },
        {
          id: 3,
          username: '阿灰',
          time: '2021/1/10',
          blog: '技术文档写作',
          content: '芜湖起飞',
          likes: 1222,
          visible: false,
        },
        {
          id: 4,
          username: '阿德',
          time: '2020/12/22',
          blog: '普通的博客',
          content: 'ashadkjfalksduibnotiahxbm,duaio woooooo~~`',
          likes: 1,
          visible: true,
        },
        {
          id: 5,
          username: '狗子',
          time: '2020/12/22',
          blog: '普通的博客',
          content: '狗子掉了',
          likes: 10,
          visible: false,
        },
      ],

      // 本页的评论
      commentsInCurrentPage: [],

      // 分页相关数据
      pagination: {
        // 当前页数
        currentpage: 1,
        // 当前每页显示多少条数据
        pagesize: 2,
      },

      // 获取评论列表的参数对象
      queryInfo: {
        // 查询的对象
        blog: '',
      },
    }
  },

  mounted() {
    this.showComments()
  },

  methods: {
    // 获取评论列表
    async getCommentList() {
      console.log(this.queryInfo)
      const { data: res } = await this.$http.get('comments', {
        params: this.queryInfo,
      })
      if (res.meta.status !== 200)
        return this.$message.error('获取用户列表失败！')
      this.commentList = res.data.comments
      this.total = res.data.total
      this.pagination.currentpage = 1
      this.showComments()
    },

    // 监听 page-size 改变
    handleSizeChange(newSize) {
      // console.log('newSize:' + newSize)
      this.pagination.pagesize = newSize
      this.showComments()
    },

    // 监听 current-page 改变
    handleCurrentChange(newPage) {
      // console.log('newPage:' + newPage)
      this.pagination.currentpage = newPage
      this.showComments()
    },

    // 根据 pagination 将 currentpage 对应的数据存入 commentsInCurrentPage
    showComments() {
      this.commentsInCurrentPage = []
      let startIndex =
        (this.pagination.currentpage - 1) * this.pagination.pagesize
      let endIndex = Math.min(
        this.pagination.currentpage * this.pagination.pagesize,
        this.commentList.length
      )
      // console.log('startIndex:' + startIndex)
      // console.log('endIndex:' + endIndex)
      for (let i = startIndex; i < endIndex; i++) {
        // console.log(this.commentList[i])
        this.commentsInCurrentPage.push(this.commentList[i])
      }
      // console.log(this.commentsInCurrentPage)
    },

    // 监听 switch 状态的改变
    async changeCommentVisible(comment) {
      // 构造传递参数
      let params = {}
      params.id = comment.id
      params.visible = comment.visible

      // 发起 API 请求
      const { data: res } = await this.$http.put('comments', params)
      // 请求失败
      if (res.meta.status !== 200) {
        comment.visible = !comment.visible
        this.$message.error('更新评论状态失败！')
      }
      // 请求成功
      else {
        this.$message.success('更新评论状态成功！')
      }
    },

    // 根据 id 删除对应的评论
    async removeCommentById(id) {
      // 弹框提问用户是否删除数据
      const confirmResult = await this.$confirm(
        '此操作将永久删除该评论, 是否继续?',
        '提示',
        {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning',
        }
      ).catch((err) => {
        return err
      })
      // 如果用户确认删除，则返回值为字符串 confirm
      // 如果用户取消删除，则返回值为字符串 cancel
      if (confirmResult !== 'confirm') {
        return this.$message.info('已取消删除')
      }

      // 构造传递参数
      let params = {}
      params.id = id
      // 发起 API 请求
      // 注意：post和put有三个参数，url,data和config，所以在使用这两个时，可以写成axios.post(api,{id:1}),axios.put(api,{id:1}),
      // 但是delete只有两个参数：url和config，data在config中，所以需要写成 axios.delete(api,{data:{id:1}})
      const { data: res } = await this.$http.delete('comments', {
        data: params,
      })
      // 请求失败
      if (res.meta.status !== 200) {
        this.$message.error('删除评论失败')
      }
      // 请求成功
      else {
        this.$message.success('删除评论成功')
        // 刷新用户列表数据
        this.getCommentList()
      }
    },
  },
}
</script>

<style lang="less" scoped>
el-table-column {
  text-align: center;
  justify-content: space-around; /*主轴居中*/
  align-items: center;
}
</style>