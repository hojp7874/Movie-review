<template>
  <div id="MovieCard" class='col-2'>
    <div class="flip-card" :movie='movie' :idx='idx'>
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
        <b-button id="show-btn"  @click="$bvModal.show(`bv-modal-example${idx}`), searchMV(movie.movieNmEn)">show detail</b-button>
        <b-modal :id="'bv-modal-example'+idx" hide-footer>
            <template #modal-title style="text-align : center">
            {{ movie.movieNm }}
            </template>
            <div class="d-block text-center">
            <iframe :src="mvUrl" frameborder="0" width=90% height='470'  allowfullscreen></iframe>
            <h3>Hello From This Modal!</h3>
            </div>
            <b-button class="mt-3" block @click="$bvModal.hide(`bv-modal-example${idx}`)">닫기</b-button>
        </b-modal>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
const GOOGLE_API ='https://www.googleapis.com/youtube/v3/search'
// const API_KEY = process.env.VUE_APP_API_KEY
const API_KEY = 'AIzaSyDMOGwcTZCpGOR3-N1uBqTj6v1K8J9fy7U'


export default {
  name: "MovieCard",
  data: function(){
      return {
        defaultImg: 'https://1080motion.com/wp-content/uploads/2018/06/NoImageFound.jpg.png',
        mvUrl:'',
        thumbnail :'',
      }
  },
  props: {
    movie: {
      type: Object,
    },
    idx : {
      type : Number,
    }
  },
  methods :{
      searchMV : function(title){
        console.log(title)
        axios.get(GOOGLE_API, {
        params:{
          key : API_KEY,
          part : 'snippet',
          type : 'video',
          q : `${title}+trailer`,
        }
      })
        .then( res => {
          const mvWord = res.data.items[0].id.videoId
          this.mvUrl = `https://www.youtube.com/embed/${mvWord}`
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created : function(){
    return this.$emit('getImgUrl',this.movie.posterSrc)
  }
};
</script>

<style scoped>
#MovieCard {
  background-color: #323437;
  width: 100%;
  height: 100%;
  display : flex;
}
* {
  margin: 0;
  padding: 0 ;
  box-sizing: border-box;
}

.flip-card:hover {
  transform: rotateY(180deg);
}
.flip-card {
  display: flex;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform 0.7s;
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
.flip-card-back p {
  color: white;
  text-align: center;
}
</style>
