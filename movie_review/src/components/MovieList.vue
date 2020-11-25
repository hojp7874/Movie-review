<template>
  <div id="MovieList">
    <div id="m3">
      <h2>모든 영화</h2>
    </div>
    <div class="flip-card-container p-0 col-12">
      <MovieCard
        v-for="(movie,idx) in search"
        :key="idx"
        :movie='movie'
        :idx='idx'
        class="p-1"
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
      'crew',
      'search',
    ])
  },

};
</script>

<style scoped>
#MovieList {
  /* background: url('~@/assets/img4.jpg'); */
  /* background-attachment: fixed; */
  background-color: black;
  /* width: 100vw; */
  height: 310vh;
  overflow:auto
}
#m3{
  margin : 10vh 0;
}
* {
  margin: 0;
  padding: 0 ;
  box-sizing: border-box;
}
.flip-card-container {
  width: 100vw;
  height: 45vh;
  border-radius: 0.5rem;
  display: flex;
  flex-flow : row wrap
}
h2 {
  text-align: center;
  color: White;
  text-decoration: underline;
}

</style>
