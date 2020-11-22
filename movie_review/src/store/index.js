import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies:[],
    loginStatus : false,
    movie_url:''
  },
  getters: {
  },
  mutations: {
    GET_MOVIES: function (state, movieData) {
      state.movies = movieData
    },
    LOGIN : function(state){
      state.loginStatus = !state.loginStatus
    },
    SEARCH_MV : function(state,title){
      axios.get()
    }
  },
  actions: {
    getMovies: function ({commit}) {
      axios.get('http://127.0.0.1:8000/movies/movie_list_create/')
        .then((res) => {
          const movieData = res.data
          console.log(movieData)
          commit('GET_MOVIES', movieData)
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    login : function({commit}){
      commit('LOGIN')
    },
    searchMV : function({commit},title){
      commit('SEARCH_MV',title)
    }
  },
})