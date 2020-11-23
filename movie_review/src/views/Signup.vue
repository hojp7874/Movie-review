<template>
  <div id="SingupPage">
    <Navbar />
    <div id="Singupbox">
      <div id="Singup">
        <div id="h2div" class="pb-0 col-12">
          <h2>WELCOME</h2>
        </div>
        <div>
          <b-form-group
            class="mb-0"
            label="USER ID"
            label-for="input-formatter"
          >
            <b-form-input
              v-model="credentials.username"
              id="input-formatter"
              placeholder="Enter your ID"
            ></b-form-input>
          </b-form-group>

          <b-form-group class="mb-0" label="PASSWORD" label-for="input-lazy">
            <b-form-input
              id="input-lazy"
              v-model="credentials.password"
              placeholder="Enter your Password"
              type="password"
            ></b-form-input>
          </b-form-group>
          <b-form-group class="mb-0" label="CONFIRM PASSWORD" label-for="input-lazy">
            <b-form-input
              id="input-lazy"
              v-model="credentials.passwordConfirmation"
              @keypress.enter="signup"
              placeholder="Type Your Password Again"
              type="password"
            ></b-form-input>
          </b-form-group>
        </div>
        <div>
          <b-button @click='signup' variant="primary" class="col-12">Sign Up!</b-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import axios from 'axios'

// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Singup',
  components : {
    Navbar
  },
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        passwordConfirmation: '',
      }
    }
  },
  methods: {
    signup: function () {
      // axios.post(`${SERVER_URL}/accounts/signup/`, this.credentials)
      axios.post(`http://127.0.0.1:8000/accounts/signup/`, this.credentials)
        .then((res) => {
          console.log(res)
          this.$router.push({ name: 'Login' })
          alert('회원가입이 완료되었습니다!!')
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Lato&display=swap");
* {
  font-family: "Lato", sans-serif;
}

#SingupPage {
  width: 100vw;
  height: 100vh;
  position: relative;
  display: flexbox;
}
#SingupPage::before {
  width: 100%;
  height: 100%;
  content: "";
  background-image: url("~@/assets/login.jpg");
  background-size: cover;
  opacity: 0.3;
  position: absolute;
  top: 0px;
  bottom: 0px;
  left: 0px;
  right: 0px;
}
#SingupPage * {
  position: relative;
}

#Singupbox {
  display: flex;
  width: 100vw;
  height: 90vh;
  justify-content: center;
  align-items: center;
}
#Singup {
  width: 25vw;
  height: 50vh;
  background-color: white;
  border: 0px;
  border-radius: 1%;
}
b-form-input::placeholder {
  padding: 1%;
  font-size: 50%;
}
h2 {
  text-align: center;
  margin: 0;
  padding: 5%;
  font-weight: bold;
  color: black;
}
label {
  margin: 2%;
}
#Singup > div {
  padding: 3%;
}
a {
  font-size: 80%;
}
#Singup > :nth-child(1) {
  height: 20%;
}
#Singup > :nth-child(2) {
  height: 50%;
}
#Singup > :nth-child(3) {
  height: 15%;
}
#Singup > :nth-child(4) {
  height: 10%;
}
</style>
