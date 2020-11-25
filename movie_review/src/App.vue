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
#app::before{
    content: ' ';
    display: block;
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
    opacity: 0.2;
    background: url('~@/assets/img4.jpg') no-repeat center center;
    background-size: cover ;
    position: fixed;
}
#app{
  background-size: cover;
  background-attachment: fixed;
  width: 100vw;
  height:100vh;
  position: relative;
  background-color: #000;
}


@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@200;300;400;500;600;700;900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');

</style>
