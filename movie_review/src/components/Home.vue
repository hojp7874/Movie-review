<template>
    <div id='Home'>
        <div id='login'>
            <button @click='nonLogin'>비로그인</button>
            <button @click='showModal = true'>로그인</button>
        </div>
        <transition name='fade' appear>
            <div class='modal-overlay' v-if="showModal" @click='showModal = false'></div>
        </transition>
        <transition name='slide' appear>
            <div class="modal" v-if="showModal">
                <Login />
            </div>
        </transition>
    </div>
</template>

<script>
import Login from '@/components/Login.vue'

export default {
    name : 'Home',
    data : function(){
        return {
            mainLink:'',
            showModal : false,
        }
    },
    components :{
        Login,
    }
    ,
    methods : {
        nonLogin : function(){
            const answer = confirm('비로그인시 서비스에 제한이 있습니다. 비로그인으로 계속 하시겠습니까?')
            if(answer){
                this.$router.push({name : 'Main'})
            }else{
                this.$router.go({name : 'Home'})
            }
        },
        Login : function(){
            this.hide = false
        }
    }
}
</script>

<style scoped>
/* @import url('@/assets/bgi.jpg'); */
*{
    margin: 0;
    padding: 0;
}

#Home{
    background-image: url('~@/assets/222.gif');
    width: 100vw;
    height: 100vh;
    background-size: cover;
    opacity: 0.9;
    display: flex;
    justify-content: center;
    align-items: center;

    overflow: hidden;
}
#login{
    width: 30%;
    height: 30%;
    margin: auto
}
button{
    font-size: 1rem;
    border-radius: 8px;
    box-shadow : 3px 3px rgba(0, 0, 0, 0.4);
    transition : 0.4s ease-out;

    &:hover {
        box-shadow: rgba(0,0,0,0.6);
    }
}
.modal-overlay{
    position:absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 98;
    background-color: rgba(0, 0, 0, 0.3)
}
.modal{
    position: fixed;
    top: 50%;
    left: 50%;
    transform : translate(-50%,-50%);
    z-index: 99;
    width: 30%;
    height : 50%;
    max-width: 400px;
    background-color: #FFF;
    padding: 25px;

}

.fade-enter-active,
.fade-leave-active{
    transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to{
    opacity: 0;
}

.slide-enter-active,
.slide-leave-active{
    transition: transform 0.5s;
}
.slide-enter,
.slide-leave-to{
    /* transform: translateY(-50%) translateX(100vw); */
    opacity: 0
}


</style>