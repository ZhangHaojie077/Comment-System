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
    <el-card style="margin-bottom: 10px">
      <div ref="chart1" style="width: 100%; height: 376px"></div>
    </el-card>
    <el-card style="margin-bottom: 10px">
      <div ref="chart2" style="width: 100%; height: 376px"></div>
    </el-card>
  </div>
</template>

<script>
export default {
  mounted() {
    this.getEchartData()
  },

  data() {
    return {
      // 图表 1 的option
      optionEChart1: {
        title: { text: '近期评论数量' },
        tooltip: {},
        legend: { data: ['评论数量'] },
        xAxis: {
          name: '时间',
          type: 'category',
          data: ['1-1', '1-2', '1-3', '1-4', '1-5', '1-6'],
        },
        yAxis: { name: '评论数量', type: 'value' },
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
      },

      // 图表 2 的option
      optionEChart2: {
        title: { text: '近期发布博客的评论数量' },
        tooltip: {},
        legend: { data: ['评论数量'] },
        xAxis: {
          name: '博客',
          type: 'category',
          data: ['博客1', '博客2', '博客3', '博客4', '博客5', '博客6'],
        },
        yAxis: { name: '评论数量', type: 'value' },
        series: [
          {
            name: '评论数量',
            type: 'bar',
            data: [5, 18, 36, 10, 27, 20],
          },
        ],
      },
    }
  },

  methods: {
    // 获取图标数据
    async getEchartData() {
      const { data: res } = await this.$http.get('statistic')
      if (res.meta.status !== 200) {
        this.$message.error('刷新数据失败！')
      } else {
        this.$message.success('刷新数据成功！')
        this.optionEChart1.xAxis.data = res.data.xAxisData1
        this.optionEChart1.series[0].data = res.data.seriesData1
        this.optionEChart2.xAxis.data = res.data.xAxisData2
        this.optionEChart2.series[0].data = res.data.seriesData2
      }
      let chart = null

      chart = this.$refs.chart1
      if (chart) {
        let myChart = this.$echarts.init(chart)
        // 绘制图表
        myChart.setOption(this.optionEChart1)
      }

      chart = this.$refs.chart2
      if (chart) {
        let myChart = this.$echarts.init(chart)
        // 绘制图表
        myChart.setOption(this.optionEChart2)
      }
    },
  },
}
</script>

<style lang="less" scoped>
</style>