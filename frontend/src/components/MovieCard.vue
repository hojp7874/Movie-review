<template>
  <b-col xs="12" sm="6" md="4" lg="3" xl="2" id="MovieCard">
  <!-- <div id="MovieCard" class='col-2'> -->
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
          <p>{{ movie.genreAlt }} |{{movie.nationAlt}}</p>
          <p>{{movie.openDt}} {{movie.prdtStatNm}}</p>
          <p>평점: {{stars[1]}}</p>
          <!-- <p>{{score.length}}개의 점수 평가</p> -->
          <p>리뷰 {{Object.keys(reviews).length}}개</p>
          <br>
          <p>[총점]</p>
          <p><b-icon icon="emoji-angry" style="color : brown"></b-icon><span> : {{stars[2]}}</span></p>
          <p><b-icon icon="emoji-frown" style="color : brown"></b-icon><span> : {{stars[3]}}</span></p>
          <p><b-icon icon="emoji-neutral" style="color : brown"></b-icon><span> : {{stars[4]}}</span></p>
          <p><b-icon icon="emoji-smile" style="color : brown"></b-icon><span> : {{stars[5]}}</span></p>
          <p><b-icon icon="emoji-heart-eyes" style="color : brown"></b-icon><span> : {{stars[6]}}</span></p>
        </div>
        <b-modal :id="'bv-modal-'+idx" hide-footer size='xl'>
          <template #modal-title>
            <div class='txtcenter'>{{ movie.movieNm }}  <span style="color :#c7b800;">{{stars[1]}}</span></div>
          </template>
          <div class="d-block">
            <div id='modalContent'>
              <div>
                <div class='mb-4'><p style='font-weight : 600; font-size:150%;'>영화 예고편</p></div>
                <iframe :src="mvUrl" frameborder="0" width=100% height='470' allowfullscreen></iframe>
              </div><hr class="my-3">
              <div class="container d-flex flex-column">
                <div class="d-flex flex-row flex-wrap">
                  <div class="col-3 text-center">
                    <p class="mb-1">
                      <span style='font-weight : 600;'> {{ movie.genreAlt }} | {{movie.nationAlt}}</span>
                      <span style='font-weight : 600;'> {{movie.prtdYear}}</span>
                    </p>
                    <img v-if="!movie.posterSrc" src="https://1080motion.com/wp-content/uploads/2018/06/NoImageFound.jpg.png" alt="">
                    <img v-else :src="movie.posterSrc" alt="">
                    <!-- <title>{{ movie.movieNm }}</title> -->
                  </div>
                  <div class="col-lg-9 col-12 d-flex flex-column">
                    <p class="mb-1 " style='font-weight : 600; font-size:150%;'>영화 줄거리</p>
                    <span class="flex-fill d-flex flex-row">
                      <p class="align-self-center">
                        {{movie.story}}
                      </p>
                    </span>
                  </div>
                </div><hr class="my-3">
                <div class='mb-4 txtcenter'><span style=''>제작진</span></div>
                <div class="container d-flex flex-row flex-wrap">
                  <div
                    v-for="(person, idx) in movie.peoples"
                    :key="idx"
                    :person='person'
                    class="col-3"
                  >
                    <div>
                      <span style='font-weight : 600'>{{person.name}} </span>
                      <span v-if="person.role=='감독'" style='font-weight : 600'>({{person.role}})</span>
                    </div>
                    <img class="w-75" v-if="person.photo!=='이미지 없음'" :src="person.photo" alt="">
                    <img class="w-75" v-else src="https://1080motion.com/wp-content/uploads/2018/06/NoImageFound.jpg.png" alt="">
                  </div>
                </div><hr class="my-3">
                <!-- 리뷰작성 -->
                <div class="d-flex justify-content-between align-items-center">
                  <b-button v-b-toggle.collapse-3 variant="outline-dark" class="m-1">리뷰 작성</b-button>
                  <span>
                    <b>이 영화에 대한 평점을 남겨주세요 :  </b>
                    <b-button-group>
                      <b-button :class="{bgON : btn1}" @click='scoreSelect(movie.movieCd,1)' variant="outline-danger">
                        <b-icon icon="emoji-angry"></b-icon>
                        <!-- <p>최악이에요!</p> -->
                      </b-button>
                      <b-button :class="{bgON : btn2}" @click='scoreSelect(movie.movieCd,2)' variant="outline-danger">
                        <b-icon icon="emoji-frown"></b-icon>
                        <!-- <p>그저 그래요</p> -->
                      </b-button>
                      <b-button :class="{bgON : btn3}" @click='scoreSelect(movie.movieCd,3)' variant="outline-danger">
                        <b-icon icon="emoji-neutral"></b-icon>
                        <!-- <p>볼만해요</p> -->
                      </b-button>
                      <b-button :class="{bgON : btn4}" @click='scoreSelect(movie.movieCd,4)' variant="outline-danger">
                        <b-icon icon="emoji-smile"></b-icon>
                        <!-- <p>재밌어요</p> -->
                      </b-button>
                      <b-button :class="{bgON : btn5}" @click='scoreSelect(movie.movieCd,5)' variant="outline-danger">
                        <b-icon icon="emoji-heart-eyes"></b-icon>
                        <!-- <p>최고에요!</p> -->
                      </b-button>
                    </b-button-group>
                  </span>
                </div>
              </div>
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
                      <div class='d-flex justify-content-end'>
                        <b-button variant="outline-dark" class='mybtn'  @click='makeReview(movie.movieCd)' type="submit">리뷰쓰기</b-button>
                      </div>
                    </div>
                  </form>
                </b-card>
              </b-collapse>
              <hr>
              <div class='mt-4'>
                <p class='txtcenter m-4'>리뷰 목록</p>
              </div>
              <ul>
                <li
                  v-for=" (review,idxx) in reviews"
                  :key='idxx'
                  :review='review'
                >
                  <hr>
                  <b-card-body v-b-toggle="'collapse-' + idxx" class=" p-2 d-flex flex-row justify-content-between reviewHover">

                    <b><span> 글 제목 : </span>{{review.title}}</b>
                    <!-- <p>작성자 : {{review.user.username}}</p> -->
                    <small style="text-align: right">{{review.like_users.length}}명이 좋아합니다.</small>
                  </b-card-body>
                  <b-collapse :id="'collapse-'+idxx" class="mt-2">
                    <b-card>
                      <div class="d-flex justify-content-between">
                        <p><span style='font-weight :600;'>작성자 </span>: {{review.user.username}}</p>
                        <div v-if="review.like_users.includes(nowUser)"><button class='heartbutton' @click='reviewLike(review,false)' ><b-icon icon="heart-fill" style="color : red"></b-icon></button></div>
                        <div v-else><button class='heartbutton' @click='reviewLike(review,true)'><b-icon icon="heart" style="color : red"></b-icon></button></div>
                      </div>
                      <p><span style='font-weight :600;'>내용</span>: {{review.content}}</p>
                    </b-card>
                  </b-collapse>
                  <hr>
                </li>
              </ul>
            </div>
          </div>
          <b-button variant="secondary" class="mt-3" block @click="$bvModal.hide(`bv-modal-${idx}`)">닫기</b-button>
        </b-modal>
      </div>
    </div>
  </b-col>
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
        score :[],
        reviewTitle:'',
        reviewContent : '',
        btn1:false,
        btn2:false,
        btn3:false,
        btn4:false,
        btn5:false,
        reviews:[],
      }
  },
  computed:{
    ...mapState([
      'crew',
      'users',
    ]),
    stars : function(){
      if(!this.score.length){
        return [0.00, '☆'.repeat(5),0,0,0,0,0]
      }else{
        const n = Object.keys(this.score).length
        let stack =0
        this.score.forEach(function(sc){stack+=sc.score})
        let list1 = this.score.filter((sc)=> sc.score===1).length
        let list2 = this.score.filter((sc)=> sc.score===2).length
        let list3 = this.score.filter((sc)=> sc.score===3).length
        let list4 = this.score.filter((sc)=> sc.score===4).length
        let list5 = this.score.filter((sc)=> sc.score===5).length
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
            axios.delete(`${SERVER_URL}/movies/${code}/score`,{headers : {Authorization: this.setToken().headers.Authorization},data : {movie : code, score : scoreList[scoreIdx], user: user2}})
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
            axios.put(`${SERVER_URL}/movies/${code}/score`, item, config)
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
          axios.post(`${SERVER_URL}/movies/${code}/score`,item, config)
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
      }else{
          const config = this.setToken()
          // VueJwtDecode.decode(localStorage.getItem('jwt'))
          const user2 =this.getUsername()
          const item = {
            movie: code,
            title : this.reviewTitle,
            content : this.reviewContent,
            user : {username : user2}
          }
          const data = [item,config]
          this.$store.dispatch('makeReview',data)
          this.getReview(code)
      }
      this.reviewContent=''
      this.reviewTitle=''
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
    },
    getReview : function(code){
      axios.get(`${SERVER_URL}/movies/${code}/review_list/`)
        .then((res) => {
          if(res.data=== []){
            this.reviews=[]
          }else{
            this.reviews=res.data
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
    let code=this.movie.movieCd
    this.getReview(code)
    axios.get(`${SERVER_URL}/movies/${code}/score`)
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
  background-color: rgba(255, 255, 255, 0);

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
.flip-card-back:hover{
  border: #212121 1px solid;
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
  background: #d50000;
  color:white;
}
.heart{
  background: none;
  border: none;
}
.heartbutton{
  border: none;
  background: none;
}
.txtcenter{
  text-align: center;
  font-weight : 600;
  font-size:150%;
}
ul{
  list-style: none;
}
.mybtn:hover{
  background: none;
  color : black;
}
.reviewHover:hover{
  background: #fffde7;
}
</style>
