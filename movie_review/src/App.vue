<template>
  <div id="app">
    <h1>check app</h1>
    <Home />
    <!-- <router-link :to="{ name: 'Main' }"></router-link> -->
  </div>
</template>

<script>
import Home from '@/components/Home.vue'
export default {
  name : 'App',
  components : {
    Home
  }
}
</script>


<style>

</style>
