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
    crewsNm: [],
    genres : [],
    nations :[],
    genresState :[],
    filterdMovie:[],
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
      state.genres = Array.from(new Set(movieData.map(a=>a.repGenreNm)))
      state.genresState = new Array(state.genres.length)
      state.nations = Array.from(new Set(movieData.map(a=>a.repNationNm)))
    },
    LOGOUT : function(state){
      localStorage.removeItem('jwt')
      state.loginStatus=false
    },
    GET_MOVIE_CREW : function(state, movieCrew){
      state.crewsNm = movieCrew.map(a=>a.name)
      state.crew = movieCrew
    },
    GET_USERS : function(state,data){
      state.users = data
    },
    SEARCH: function (state, searchWord) {
      state.search = state.movies.filter(function (data) {
        return data.movieNm.includes(searchWord)
      })
      state.movies.filter(function (data) {
        for (let index = 0; index < data.peoples.length; index++) {
          if (data.peoples[index].name.includes(searchWord)) {
            return state.search.push(data)
          }
        }
      })
      state.search = Array.from(new Set(state.search))
    },
    LOGIN : function(state){
      state.loginStatus = true
    },
    STATE_CHANGE : function(state,idx){
      state.genresState[idx] = !state.genresState[idx]
      const list =[]
      for(var i =0; i <state.genresState.length; i++){
        if(state.genresState[i]){
          list.push(state.genres[i])
        }
      }
      const filtered = state.movies.filter((movie)=>{
        return list.includes(movie.repGenreNm) 
      })
      state.filterdMovie = filtered
    }
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
    },
    login : function({commit}){
      commit('LOGIN')
    },
    stateChange : function({commit},idx){
      commit('STATE_CHANGE',idx)
    }
  },
})