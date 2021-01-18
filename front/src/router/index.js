import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import Home from '../components/Home.vue'
import Welcome from '../components/Welcome.vue'
import Comment from '../components/Comment.vue'
import Statistic from '../components/Statistic.vue'
import Analysis from '../components/Analysis.vue'
import Main from '../components/Main.vue'

// ����ȫ����ʽ��
import '../assets/css/global.css'
// ��������ͼ��
import '../assets/fonts/iconfont.css'

import axios from 'axios'
// ��������ĸ�·��
axios.defaults.baseURL = 'http://127.0.0.1:5000'
axios.interceptors.request.use(config => {
  // console.log(config)
  config.headers.Authorization = window.sessionStorage.getItem('token')
  config.headers.Username = window.sessionStorage.getItem('username')
  // �������뷵�� config
  return config
})
Vue.prototype.$http = axios

import * as echarts from 'echarts' //����echarts
Vue.prototype.$echarts = echarts //�������

Vue.use(VueRouter)

const routes = [{
    path: '/',
    redirect: '/main'
  },
  {
    path: '/main',
    component: Main
  }
]

const router = new VueRouter({
  routes
})

// ����·�ɵ�������
// router.beforeEach((to, from, next) => {
//   // to ��Ҫ���ʵ�·��
//   // from ���ĸ�·����ת����
//   // next ���к�����next() ��ʾ���У�next('/login') ��ʾǿ����ת
//   if (to.path === '/login') return next()
//   // ��ȡ token
//   const tokenStr = window.sessionStorage.getItem("token")
//   if (!tokenStr) return next('/login')
//   next()
// })

export default router
