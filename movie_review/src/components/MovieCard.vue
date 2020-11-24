<template>
  <div id="MovieCard" class='col-2'>
    <div class="flip-card" :movie='movie' :idx='idx'>
    <div class="flip-card-front">
      <!-- <img :src="imgSrc" alt="" /> -->
      <img v-if="!movie.posterSrc" src="https://1080motion.com/wp-content/uploads/2018/06/NoImageFound.jpg.png" alt="">
      <img v-else :src="movie.posterSrc" alt="">
    </div>
    <div class="flip-card-back">
      
      <title><span>{{ movie.movieNm }}</span></title>
      <div>
        <p>개요</p><span> {{ movie.genreAlt }} | {{movie.nationAlt}}</span>
        <p>개봉</p><span> {{movie.movieCd}} | ☆☆☆☆☆</span>
      </div>
      <b-button id="show-btn"  @click="$bvModal.show(`bv-modal-example${idx}`), searchMV(movie.movieNm), getMovieScore(movie.movieCd), getReview(movie.movieCd)">show detail</b-button>

        <b-modal :id="'bv-modal-example'+idx" hide-footer>
            <template #modal-title style="text-align : center">
            <span>{{ movie.movieNm }} | {{stars[0]}} {{stars[1]}}</span>
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
                    <b-button @click='scoreSelect(movie.movieCd,1)' variant="outline-warning">
                      <b-icon icon="emoji-angry"></b-icon>
                      <p>최악이에요!</p>
                    </b-button>
                    <b-button @click='scoreSelect(movie.movieCd,2)' variant="outline-warning">
                      <b-icon icon="emoji-frown"></b-icon>
                      <p>그저 그래요</p>
                    </b-button>
                    <b-button @click='scoreSelect(movie.movieCd,3)' variant="outline-warning">
                      <b-icon icon="emoji-neutral"></b-icon>
                      <p>볼만해요</p>
                    </b-button>
                    <b-button @click='scoreSelect(movie.movieCd,4)' variant="outline-warning">
                      <b-icon icon="emoji-smile"></b-icon>
                      <p>재밌어요</p>
                    </b-button>
                    <b-button @click='scoreSelect(movie.movieCd,5)' variant="outline-warning">
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
                    v-for="(person, idx) in movie.peoples"
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
                  <form @submit.prevent='makeReview(movie.movieCd)' action="#">
                    <input v-model.trim="reviewTitle" type="text">
                    <textarea v-model.trim="reviewContent" id="" cols="30" rows="4"></textarea>
                    <button @click='makeReview(movie.movieCd)' type="submit">리뷰쓰기</button>
                  </form>
                </div>
                <div>
                  <ul>
                    <li
                      v-for=" (review,idx) in reviews"
                      :key='idx'
                      :review='review'
                    >
                      <p>작성자 : {{review.user.username}}</p>
                      <p>제목 : {{review.title}}</p>
                      <p>내용: {{review.content}}</p>
                    </li>
                  </ul>
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
import VueJwtDecode from 'vue-jwt-decode'
const GOOGLE_API ='https://www.googleapis.com/youtube/v3/search'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
const API_KEY = process.env.VUE_APP_API_KEY
import {mapState} from 'vuex'

export default {
  name: "MovieCard",
  data: function(){
      return {
        defaultImg: 'https://1080motion.com/wp-content/uploads/2018/06/NoImageFound.jpg.png',
        mvUrl:'',
        thumbnail :'',
        reviews:[],
        score :[],
        reviewTitle:'',
        reviewContent : '',
      }
  },
  computed:{
    ...mapState({
      crew : 'crew',
      users : 'users',
    }),
    stars : function(){
      if(!this.score.length){
        return [0.00, '☆'.repeat(5)]
      }else{
        const n = Object.keys(this.score).length
        let stack =0
        this.score.forEach(function(sc){stack+=sc.score})
        const value = parseFloat(stack/n).toFixed(2)
        const value2 = Math.floor(value)
        return [value,'★'.repeat(value2) + '☆'.repeat(5-value2)]
      }
    },
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
    setToken: function () {
      const token = localStorage.getItem('jwt')

      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    getUsername : function(){
      const token = localStorage.getItem('jwt')
      const user = VueJwtDecode.decode(token)
      return user.username
    },
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
      axios.get(`${SERVER_URL}/movies/${code}/review_list/`)
        .then((res) => {
          if(res.data=== []){
            this.reviews =[]
          }else{
            this.reviews = res.data
          }
        })
        .catch((err)=>{
          console.log(err)
        })        
    },
    getMovieScore :function(code){
      axios.get(`${SERVER_URL}/movies/${code}/movie_score_list/`)
        .then((res) => {
          const movieScore = res.data
          this.score = movieScore
        })
        .catch((err)=>{
          console.log(err)
        })      
    },
    scoreSelect : function(code, score){
      const user2 =this.getUsername()
      let can = false
      this.score.forEach((obj)=>{
        if(obj.user===user2){
          can = false
        }else{
          can = true
        }
      })
      if(can){
        const config = this.setToken()
        const item = {
          movie: code,
          score : score,
          user : user2
        }
        axios.post(`${SERVER_URL}/movies/movie_score_create/`,item,config)
          .then(() => {
            this.score.push(item)
          })
          .catch((err)=>{
            console.log(err)
          })            
      }else{
        return
      }
    },
    makeReview : function(code){
      const config = this.setToken()
      // VueJwtDecode.decode(localStorage.getItem('jwt'))
      const user2 =this.getUsername()
      const item = {
        movie: code,
        title : this.reviewTitle,
        content : this.reviewContent,
        user : {username : user2}

      }
      axios.post(`${SERVER_URL}/movies/review_create/`,item,config)
        .then(() => {
          this.reviews.push(item)
          this.reviewContent=''
          this.reviewTitle=''
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

b-modal{
  width: 80vw;
}
b-button>p{
  font-size: 0.5em;
}
</style>
