<template>
  <div id="Recommend">
    <div>
      <h2>화제의 영화</h2>
      <br>
    </div>
      <carousel-3d
        v-model="slide"
        :autoplay="true"
        :autoplay-timeout="2500"
        class="col-12"
        :height='400'
      >
        <slide
          v-for="(movie,idx) in movies"
          :key="idx" 
          :index="idx"
          :height='4000'
        >
          <MovieCard
            :movie='movie'
            :idx='idx'
            class="col-12 p-0 m-0"
          />
        </slide>
      </carousel-3d>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import MovieCard from '@/components/MovieCard.vue'
import { Carousel3d, Slide } from 'vue-carousel-3d';

export default {
  name: "Recommended",
  data: function() {
    return {
      slide: 0,
      sliding: null,
      url :'',
    };
  },
  components :{
    MovieCard,
    Carousel3d,
    Slide,
  },
  methods: {
    onSlideStart() {
      this.sliding = true;
    },
    onSlideEnd() {
      this.sliding = false;
    },
    getImgUrl(url){
      this.url = url
    }
  },
  computed :{
    ...mapState([
      'movies'
    ])
  }
};
</script>
<style scoped>
#Recommend {
  margin-bottom: 0;
  height: 80vh;
  position: relative;
  padding-top: 3%;
}
#Recommend>:nth-child(1){
  margin: 0;
}

h2 {
  color: white;
  text-align: center;
  font-weight: 700;
  font-size: 3rem;
}
#caru {
  margin: 3% 0;
}

div.carousel-3d-slide{
  border-radius: 0.5rem;
}

.carousel-indicators {
  margin-top: 50%;
}
b-carousel-slide>div{
  position: absolute;
  top: 50vh;
}
carousel-3d-slider{
  padding: 0;
  border: 0 none;
}
div{
  border: 0 none;
  background-color: none;
} 
carousel-3d{
  height: 90vh;
}
</style>
