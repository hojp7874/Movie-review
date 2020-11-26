<template>
  <div id="app" class="container-fluid p-0 m-0">
    <router-view @login='login=true' />
  </div>
</template>

<script>
import {mapState} from 'vuex'


export default {
  name: 'App',
  data: function() {
    return {
      login : false,
      
    }
  },
  created: function() {
    this.$store.dispatch('getMovies')
    this.$store.dispatch('getMovieCrew')
    this.$store.dispatch('getUser')
    const token = localStorage.getItem('jwt')
    if(token){
      this.login = true
    }
  },
  computed : {
    ...mapState([
      'loginStatus'
    ])
  }
}
</script>


<style>
*{
  font-family: 'Noto Sans KR', sans-serif;
  
}

@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@200;300;400;500;600;700;900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');

</style>
