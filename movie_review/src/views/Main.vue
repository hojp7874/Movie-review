<template>
  <div id='Main'>
    <Navbar />
    <br>
    <Recommended />
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
  },
  updated : function(){
    console.log(localStorage.getItem('jwt'))
  }
}
</script>

<style>
#Main{
  background-color: #323437;

}

</style>