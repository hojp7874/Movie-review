<template>
  <div id="MovieCard" class='col-2'>
    <div class="flip-card" :movie='movie' :idx='idx'>
    <div class="flip-card-front">
      <!-- <img :src="imgSrc" alt="" /> -->
      <img v-if="!movie.posterSrc" src="https://1080motion.com/wp-content/uploads/2018/06/NoImageFound.jpg.png" alt="">
      <img v-else :src="movie.posterSrc" alt="">
    </div>
    <div class="flip-card-back">
      
      <title><span>{{ movie.movieNm }}☆☆☆☆☆</span></title>
      <div>
        <p>개요</p><span> {{ movie.genreAlt }} | {{movie.nationAlt}}</span>
        <p>개봉</p><span> {{movie.movieCd}} | ☆☆☆☆☆</span>
      </div>
      <b-button id="show-btn"  @click="$bvModal.show(`bv-modal-example${idx}`), searchMV(movie.movieNm), getReview(movie.movieCd)">show detail</b-button>

        <b-modal :id="'bv-modal-example'+idx" hide-footer>
            <template #modal-title style="text-align : center">
            {{ movie.movieNm }}
            </template>
            <div class="d-block">
              <div id='modalContent'>
                <div>
                  <img class="col-12" v-if="!movie.posterSrc" src="https://1080motion.com/wp-content/uploads/2018/06/NoImageFound.jpg.png" alt="">
                  <img class="col-12" v-else :src="movie.posterSrc" alt="">
                </div>
                <div>
                  <title>{{ movie.movieNm }}</title>
                  <p>개요</p><span> {{ movie.genreAlt }} | {{movie.nationAlt}}</span>
                  <p>개봉</p><span> {{movie.prtdYear}}</span>
                <div>
                  <b-button-group>
                    <b-button variant="outline-warning">
                      <b-icon icon="emoji-angry"></b-icon>
                      <p>최악이에요!</p>
                    </b-button>
                    <b-button variant="outline-warning">
                      <b-icon icon="emoji-frown"></b-icon>
                      <p>그저 그래요</p>
                    </b-button>
                    <b-button variant="outline-warning">
                      <b-icon icon="emoji-neutral"></b-icon>
                      <p>볼만해요</p>
                    </b-button>
                    <b-button variant="outline-warning">
                      <b-icon icon="emoji-smile"></b-icon>
                      <p>재밌어요</p>
                    </b-button>
                    <b-button variant="outline-warning">
                      <b-icon icon="emoji-heart-eyes"></b-icon>
                      <p>최고에요!</p>
                    </b-button>
                  </b-button-group>
                </div>
                <div>
                  <p>영화 줄거리</p>
                  <span>{{movie.story}}</span>
                </div>
                <ul>
                  <li
                    v-for="(person, idx) in people"
                    :key="idx"
                    :person='person'
                  >
                    <div><span>{{person.role}} : </span><span>{{person.name}}</span></div>
                    <img :src="person.photo" alt="">
                  </li>
                </ul>
                </div>
                <div>
                  <p>영화 예고편</p>
                  <iframe :src="mvUrl" frameborder="0" width=100% height='470'  allowfullscreen></iframe>
                </div>
                <div>
                  <p>영화 리뷰</p>
                  <form action="">
                    <textarea name="" id="" cols="30" rows="4"></textarea>
                    <button>리뷰쓰기</button>
                  </form>
                </div>
                <div>
                  <ul v-if="reviews">
                    <li
                      v-for=" (review,idx) in reviews"
                      :key='idx'
                      :review='review'
                    >
                      <p>글쓴이 : {{review.id | getUserId(review.id)}}</p>
                      <p>제목 : {{review.title}}</p>
                      <p>내용: {{review.content}}</p>
                    </li>
                  </ul>
                  <div v-if="!reviews">
                    <p>작성된 리뷰가 없습니다.</p>
                  </div>
                </div>
              </div>
            </div>
            <b-button class="mt-3" block @click="$bvModal.hide(`bv-modal-example${idx}`)">닫기</b-button>
        </b-modal>

    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
const GOOGLE_API ='https://www.googleapis.com/youtube/v3/search'
// const API_KEY = process.env.VUE_APP_API_KEY
const API_KEY = 'AIzaSyDMOGwcTZCpGOR3-N1uBqTj6v1K8J9fy7U'
import {mapState} from 'vuex'

export default {
  name: "MovieCard",
  data: function(){
      return {
        defaultImg: 'https://1080motion.com/wp-content/uploads/2018/06/NoImageFound.jpg.png',
        mvUrl:'',
        thumbnail :'',
        reviews:[],
      }
  },
  computed:{
    ...mapState([
      'crew',
      'score',
      'users'
    ]),
    people : function(){
      return this.crew.filter((obj)=>{
        return obj.movies.includes(this.movie.movieCd)
      })
    },
    rating : function(){
      return this.score.filter()
    }
  },
  props: {
    movie: {
      type: Object,
    },
    idx : {
      type : Number,
    },
  },
  methods :{
      searchMV : function(title){
        axios.get(GOOGLE_API, {
        params:{
          key : API_KEY,
          part : 'snippet',
          type : 'video',
          q : `영화+${title}+예고`,
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
    getReview : function(code){
      axios.get(`http://127.0.0.1:8000/movies/${code}/review_list_create/`)
        .then((res) => {
          if(res.data=== []){
            this.reviews =false
          }else{
            this.reviews = res.data
          }
        })
        .catch((err)=>{
          console.log(err)
        })        
    },
  },
  created : function(){
    this.$emit('getImgUrl',this.movie.posterSrc)
    this.$emit('getCrew',this.movie.movieCd)
  },

};
</script>

<style scoped>
#MovieCard {
  background-color: #323437;
  width: 100%;
  height: 100%;
  padding: 0;
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
}
.flip-card-front {
  color: white;
}
.flip-card-back {
  background-color: #f5f5f5;
  color: white;
  transform: rotateY(180deg);
}
.flip-card-front img {
  width: 100%;
  height: 100%;
  border-radius: 0.5rem;
}
.flip-card-back p {
  color: #5d4037;
  font-size: 1.5rem;
}
.flip-card-back span{
  color: #000000;
  font-size: 1rem;
  margin-bottom : 1rem;
  overflow: hidden;
}
.flip-card-back>:nth-child(2){
  height: 80%;
}
#show-btn{
  height: 10%;
  background: #757575;
  border: 0 none;
  border-radius: 0.5rem;
  color: white;
  text-align: center;
}
#modalContent{
  display: flexbox;
  width: 100%;
}
#modalContent>div img{
  /* width: %; */
}
b-modal{
  width: 80vw;
}
b-button>p{
  font-size: 0.5em;
}
</style>
