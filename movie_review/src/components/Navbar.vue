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
              <b-form-input
                v-model="searchWord"
                size="sm"
                class="mr-sm-2"
                placeholder="검색어를 입력하세요"
                ></b-form-input>
                <!-- <ul v-show="searchWord.length">
                  <li v-for="(wd,idx) in candidate" :key='idx'></li>
                </ul> -->
              <b-button size="sm" class="my-2 my-sm-0" type="submit">🔍</b-button>
          </b-nav-form>

          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template #button-content>
              <em class="whitefont">마이페이지</em>
            </template>
            <b-dropdown-item v-show="loginStatus" href="#">내 활동</b-dropdown-item>
            <b-dropdown-item v-show="loginStatus" @click='logout'>로그아웃</b-dropdown-item>
            <b-dropdown-item v-show="!loginStatus" href="#"><router-link :to="{ name: 'Signup' }">회원가입</router-link></b-dropdown-item>
            <b-dropdown-item v-show="!loginStatus" href="#"><router-link :to="{ name: 'Login' }">로그인</router-link></b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
import { mapGetters, mapState } from 'vuex'

export default {
  name: "Navbar",
  data:function(){
    return{
      searchWord : '',
      // movieList:[],
      // loginStatus:'',
    }
  },
  components : {
  },
    computed : {
    ...mapState([
      'loginStatus'
    ]),
    ...mapGetters([
      'movieList'
    ]),
    candidate : function(){
      return this.$store.getters.movieList.filter(function(movie){
        return (movie.indexOf(this.searchWord) !== -1)
      })
    }
  },
  methods: {
    toMain: function() {
      this.$router.push({ name: "Main" });
    },
    logout : function(){
      this.$store.dispatch('logout')
    },
  },
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
