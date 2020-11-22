<template>
  <div id="Recommend">
    <div>
      <h2>화제의 영화</h2>
    </div>
    <div id="caru">
      <b-carousel
        id="carousel-1"
        v-model="slide"
        :interval="4000"
        controls
        indicators
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
          <template v-slot:img>
            <div class="flip-card-container col-3 p-0">
              <div class="flip-card">
                <div class="flip-card-front">
                  <img
                    src="https://news.kbs.co.kr/data/news/2019/11/20/4327665_Fe2.jpg"
                    class="d-block img-fluid mx-auto my-auto"
                    alt=""
                  />
                </div>
                <div class="flip-card-back">
                  <p>this is back</p>
                </div>
              </div>
            </div>
          </template>
        </b-carousel-slide>
        <b-carousel-slide>
          <template v-slot:img>
            <div class="flip-card-container col-3 p-0">
              <div class="flip-card">
                <div class="flip-card-front">
                  <img
                    src="https://picsum.photos/1024/480/?image=52"
                    class="d-block img-fluid mx-auto my-auto"
                    alt=""
                  />
                </div>
                <div class="flip-card-back">
                  <p>this is back</p>
                </div>
              </div>
            </div>
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
  name: "Recommended",
  data: function() {
    return {
      slide: 0,
      sliding: null,
    };
  },
  methods: {
    onSlideStart() {
      this.sliding = true;
    },
    onSlideEnd() {
      this.sliding = false;
    },
  },
};
</script>
<style scoped>
#Recommend {
  margin: 2em 0;
}

h2 {
  color: white;
  text-align: center;
  text-decoration-line: underline;
}
#caru {
  margin: 3% 0;
}

b-carousel-slide {
  border-radius: 0.5rem;
}
.flip-card-container {
  width: 100vw;
  height: 30vh;
  border-radius: 0.5rem;
}
.flip-card-container:hover .flip-card {
  transform: rotateY(180deg);
}
.flip-card {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform 1s;
}
.flip-card-front,
.flip-card-back {
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  position: absolute;
  border-radius: 0.5rem;
}
.flip-car-front {
  background-color: #333;
  color: white;
}
.flip-card-back {
  background-color: darkgray;
  color: white;
  transform: rotateY(180deg);
}
.flip-card-front img {
  width: 100%;
  height: 100%;
  border-radius: 0.5rem;
}
.flip-card-back p {
  color: white;
  text-align: center;
}

.carousel-indicators {
  margin-top: 50%;
}
#caru > div > div > div > div {
  left: 38vw;
}
</style>
