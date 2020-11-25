<template>
  <div id="navbar">
    <b-navbar toggleable="lg">
      <b-navbar-brand @click="toMain" href="#">🎬</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="#">영화 목록</b-nav-item>
          <b-nav-item href="#">리뷰 목록</b-nav-item>
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
            <b-dropdown-item v-show="logined" href="#">내 활동</b-dropdown-item>
            <b-dropdown-item v-show="logined" @click='logout'>로그아웃</b-dropdown-item>
            <b-dropdown-item v-show="!logined" href="#"><router-link :to="{ name: 'Signup' }">회원가입</router-link></b-dropdown-item>
            <b-dropdown-item v-show="!logined" href="#"><router-link :to="{ name: 'Login' }">로그인</router-link></b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
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
      this.$router.go({ name: "Main" });
    },
    logout : function(){
      this.$store.dispatch('logout')
      this.$router.push({name:'Home'})
    },
    search: function() {
      this.$store.dispatch('search', this.searchWord)
    },
  },
  mounted : function(){
      if(localStorage.getItem('jwt')){
        this.logined=true
      }
    }
  
};
</script>

<style>
#navbar {
  width: 100vw;
  position: sticky;
  background: none;
  border-bottom: darkgray 0.1em solid;
}

.navbar-light .navbar-nav .nav-link:link,
.navbar-light .navbar-nav .nav-link:visited,
.navbar-light .navbar-nav .nav-link:hover {
  color: white;
  text-decoration: none;
}
</style>
