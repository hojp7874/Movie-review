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
    recommend: [],
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
      for (let index = 0; index < movieData.length; index++) {
        // console.log(movieData[index].popularity)
        // console.log(movieData[index].popularity.slice(-2, ))
        if (movieData[index].popularity != null) {
          if (movieData[index].popularity.slice(-2, ) == '만명' && movieData[index].popularity.slice(0, -2) > 10) {
            state.recommend.push(movieData[index])
          } else if (movieData[index].reviews) {
            state.recommend.push(movieData[index])
          }
        }
      }
      // object를 키 이름으로 정렬하여 반환
      // state.recommend = function sortObject(o)
      // {
      //   var sorted = {},
      //   key, a = [];
      //   // 키이름을 추출하여 배열에 집어넣음
      //   for (key in o) {
      //       if (o.hasOwnProperty(key)) a.push(key);
      //   }
      //   // 키이름 배열을 정렬
      //   a.sort();
      //   // 정렬된 키이름 배열을 이용하여 object 재구성
      //   for (key=0; key<a.length; key++) {
      //       sorted[a[key]] = o[a[key]];
      //   }
      //   return sorted;
      // }
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
      if (filtered[1] == null) {
        state.filterdMovie = state.movies
      }
      // if (state.genresState == []) {

      // }
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