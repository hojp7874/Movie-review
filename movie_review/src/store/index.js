import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies:[],
    crew:[],
    users:[],
    loginStatus : false,
    search:[],
    moviesNm: [],

  },
  getters: {
    movieList:function(){
      return this.state.movies.map(a=>a.movieNm)
      }
  },
  mutations: {
    GET_MOVIES: function (state, movieData) {
      state.movies = movieData
      state.search = movieData
      state.moviesNm = movieData.map(a=>a.movieNm)
      console.log(state.moviesNm)
    },
    LOGOUT : function(state){
      localStorage.removeItem('jwt')
      state.loginStatus=false
    },
    GET_MOVIE_CREW : function(state, movieCrew){
      state.crew = movieCrew
    },
    GET_USERS : function(state,data){
      state.users = data
    },
    SEARCH: function (state, searchWord) {
      state.search = state.movies.filter(function (data) {
        return data.movieNm.includes(searchWord)
      })
      console.log(state.search)
    }
    // GET_REVIEW : function(state,movieReview){
    //   state.reviews = movieReview
    // },

  },
  actions: {
    getMovies: function ({commit}) {
      axios.get(`${SERVER_URL}/movies/movie_list_create/`)
        .then((res) => {
          const movieData = res.data
          commit('GET_MOVIES', movieData)
        })
        .catch((err)=>{
          console.log(err)
        })
    },

    logout:function({commit}){
      commit('LOGOUT')
    },
    getMovieCrew :function({commit}){
      axios.get(`${SERVER_URL}/movies/people_list/`)
        .then((res) => {
          const movieCrew = res.data
          commit('GET_MOVIE_CREW', movieCrew)
        })
        .catch((err)=>{
          console.log(err)
        })      
    },
    getUser:function({commit}){
      axios.get(`${SERVER_URL}/accounts/get-users/`)
        .then((res) => {
          const users = res.data
          commit('GET_USERS', users)
        })
        .catch((err)=>{
          console.log(err)
        })      
    },
    search: function ({commit}, searchWord) {
      commit('SEARCH', searchWord)
    }
  },
})