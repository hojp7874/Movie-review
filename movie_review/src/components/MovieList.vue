<template>
  <div id="MovieList">
    <div class="m-3">
      <h2>모든 영화</h2>
    </div>
    <div class="flip-card-container p-0">
      <MovieCard
        v-for="(movie,idx) in movies"
        :key="idx"
        :movie='movie'
        :idx='idx'
      />
    </div>
  </div>
</template>

<script>
// import _ from 'lodash' 
import {mapState} from 'vuex'
import MovieCard from '@/components/MovieCard.vue'

export default {
  name: "MovieList",
  data: function(){
      return {
      }
  },
  props: {
  },
  components:{
    MovieCard,
  },
  computed : {
    ...mapState([
      'movies',
      'score',
      'crew'
    ])
  },

};
</script>

<style scoped>
#MovieList {
  background-color: #323437;
  width: 100vw;
  height: 100vh;
}
* {
  margin: 0;
  padding: 0 ;
  box-sizing: border-box;
}
.flip-card-container {
  width: 100vw;
  height: 30vh;
  border-radius: 0.5rem;
  display: flex;
}
h2 {
  text-align: center;
  color: White;
  text-decoration: underline;
}

</style>
