<template>
    <div id='Recommend'>
        <div>
            <h2>화제의 영화</h2>
        </div>
        <div id ='caru'>
        <b-carousel

        
            id="carousel-1"
            v-model="slide"
            :interval="4000"
            controls
            indicators
            img-width = "300"
            img-height = '700'
            style="text-shadow: 1px 1px 2px #333;"
            @sliding-start="onSlideStart"
            @sliding-end="onSlideEnd"
        >
        <!-- <b-carousel-slide
            caption="First slide"
            img-src="https://picsum.photos/1024/480/?image=52"
        >
        </b-carousel-slide> -->

            <b-carousel-slide>
                <template #img>
                <img

                    fluid
                    class="d-block img-fluid mx-auto my-auto"

                    src="https://picsum.photos/1024/480/?image=55"
                    alt="image slot"
                >
                </template>
            </b-carousel-slide>
            <b-carousel-slide>
                <template #img>
                <img
                    class="d-block img-fluid mx-auto my-auto"
                    src="https://picsum.photos/1024/480/?image=52"
                    alt="image slot"
                >
                </template>
            </b-carousel-slide>
            <!-- <b-carousel-slide>
                <template #img>
                <img
                    class="d-block img-fluid"
                    src="https://picsum.photos/1024/480/?image=54"
                    alt="image slot"
                >
                </template>
            </b-carousel-slide>
            <b-carousel-slide>
                <template #img>
                <img
                    class="d-block img-fluid"
                    src="https://picsum.photos/1024/480/?image=58"
                    alt="image slot"
                >
                </template>
            </b-carousel-slide> -->

        </b-carousel>
        </div>
    </div>
</template>

<script>
export default {
    name : 'Recommended',
    data : function() {
        return {
            slide: 0,
            sliding: null
        }
    },
    methods: {
        onSlideStart() {
        this.sliding = true
        },
        onSlideEnd() {
        this.sliding = false
        }
    }
}
</script>
<style scoped>
#Recommend{
    margin: 2em 0;
}

h2{
    color: white;
    text-align: center;
    text-decoration-line: underline;

}
#caru{
    margin: 3% 0;
}

b-carousel-slide>template>img{
    width : 30vw;
    height : 50vh;
}
</style>