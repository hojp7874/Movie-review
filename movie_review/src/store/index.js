import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'



Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies:[],
    loginStatus : false,
    score:[],
    crew:[],
    users:[],

  },
  getters: {
    movieList:function(){
      return this.state.movies.forEach((obj)=>{
        return obj.movieNm
      })
    }
  },
  mutations: {
    GET_MOVIES: function (state, movieData) {
      state.movies = movieData
    },
    LOGIN : function(state){
      state.loginStatus = !state.loginStatus
    },
    LOGOUT : function(state){
      localStorage.removeItem('jwt')
      state.loginStatus = !state.loginStatus
      this.$router.go({name: 'Home'})      
    },
    GET_MOVIE_SCORE : function(state,movieScore){
      state.score = movieScore
    },
    GET_MOVIE_CREW : function(state, movieCrew){
      state.crew = movieCrew
    },
    GET_USERS : function(state,data){
      state.users = data
    },
    // GET_REVIEW : function(state,movieReview){
    //   state.reviews = movieReview
    // },

  },
  actions: {
    getMovies: function ({commit}) {
      axios.get('http://127.0.0.1:8000/movies/movie_list_create/')
        .then((res) => {
          const movieData = res.data
          commit('GET_MOVIES', movieData)
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    login : function({commit}){
      commit('LOGIN')
    },
    logout:function({commit}){
      commit('LOGOUT')
    },
    getMovieScore :function({commit}){
      axios.get('http://127.0.0.1:8000/movies/movie_score_list_create/')
        .then((res) => {
          const movieScore = res.data
          commit('GET_MOVIE_SCORE', movieScore)
        })
        .catch((err)=>{
          console.log(err)
        })      
    },
    getMovieCrew :function({commit}){
      axios.get('http://127.0.0.1:8000/movies/people_list/')
        .then((res) => {
          const movieCrew = res.data
          commit('GET_MOVIE_CREW', movieCrew)
        })
        .catch((err)=>{
          console.log(err)
        })      
      },
      getUser:function({commit}){
        axios.get('http://127.0.0.1:8000/accounts/get-users/')
          .then((res) => {
            const users = res.data
            commit('GET_USERS', users)
          })
          .catch((err)=>{
            console.log(err)
          })      
    },
  },
})