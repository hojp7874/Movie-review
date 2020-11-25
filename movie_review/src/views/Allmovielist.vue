<template>
  <div id='Allmovielist'>
    <Navbar />
    <br>
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
          'search',
      ]),
  }
}
</script>

<style>

</style>