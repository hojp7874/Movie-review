<template>
  <div id='genreMovie'>
    <div class='text-center'>
    <b-button-group size="sm" >
      <b-button
        v-for="(btn, idx) in genres"
        :key="idx"
        pill
        :class="{myclass : genresState[Number(idx)]}"
        v-on:click="clicked(idx)"
        
      >
        <span :class="{myclass : genresState[Number(idx)]}" >{{ btn }}</span>
      </b-button>
    </b-button-group>
    </div>
    <br>
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

.myclass{
  color: gold;
}


</style>

