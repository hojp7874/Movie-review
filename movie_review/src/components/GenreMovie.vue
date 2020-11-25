<template>
  <div id='genreMovie'>
    <div>
    <b-button-group size="sm" >
      <b-button
        v-for="(btn, idx) in genres"
        :key="idx"
        variant="outline-danger"
        pill
        :class="{clicked:genresState[idx]}"
        v-on:click="clicked(idx)"
      >
        {{ btn }}
      </b-button>
    </b-button-group>
    </div>
    <MovieList 
      :movies='filterdMovie'
    />
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'
import { mapState } from 'vuex'

export default {
  name : 'GenreMovie',
  components : {
    MovieList,
  },

  computed : {
    ...mapState([
      'genres',
      'genresState',
      'movies',
      'filterdMovie'
    ]),
    // filteredMovie : function(){
    //   const list =[]
    //   for(var i =0; i<this.genresState.length; i++){
    //     if(this.genresState[i]){
    //       list.push(this.genres[i])
    //     }
    //   }
    //   return this.movies.filter((movie)=>{
    //     return list.includes(movie.repGenreNm) 
    //   })
    // }
  },
  methods :{
    clicked : function(idx){
      this.$store.dispatch('stateChange',idx)
    }
  },
}
</script>

<style>
.clicked{
  background: #dc3545;
  color: white;
}
</style>

