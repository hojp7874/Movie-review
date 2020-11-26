<template>
  <div id="Home">
    <div id="text">
      <p id='ant2'>늑대와 개미핥기</p>
      <h5>영화를 주제로 </h5>
      <h5>사람들과 소통할 수 있는 페이지입니다.</h5>
      <transition name="fade">
        <b-button
          variant="outline-white"
          @click="clicked = !clicked"
          v-if="!clicked"
          >View More</b-button
        >
        <div v-else id="btndiv">
          <b-button class="mx-2" variant="outline-white" @click="selectGuest"
            >Guest</b-button
          >
          <b-button class="mx-2" variant="outline-white" @click="selectLogin"
            >Login</b-button
          >
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
  data: function() {
    return {
      clicked: false,
    };
  },
  components: {},
  methods: {
    selectGuest: function() {
      const answer = confirm(
        "비로그인시 서비스가 제한됩니다. 비로그인으로 계속하시겠습니까?"
      );
      if (answer) {
        this.$router.push({ name: "Main" });
      } else {
        this.$router.go({ name: "Home" });
      }
    },
    selectLogin: function() {
      this.$router.push({ name: "Login" });
    },
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=East+Sea+Dokdo&display=swap');
/* @import url('@/assets/bgi.jpg'); */
* {
  margin: 0;
  padding: 0;
}

.fade-enter-active {
  transition: opacity 1s;
}
.fade-leave-active {
  transition: opacity 0s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}

#Home {
  background-image: url("~@/assets/222.gif");
  width: 100vw;
  height: 100vh;
  background-size: cover;
  display: flexbox;
  justify-content: center;
  align-items: center;

  overflow: hidden;
}
#text {
  position: absolute;
  top: 45%;
  right: 15%;
  background: none;
}
#btndiv {
  background: none;
}

* {
  color: white;
}
button {
  color: white;
  border: 1px solid white;
}
h1 {
  margin: 2rem 0;
}
button {
  margin: 2rem 0;

}
button:hover {
  background: white;
  color: black;
}
#ant2{
  font-family: 'East Sea Dokdo', cursive;
  color: white;
  font-size: 5rem;
}
</style>
