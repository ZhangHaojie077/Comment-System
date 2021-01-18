<template>
  <div>
    <h3>评论统计</h3>

    <!-- 面包屑导航区 -->
    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>评论统计</el-breadcrumb-item>
      <el-breadcrumb-item>评论统计</el-breadcrumb-item>
    </el-breadcrumb>

    <!-- 卡片视图区 -->
    <el-card>
      <div ref="chart" style="width: 100%; height: 376px"></div>
    </el-card>
  </div>
</template>

<script>
export default {
  mounted() {
    this.getEchartData()
  },

  data() {
    return {}
  },

  methods: {
    // 获取评论列表
    async getCommentList() {
      const { data: res } = await this.$http.get('comments', {
        params: this.queryInfo,
      })
      // console.log(res)
      if (res.meta.status !== 200)
        return this.$message.error('获取用户列表失败！')
      this.commentList = res.data.users
      this.total = res.data.total
    },

    // 获取图标数据
    getEchartData() {
      const chart = this.$refs.chart
      if (chart) {
        const myChart = this.$echarts.init(chart)
        // 绘制图表
        myChart.setOption({
          title: { text: '近期评论数量' },
          tooltip: {},
          legend: {
            data: ['评论数量'],
          },
          xAxis: {
            name: '时间',
            type: 'category',
            data: ['1-1', '1-2', '1-3', '1-4', '1-5', '1-6'],
          },
          yAxis: {
            name: '评论数量',
            type: 'value',
          },
          series: [
            {
              name: '评论数量',
              type: 'line',
              areaStyle: {
                normal: {
                  // 线性渐变，前四个参数分别是 x0, y0, x2, y2, 范围从 0 - 1，相当于在图形包围盒中的百分比，如果 globalCoord 为 `true`，则该四个值是绝对的像素位置
                  color: {
                    type: 'linear',
                    x: 0,
                    y: 0,
                    x2: 0,
                    y2: 1,
                    colorStops: [
                      {
                        offset: 0,
                        color: 'red', // 0% 处的颜色
                      },
                      {
                        offset: 1,
                        color: 'blue', // 100% 处的颜色
                      },
                    ],
                    global: false, // 缺省为 false
                  },
                },
              },
              data: [5, 18, 36, 10, 27, 20],
            },
          ],
        })
      }
    },
  },
}
</script>

<style lang="less" scoped>
</style>