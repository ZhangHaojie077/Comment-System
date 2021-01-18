<template>
  <div>
    <h2>您好，欢迎使用云评论系统后台管理程序！~</h2>

    <div class="block" style="margin-top: 30px">
      <el-carousel height="500px">
        <el-carousel-item v-for="item in carousel" :key="item">
          <img :src="item" alt="" style="width: 100%" />
        </el-carousel-item>
      </el-carousel>
    </div>
  </div>
</template>

<script>
export default {
  mounted() {
    this.getImagesPath()
  },

  data() {
    return {
      publicPath: process.env.BASE_URL,
      carousel: [
        'assets/images/carousel-1.jpg',
        'assets/images/carousel-2.jpg',
        'assets/images/carousel-3.jpg',
        'assets/images/carousel-4.jpg',
      ],
    }
  },

  methods: {
    // 获取图片的路径，路径必须动态获取，否则开发环境没问题了，但打包报错
    getImagesPath() {
      for (let item in this.carousel) {
        item = this.publicPath + item
      }
    },
  },
}
</script>

<style lang="less" scoped>
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 150px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>