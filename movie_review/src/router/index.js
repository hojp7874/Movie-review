import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '@/views/Main.vue'
import Home from '@/views/Home.vue'
import Login from '@/views/Login.vue'
import Signup from '@/views/Signup.vue'
import Allmovielist from '@/views/Allmovielist.vue'
import Likemovielist from '@/views/Likemovielist.vue'
import SearchedList from '@/views/SearchedList.vue'

Vue.use(VueRouter)

const routes = [

  {
    path : '/',
    name : 'Home',
    component : Home
  },
  {
    path : '/main',
    name : 'Main',
    component : Main
  },
  {
    path : '/login',
    name : 'Login',
    component : Login
  },
  {
    path : '/signup',
    name : 'Signup',
    component : Signup
  },
  {
    path : '/movielist',
    name : 'Allmovielist',
    component : Allmovielist
  },
  {
    path : '/likemovielist',
    name : 'Likemovielist',
    component : Likemovielist
  },
  {
    path : '/search',
    name : 'SearchedList',
    component : SearchedList
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
