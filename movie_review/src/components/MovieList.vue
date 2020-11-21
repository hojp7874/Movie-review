<template>
    <div id='app'>
        <div class="m-3">
            <h2>모든 영화</h2>
        </div>
        <div class='flip-card-container col-2 p-0'>
            <div class="flip-card">
                <div class="flip-card-front">
                    <img src="https://news.kbs.co.kr/data/news/2019/11/20/4327665_Fe2.jpg" alt="">
                </div>
                <div class="flip-card-back">
                    <p>this is back</p>
                </div>
            </div>
        </div>
    </div>    
</template>

<script>
export default {
    name : 'MovieList',
    methods : {
        msOver : function(){
            
        }
    }
}
</script>

<style scoped>
#app{
    background-color: #323437;
    width: 100vw;
    height:100vh;
}
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
.flip-card-container{
    width: 100vw;
    height: 30vh;
    border-radius: 0.5rem;
}
.flip-card-container:hover .flip-card{
    transform: rotateY(180deg);
}
.flip-card{
    position: relative;
    width: 100%;
    height: 100%;
    transform-style: preserve-3d;
    transition: transform 1s;
}
.flip-card-front, .flip-card-back{
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    position: absolute;
    border-radius: 0.5rem;
}
.flip-car-front{
    background-color: #333;
    color: white;
}
.flip-card-back{
    background-color: darkgray;
    color: white;
    transform: rotateY(180deg);
}
.flip-card-front img{
    width: 100%;
    height : 100%;
    border-radius: 0.5rem;
}
h2{
    text-align: center;
    color: White;
    text-decoration: underline;
}
.flip-card-back p{
    color: white;
    text-align: center;
}
</style>