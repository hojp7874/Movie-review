<template>
  <div id='Main'>
    <Navbar />
    <br>
    <Recommended />
    <div class='blankblock'></div>
    <MovieList 
      :movies="movies"
    />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import Navbar from '@/components/Navbar.vue'
import Recommended from '@/components/Recommended.vue'
import MovieList from '@/components/MovieList.vue'

export default {
  name: 'Main',
  components: {
    Navbar,
    Recommended,
    MovieList
  },
  computed: {
      ...mapState([
          'movies',
      ])
  }
}
</script>

<style scoped>
#Main{
  background-color: #323437;
  width: 100vw;
  height:100vh;
}
.blankblock{
  height: 10vh;
}

</style>