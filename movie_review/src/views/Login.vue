<template>
  <div id="loginPage">
    <Navbar />
    <div id="loginbox">
      <div id="login">
        <div id="h2div" class="pb-0 col-12">
          <h2>LOGIN</h2>
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
              @keypress.enter="login"
              v-model="credentials.password"
              id="input-lazy"
              placeholder="Enter your PASSWORD"
              type="password"
            ></b-form-input>
          </b-form-group>
        </div>
        <div>
          <b-form-group class="mb-0" label-for="input-lazy">
          <b-button @click="login" variant="primary" class="col-12">Login</b-button>
          </b-form-group>
        </div>
        <div class="pt-0">
          <router-link :to="{ name: 'Signup' }">Not Enrolled? Sign Up Now.</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  components: {
    Navbar,
  },
  name: "Login",

  data: function() {
    return {
      credentials: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    login: function() {
      axios.post(`${SERVER_URL}/accounts/api-token-auth/`,this.credentials)
          .then((res)=>{
            localStorage.setItem('jwt',res.data.token)
            this.$store.dispatch('login',true)
            this.$router.push({name:'Main'})
          })
          .catch((err)=>{
            alert(err)
            console.log(err)
          })
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Lato&display=swap");
* {
  font-family: "Lato", sans-serif;
}

#loginPage {
  width: 100vw;
  height: 100vh;
  position: relative;
  display: flexbox;
  background-color: black;
}
#loginPage::before {
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
#loginPage * {
  position: relative;
}

#loginbox {
  display: flex;
  width: 100vw;
  height: 90vh;
  justify-content: center;
  align-items: center;
}
#login {
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
#login > div {
  padding: 3%;
}
a {
  font-size: 80%;
}
#login > :nth-child(1) {
  height: 20%;
}
#login > :nth-child(2) {
  height: 50%;
}
#login > :nth-child(3) {
  height: 15%;
}
#login > :nth-child(4) {
  height: 10%;
}
</style>
