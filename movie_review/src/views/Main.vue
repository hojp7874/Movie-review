<template>
    <div>
        <Navbar />
        <br>
        <Recommended />
    </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
import Recommended from '@/components/Recommended.vue'


export default {
    name :'Main',
    components : {
        Navbar,
        Recommended
    }
}
</script>

<style>

</style>