<template>
  <div id='Main' class="p-0">
    <Navbar />
    <br>
    <Recommended />
    <br><br>
    <!-- <GenreMovie /> -->
    <!-- <MovieList 
      :movies="movies"
    /> -->
  </div>
</template>

<script>
import { mapState } from 'vuex'
import Navbar from '@/components/Navbar.vue'
import Recommended from '@/components/Recommended.vue'
// import MovieList from '@/components/MovieList.vue'
// import GenreMovie from '@/components/GenreMovie.vue'

export default {
  name: 'Main',
  components: {
    Navbar,
    Recommended,
    // MovieList,
    // GenreMovie,
  },
  computed: {
    ...mapState([
        'movies',
        'search',
    ]),
  },
  updated : function(){
    console.log(localStorage.getItem('jwt'))
  }
}
</script>

<style>
#Main::before{
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
#Main{
  background-size: cover;
  background-attachment: fixed;
  width: 100vw;
  height:100vh;
  position: relative;
  background-color: #000;
  
}

</style>