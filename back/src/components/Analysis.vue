<template>
  <div>
    <h3>评论分析</h3>

    <!-- 面包屑导航区 -->
    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>评论分析</el-breadcrumb-item>
      <el-breadcrumb-item>评论分析</el-breadcrumb-item>
    </el-breadcrumb>

    <!-- 卡片视图区 -->
    <el-card style="margin-bottom: 10px">
      <div ref="chart2" style="width: 100%; height: 376px"></div>
    </el-card>
    <el-card style="margin-bottom: 10px">
      <div ref="chart1" style="width: 100%; height: 376px"></div>
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
      // 图表 1 的 option
      optionEChart1: {
        //标题
        title: {
          text: '评论雷达图',
          textStyle: {
            fontSize: 23,
          },
        },
        tooltip: {},
        legend: {
          data: ['我的评论', '所有评论'],
        },
        radar: {
          // shape: 'circle',
          name: {
            textStyle: {
              color: '#fff',
              backgroundColor: '#999',
              borderRadius: 3,
              padding: [3, 5],
            },
          },
          indicator: [
            { name: '总评论数量' },
            { name: '总评论用户数量' },
            { name: '平均评论数量' },
            { name: '平均评论用户数量' },
            { name: '平均评论长度' },
          ],
        },
        series: [
          {
            name: '评论雷达图',
            type: 'radar',
            areaStyle: { normal: {} },
            data: [
              {
                value: [15000, 8000, 200, 18, 11],
                name: '所有评论',
              },
              {
                value: [3000, 1400, 180, 150, 25, 23],
                name: '我的评论',
              },
            ],
          },
        ],
      },

      // 图表 2 的 option
      optionEChart2: {
        title: {
          text: '评论热词云图',
          // x: 'center',
          textStyle: {
            fontSize: 23,
          },
        },
        backgroundColor: '#fff',
        tooltip: {
          show: false,
        },
        series: [
          {
            type: 'wordCloud',
            name: '评论热词分析',
            //用来调整词之间的距离
            gridSize: 5,
            //用来调整字的大小范围
            sizeRange: [12, 60],
            //用来调整词的旋转方向，，[0,0]--代表着没有角度，也就是词为水平方向
            rotationRange: [0, 0],
            //随机生成字体颜色
            textStyle: {
              normal: {
                color: function () {
                  return (
                    'rgb(' +
                    Math.round(Math.random() * 255) +
                    ', ' +
                    Math.round(Math.random() * 255) +
                    ', ' +
                    Math.round(Math.random() * 255) +
                    ')'
                  )
                },
              },
            },
            //位置相关设置
            left: 'center',
            top: 'center',
            right: null,
            bottom: null,
            width: '200%',
            height: '200%',
            //数据
            data: [
              { name: '这篇', value: 15000 },
              { name: '好', value: 10081 },
              { name: '不错', value: 9386 },
              { name: '一般', value: 7500 },
              { name: '就那样吧', value: 7500 },
              { name: '真不错', value: 6500 },
              { name: '踩', value: 6500 },
              { name: '赞', value: 6000 },
              { name: '文章', value: 4500 },
              { name: '技术', value: 3800 },
              { name: '太', value: 3000 },
              { name: '棒了', value: 2500 },
              //{ name: '领土完整', value: 2300 },
              //{ name: '安全', value: 2000 },
              //{ name: '从严治党', value: 1900 },
              //{ name: '现代化经济体系', value: 1800 },
              //{ name: '国防动员', value: 1700 },
              //{ name: '信息化战争', value: 1600 },
              //{ name: '局部战争', value: 1500 },
              //{ name: '教育', value: 1200 },
              //{ name: '职业教育', value: 1100 },
              //{ name: '兵法', value: 900 },
              //{ name: '一国两制', value: 800 },
              //{ name: '特色社会主义思想', value: 700 },
            ],
          },
        ],
      },
    }
  },

  methods: {
    // 获取图标数据
    getEchartData() {
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