<template>
  <div id="MovieCard" class='col-2'>
    <div class="flip-card" :movie='movie' >
    <div
      class="flip-card-front"
      style="cursor:pointer"
      @click="$bvModal.show(`bv-modal-${idx}`), getTrailer(movie.movieNm)"
    >
      <!-- <img :src="imgSrc" alt="" /> -->
      <img v-if="!movie.posterSrc" src="https://1080motion.com/wp-content/uploads/2018/06/NoImageFound.jpg.png" alt="">
      <img v-else :src="movie.posterSrc" alt="">
    </div>
    <div
      class="flip-card-back"
      style="cursor:pointer"
      @click="$bvModal.show(`bv-modal-${idx}`), getTrailer(movie.movieNm)"
    >
      <div class="text-center">
        <h3 class="mt-5 mb-2 text-dark">{{ movie.movieNm }}</h3>
        <p>{{ movie.genreAlt }} | {{movie.nationAlt}}</p>
        <p>{{movie.openDt}} {{movie.prdtStatNm}}</p>
        <p>평점: {{stars[1]}}</p>
        <!-- <p>{{score.length}}개의 점수 평가</p> -->
        <p>리뷰 {{Object.keys(reviews).length}}개</p>
        <p>내 평점: </p>
        <b-icon icon="emoji-angry" style="color : brown"></b-icon>
        <b-icon icon="emoji-frown" style="color : brown"></b-icon>
        <b-icon icon="emoji-neutral" style="color : brown"></b-icon>
        <b-icon icon="emoji-smile" style="color : brown"></b-icon>
        <b-icon icon="emoji-heart-eyes" style="color : brown"></b-icon>
      </div>
      <b-modal :id="'bv-modal-'+idx" hide-footer size='xl'>
        <template #modal-title>
          <div>{{ movie.movieNm }} | {{stars[1]}}</div>
        </template>
        <div class="d-block">
          <div id='modalContent'>
            <div>
              <p>영화 예고편</p>
              <iframe :src="mvUrl" frameborder="0" width=100% height='470' allowfullscreen></iframe>
            </div><hr class="my-3">
            <div class="container d-flex flex-column">
              <div class="d-flex flex-row">
                <div class="col-3 text-center">
                  <p class="mb-1">
                    <span> {{ movie.genreAlt }} | {{movie.nationAlt}}</span>
                    <span> {{movie.prtdYear}}</span>
                  </p>
                  <img v-if="!movie.posterSrc" src="https://1080motion.com/wp-content/uploads/2018/06/NoImageFound.jpg.png" alt="">
                  <img v-else :src="movie.posterSrc" alt="">
                  <!-- <title>{{ movie.movieNm }}</title> -->
                </div>
                <div class="col-9 d-flex flex-column">
                  <p class="mb-1">영화 줄거리</p>
                  <span class="flex-fill d-flex flex-row">
                    <p class="align-self-center">
                      {{movie.story}}
                    </p>
                  </span>
                </div>
              </div><hr class="my-3">
              <div class="container d-flex flex-row flex-wrap">
                <div
                  v-for="(person, idx) in movie.peoples"
                  :key="idx"
                  :person='person'
                  class="col-3"
                >
                  <div>
                    <span>{{person.name}} </span>
                    <span v-if="person.role=='감독'">({{person.role}})</span>
                  </div>
                  <img class="w-75" v-if="person.photo!=='이미지 없음'" :src="person.photo" alt="">
                  <img class="w-75" v-else src="https://1080motion.com/wp-content/uploads/2018/06/NoImageFound.jpg.png" alt="">
                </div>
              </div><hr class="my-3">
              <!-- 리뷰작성 -->
              <div>
                <b-button v-b-toggle.collapse-3 variant="primary" class="m-1">리뷰 작성</b-button>
                <span>
                  <b-button-group>
                    <b-button :class="{bgON : btn1}" @click='scoreSelect(movie.movieCd,1)' variant="outline-primary">
                      <b-icon icon="emoji-angry"></b-icon>
                      <!-- <p>최악이에요!</p> -->
                    </b-button>
                    <b-button :class="{bgON : btn2}" @click='scoreSelect(movie.movieCd,2)' variant="outline-primary">
                      <b-icon icon="emoji-frown"></b-icon>
                      <!-- <p>그저 그래요</p> -->
                    </b-button>
                    <b-button :class="{bgON : btn3}" @click='scoreSelect(movie.movieCd,3)' variant="outline-primary">
                      <b-icon icon="emoji-neutral"></b-icon>
                      <!-- <p>볼만해요</p> -->
                    </b-button>
                    <b-button :class="{bgON : btn4}" @click='scoreSelect(movie.movieCd,4)' variant="outline-primary">
                      <b-icon icon="emoji-smile"></b-icon>
                      <!-- <p>재밌어요</p> -->
                    </b-button>
                    <b-button :class="{bgON : btn5}" @click='scoreSelect(movie.movieCd,5)' variant="outline-primary">
                      <b-icon icon="emoji-heart-eyes"></b-icon>
                      <!-- <p>최고에요!</p> -->
                    </b-button>
                  </b-button-group>
                </span>
                <b-collapse id="collapse-3">
                  <b-card>
                    <form @submit.prevent='makeReview(movie.movieCd)' action="#">
                      <div>
                        <!-- Using props -->
                        <b-input-group prepend="제목">
                          <b-form-input v-model.trim="reviewTitle" type="text"></b-form-input>
                        </b-input-group>
                        <b-input-group prepend="내용">
                          <b-form-textarea v-model.trim="reviewContent" id="" cols="30" rows="4" type="text"></b-form-textarea>
                        </b-input-group>
                        <b-button variant="primary" @click='makeReview(movie.movieCd)' type="submit">리뷰쓰기</b-button>
                      </div>
                    </form>
                  </b-card>
                </b-collapse>
              </div>
            </div>
            <div>
              <ul>
                <li
                  v-for=" (review,idx) in reviews"
                  :key='idx'
                  :review='review'
                >
                  <button class='heart' @click='reviewLike(review,false)' v-if="review.like_users.includes(nowUser)"><b-icon icon="heart-fill" style="color : red"></b-icon></button>
                  <button class='heart' @click='reviewLike(review,true)' v-else><b-icon icon="heart" style="color : red"></b-icon></button>
                  <p>{{review.like_users.length}}명이 좋아합니다.</p>
                  <p>작성자 : {{review.user.username}}</p>
                  <p>제목 : {{review.title}}</p>
                  <p>내용: {{review.content}}</p>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <b-button class="mt-3" block @click="$bvModal.hide(`bv-modal-${idx}`)">닫기</b-button>
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
        btn1:false,
        btn2:false,
        btn3:false,
        btn4:false,
        btn5:false,
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
        const list1 = this.score.filter((sc)=> sc.score===1).length
        const list2 = this.score.filter((sc)=> sc.score===2).length
        const list3 = this.score.filter((sc)=> sc.score===3).length
        const list4 = this.score.filter((sc)=> sc.score===4).length
        const list5 = this.score.filter((sc)=> sc.score===5).length
        const value = parseFloat(stack/n).toFixed(2)
        const value2 = Math.floor(value)
        return [value,'★'.repeat(value2) + '☆'.repeat(5-value2), list1, list2, list3, list4, list5]
      }
    },
    nowUser : function(){
      return this.getUsername()
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
    scoreSelect : function(code, newScore){
      //비로그인
      if(!localStorage.getItem('jwt')){
        const ans = confirm('영화 평점을 남기려면 로그인 해주세요.')
        if(ans){
          this.$router.push({name:'Login'})
        }
      //로그인
      }else{
        const user2 =this.getUsername()
        const config = this.setToken()
        let scoreList = this.score.map(a=>a.score)
        let userList = this.score.map(a=>a.user)
        const item = {
          movie: code,
          score : newScore,
          user : user2
        }
        
        const scoreIdx = userList.indexOf(user2)
        if(scoreIdx !=-1){
          //리뷰가 있으면
          if(scoreList[scoreIdx] === newScore){
            // 기존의 점수와 같으면 -> DELETE
            axios.delete(`${SERVER_URL}/movies/${code}/movie_score_update_delete/`,{headers : {Authorization: this.setToken().headers.Authorization},data : {movie : code, score : scoreList[scoreIdx], user: user2}})
              .then(() => {
                this.score.splice(scoreIdx,1)
                this.btn1=false
                this.btn2=false
                this.btn3=false
                this.btn4=false
                this.btn5=false
              })
              .catch((err)=>{
                console.log(err)
              })
          }else{
            // 다르면 put
            axios.patch(`${SERVER_URL}/movies/${code}/movie_score_update_delete/`,{data : {score : newScore}},config)
              .then(() => {
                this.score[scoreIdx].score = item.score
                switch(item.score){
                  case 1 :
                    this.btn1=true;
                    this.bnt2=false; this.btn3=false; this.btn4=false; this.btn5=false;
                    break;
                  case 2 :
                    this.btn2=true;
                    this.btn1=false; this.btn3=false; this.btn4=false; this.btn5=false;
                    break;
                  case 3 :
                    this.btn3=true;
                    this.btn1=false; this.btn2=false; this.btn4=false; this.btn5=false;
                    break;
                  case 4 :
                    this.btn4=true;
                    this.btn1=false; this.btn2=false; this.btn3=false; this.btn5=false;
                    break;
                  case 5 :
                    this.btn5=true;
                    this.btn1=false; this.btn2=false; this.btn3=false; this.btn4=false;
                    break;
                  default :
                    break;
              }
              })
              .catch((err)=>{
                console.log(err)
              })
          }
        //POST
        }else{
          axios.post(`${SERVER_URL}/movies/movie_score_create/`,item,config)
            .then(() => {
              this.score.push(item)
                switch(item.score){
                  case 1 :
                    this.btn1=true;
                    break;
                  case 2 :
                    this.btn2=true;
                    break;
                  case 3 :
                    this.btn3=true;
                    break;
                  case 4 :
                    this.btn4=true;
                    break;
                  case 5 :
                    this.btn5=true;
                    break;
                  default :
                    break;
              }    
            })
            .catch((err)=>{
              console.log(err)
            })
        }
      }
    },
    makeReview : function(code){
      if(!localStorage.getItem('jwt')){
        const ans = confirm('영화에 대한 리뷰를 남기려면 로그인 해주세요.')
        if(ans){
          this.$router.push({name:'Login'})
        }
      }
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
    reviewLike:function(review,bool){
      const user2 =this.getUsername()
      const config = this.setToken()
      axios.post(`${SERVER_URL}/movies/${review.id}/review_like/`,bool,config)
        .then(()=>{
          const idx = this.reviews.map(a=>a.id).indexOf(review.id)
          if(bool){
            this.reviews[idx].like_users.push(user2)
          }else{
            const userIdx = this.reviews[idx].like_users.indexOf(user2)
            this.reviews[idx].like_users.splice(userIdx,1)
          }
        })
    },
    getTrailer : function(title){
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
    }
  },
  created : function(){
    this.$emit('getImgUrl',this.movie.posterSrc)
    this.$emit('getCrew',this.movie.movieCd)
    const code=this.movie.movieCd
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
    axios.get(`${SERVER_URL}/movies/${code}/movie_score_list/`)
      .then((res) => {
        const movieScore = res.data
        this.score = movieScore
        if(localStorage.getItem('jwt')){
          const userSet = this.score.map(a=>a.user)
          const nowUser =this.getUsername()
          const userIdx = userSet.indexOf(nowUser)
          if(userIdx!==-1){
            switch(this.score[userIdx].score){
              case 1 :
                this.btn1=true;
                break;
              case 2 :
                this.btn2=true;
                break;
              case 3 :
                this.btn3=true;
                break;
              case 4 :
                this.btn4=true;
                break;
              case 5 :
                this.btn5=true;
                break;
              default :
                break;
            }
            }          
        }
      })
      .catch((err)=>{
        console.log(err)
      }) 
  },
};
</script>

<style scoped>
#MovieCard {
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
/* .flip-card-front {
  color: white;
} */
.flip-card-back {
  background-color: #fffcf4ef;
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
  font-size: 1rem;
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
/* #modalContent{
  display: flexbox;
  width: 100%;
} */

b-modal{
  width: 80vw;
}
b-button>p{
  font-size: 0.5em;
}
.bgON{
  background: #ffc107;
  color: #212529;
}
.heart{
  background: none;
  border: none;
}
</style>
