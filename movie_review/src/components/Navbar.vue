<template>
  <div id="navbar">
    <b-navbar toggleable="lg">
      <b-navbar-brand @click="toMain" href="#"><span id='ant'>늑대와 개미핥기</span></b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item><router-link class="whitefont" :to="{ name: 'Allmovielist' }">영화 목록</router-link></b-nav-item>
          <b-nav-item><router-link @click='requireLogin' class="whitefont" :to="{ name: 'Likemovielist' }">평가한 영화</router-link></b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
              <!-- :data="moviesNm" -->
            <vue-bootstrap-typeahead
              :data="searchNm"
              v-model="searchWord"
              size="sm"
              class="mr-sm-2"
              placeholder="검색어를 입력하세요"
              @keypress.enter="search"
            />
              <!-- <ul v-show="searchWord.length">
                <li v-for="(wd,idx) in candidate" :key='idx'></li>
              </ul> -->
            <b-button size="sm" class="my-2 my-sm-0" @click="search">🔍</b-button>
          </b-nav-form>

          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template #button-content>
              <em class="whitefont">마이페이지</em>
            </template>
            <b-dropdown-item v-show="loginStatus" @click='logout'><b-icon class='colblack' icon="power" aria-hidden="true"></b-icon><span class='colblack'>로그아웃</span></b-dropdown-item>
            <b-dropdown-item v-show="!loginStatus" href="#"><router-link :to="{ name: 'Signup' }"><b-icon class='colblack' icon="person-fill"></b-icon><span class='colblack'> 회원가입</span></router-link></b-dropdown-item>
            <b-dropdown-item v-show="!loginStatus" href="#"><router-link :to="{ name: 'Login' }"><b-icon  class='colblack' icon="power" aria-hidden="true"></b-icon><span class='colblack'> 로그인</span></router-link></b-dropdown-item>

          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <router-view  />
  </div>
</template>

<script>
import { mapGetters, mapState } from 'vuex'
import VueBootstrapTypeahead from 'vue-bootstrap-typeahead'

export default {
  name: "Navbar",
  data:function(){
    return{
      searchWord : '',
      logined : false
    }
  },
  components : {
    VueBootstrapTypeahead
  },
  computed : {
    ...mapState([
      'loginStatus',
      'moviesNm',
      'crewsNm',
    ]),
    ...mapGetters([
      'movieList'
    ]),
    candidate : function(){
      return this.$store.getters.movieList.filter(function(movie){
        return (movie.indexOf(this.searchWord) !== -1)
      })
    },
    searchNm: function () {
      return this.moviesNm.concat(this.crewsNm)
    }
  },
  methods: {
    toMain: function() {
      this.$router.push({ name: "Main" });
    },
    logout : function(){
      this.$store.dispatch('logout')
      this.$router.push({name:'Home'})
    },
    search: function() {
      this.$store.dispatch('search', this.searchWord)
      this.$router.push({name : 'SearchedList'})
    },
    requireLogin : function(){
      if(!localStorage.getItem('jwt')){
        alert('로그인이 필요한 서비스입니다.')
      }
    }
  },
  mounted : function(){
      if(localStorage.getItem('jwt')){
        this.logined=true
      }
    }
  
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=East+Sea+Dokdo&display=swap');


#navbar {
  width: 100vw;
  z-index: 1;
  position: sticky;
  background: none;
  border-bottom: darkgray 0.1em solid;
}
#ant{
  font-family: 'East Sea Dokdo', cursive;
  color: white;
  font-size: 2rem;
}
.navbar-light .navbar-nav .nav-link:link,
.navbar-light .navbar-nav .nav-link:visited,
.navbar-light .navbar-nav .nav-link:hover {
  color: white;
  text-decoration: none;
}
router-link:link,
router-link:visited,
router-link:hover{
  color: white;
  font-style: none;
}
.whitefont{
  color: white;
  font-style: none;
}
.whitefont:hover{
  color:white;
  font-style: none;
}
div.list-group > a:hover{
  background-color:#f5f5f5;
  border: none;
  color: black;
}
.colblack{
  color: black;
}
router-link:hover{
  background-color:#c2c2c2;
}
</style>
