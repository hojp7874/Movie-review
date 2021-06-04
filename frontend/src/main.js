import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Carousel3d from 'vue-carousel-3d';
import VueJwtDecode from 'vue-jwt-decode'
import Vuex from 'vuex'


Vue.use(Vuex)
Vue.use(BootstrapVue)
Vue.use(Carousel3d)
Vue.use(BootstrapVueIcons)
Vue.use(VueJwtDecode)

Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
