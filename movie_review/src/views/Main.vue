<template>
    <div id='app'>
        <Navbar />
        <br>
        <Recommended />
        <div class='blankblock'></div>
        <MovieList />
    </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
import Recommended from '@/components/Recommended.vue'
import MovieList from '@/components/MovieList.vue'

export default {
    name :'Main',
    components : {
        Navbar,
        Recommended,
        MovieList
    }
}
</script>

<style scoped>
#app{
    background-color: #323437;
    width: 100vw;
    height:100vh;
}
.blankblock{
    height: 10vh;
}
</style>