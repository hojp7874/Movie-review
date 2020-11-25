<template>
  <div id='genreMovie'>
    <b-button-group size="sm" @click="click(genresBtn)">
      <b-button
        v-for="(btn, idx) in genresBtn"
        :key="idx"
        :pressed.sync="btn.state"
        variant="primary"
        :class="{clicked:btn.state}"
      >
        {{ btn.caption }}
      </b-button>
    </b-button-group>
    <div>{{btnStates}}</div>
  </div>
</template>

<script>
export default {
  name : 'GenreMovie',
  computed : {
    genresBtn : {
      get(){
      let lst = []
      this.$store.state.genres.forEach((genre)=>{
        lst.push({caption : genre, state : false})
      })
      return lst
      },
      set(){

      }
    },
    btnStates : {
      get(){
        return this.genresBtn.map(btn => btn.state)
      },
      set(){
        
      }
    }
  },
  methods :{
    click : function(data){
      this.genresBtn = data
    }
  }
}
</script>

<style>
.clicked{
  background: #005cbf;;
}
</style>

