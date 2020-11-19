<template>
    <div>
        <h1>LOGIN</h1>
        <div>
            <label for="username">사용자 아이디</label>
            <input type="text" id='username' v-model="credentials.username">
        </div>
        <div>
        <label for="password">비밀번호</label>
            <input
            type="password"
            id='password'
            v-model="credentials.password"
            @keypress.enter ='login'
            >
        </div>
        <button @click='login'>로그인</button>
    </div>
</template>

<script>
// import axios from 'axios'

// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
    name: 'Login',
    data: function () {
    return {
        credentials:{
            username:'',
            password:'',
        }      
    }
    },
    methods: {
        login: function () {
            this.$router.push({name:'Main'})
        // axios.post(`${SERVER_URL}/accounts/api-token-auth/`,this.credentials)
        //     .then((res)=>{
        //         localStorage.setItem('jwt',res.data.token)
        //         this.$emit('login')
        //         this.$router.push({name:'Main'})
        //     })
        //     .catch((err)=>{
        //         console.log(err)
        //     })
        }
    }
}
</script>

<style>

</style> 