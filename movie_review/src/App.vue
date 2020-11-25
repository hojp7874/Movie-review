<template>
  <div id="app">

    <router-view @login='login=true' />
  </div>
</template>

<script>

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
}
</script>


<style>
*{
  font-family: 'Noto Sans KR', sans-serif;
  
}
/*  #2a2a2e */
#app{
  background-image: url('~@/assets/rainbow.png');
  background-size: cover;
  background-attachment: fixed;
  width: 100vw;
  height:100vh;
}
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');
</style>
