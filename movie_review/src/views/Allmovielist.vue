<template>
  <div id='Allmovielist'>
    <Navbar />
    <br>
    <h2>모든 영화</h2>
    <MovieList 
      :movies="movies"
    />
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
import MovieList from '@/components/MovieList.vue'
import { mapState } from 'vuex'


export default {
  name : 'Allmovielist',
  components : {
    Navbar,
    MovieList
  },
  computed : {
      ...mapState([
          'movies',
      ]),
  }
}
</script>

<style >
#Allmovielist::before{
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
#Allmovielist{
  background-size: cover;
  background-attachment: fixed;
  width: 100vw;
  height:100vh;
  position: relative;
  background-color: #000;
}
h2 {
  text-align: center;
  color: White;
  font-weight: 700;
  margin: 3% 0 3% 0;
    font-size: 2rem;
}
</style>