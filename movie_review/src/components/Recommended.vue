<template>
  <div id="Recommend">
    <div>
      <h2>화제의 영화</h2>
    </div>
    <div id="caru">

      <b-carousel
        id="carousel-1"
        v-model="slide"
        :interval="4000"
        controls
        indicators
        style="text-shadow: 1px 1px 2px #333;"
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
      >
        <p>inner b-carousel</p>


        <b-carousel-slide
          v-for="(movie,idx) in movies"
          :key="idx"
        > 
          <!-- <template v-slot:img> -->
          <div style="height: 30vh">
            <MovieCard
              v-for="(movie,idx) in movies"
              :key="idx"
              :movie='movie'
              :idx='idx'
            />
          </div>
          <!-- </template> -->
        </b-carousel-slide>

      </b-carousel>
    </div>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import MovieCard from '@/components/MovieCard.vue'

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
    MovieCard
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
  margin: 2em 0;
}

h2 {
  color: white;
  text-align: center;
  text-decoration-line: underline;
}
#caru {
  margin: 3% 0;
}

b-carousel-slide {
  border-radius: 0.5rem;
  height: 50vh;
}
.flip-card-container {
  width: 100vw;
  height: 30vh;
  border-radius: 0.5rem;
  display: flex;
}
.carousel-indicators {
  margin-top: 50%;
}
#caru > div > div > div > div {
  left: 38vw;
}
</style>
