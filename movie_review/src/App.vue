<template>
  <div id="app">

    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function() {
    return {
    }
  },
  created: function() {
    this.$store.dispatch('getMovies')
    this.$store.dispatch('getMovieScore')
    this.$store.dispatch('getMovieCrew')
    this.$store.dispatch('getUser')
  },
}
</script>


<style>
*{
  font-family: 'Noto Serif KR', serif;
}
/*  #2a2a2e */
#app{
  background-color: #323437;
  width: 100vw;
  height:100vh;
}
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@200;300;400;500;600;700;900&display=swap');
</style>
