<template>

  <div id="app">
    <div class="m-3">
      <h2>모든 영화</h2>
    </div>
    <div class="flip-card-container p-0">
      <div class="flip-card col-2"
        v-for="(movie, idx) in movies"
        :key="idx"
        :movie='movie'
      >
        <div class="flip-card-front">
          <!-- <img :src="imgSrc" alt="" /> -->
          <img v-if="!movie.posterSrc" src="https://1080motion.com/wp-content/uploads/2018/06/NoImageFound.jpg.png" alt="">
          <img v-else :src="movie.posterSrc" alt="">
        </div>
        <div class="flip-card-back">
          <p>{{ movie.movieNm }}</p>
          <p>{{ movie.prdtYear }}</p>
          <p>{{ movie.nationAlt }}</p>
          <p>{{ movie.genreAlt }}</p>
          <div>
            <b-button id="show-btn"  @click="$bvModal.show(`bv-modal-example${idx}`), searchMV(movie.title)">show detail</b-button>
            <b-modal :id="'bv-modal-example'+idx" hide-footer>
                <template #modal-title style="text-align : center">
                {{ movie.movieNm }}
                </template>
                <div class="d-block text-center">
                <h3>Hello From This Modal!</h3>
                </div>
                <b-button class="mt-3" block @click="$bvModal.hide(`bv-modal-example${idx}`)">닫기</b-button>
            </b-modal>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieList",
  data: function(){
      return {
          defaultImg: 'https://1080motion.com/wp-content/uploads/2018/06/NoImageFound.jpg.png'
      }
  },
  props: {
    movies: {
      type: Array,
    },
  },
  methods :{
      searchMV : function(title){
        this.$store.dispatch('searchMV',title)
      }
  }
};
</script>

<style scoped>
#app {
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
.flip-card-container .flip-card:hover {
  transform: rotateY(180deg);
}
.flip-card {
  display: flex;
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform 0.5s;
  padding: 0;
}
.flip-card-front,
.flip-card-back {
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  position: absolute;
  border-radius: 0.5rem;
  padding: 10px;
}
.flip-card-front {
  background-color: #333;
  color: white;
}
.flip-card-back {
  background-color: darkgray;
  color: white;
  transform: rotateY(180deg);
}
.flip-card-front img {
  width: 100%;
  height: 100%;
  border-radius: 0.5rem;
}
h2 {
  text-align: center;
  color: White;
  text-decoration: underline;
}
.flip-card-back p {
  color: white;
  text-align: center;
}
</style>
