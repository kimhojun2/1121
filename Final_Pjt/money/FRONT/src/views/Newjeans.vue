<template>
  <div>
    <h1>뉴진스 짱</h1>
    <carousel :perPageCustom="[[480, 1], [768, 2], [992, 3]]" :autoplay="3000" :loop="true" class="carousel" :wrap-around="true" :breakpoints="breakpoints">
      <pagination></pagination>
      <slide v-for="(box, index) in boxes" :key="index">
        <div class="slide-content">
          <img :src="box.src" alt="Carousel Slide">
          <h2>{{ box.title }}</h2>
          <p>{{ box.content }}</p>
        </div>
      </slide>
    </carousel>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import 'vue3-carousel/dist/carousel.css';
import { Carousel, Slide, Pagination } from 'vue3-carousel';

const boxes = ref([
  { title: '금융상품', content: '첫 번째 슬라이드 내용', src: 'https://blog.fint.co.kr/app/uploads/2022/09/%E1%84%91%E1%85%B5%E1%86%AB%E1%84%90%E1%85%B3%E1%84%85%E1%85%A6%E1%84%90%E1%85%A5_220913_%E1%84%8A%E1%85%A5%E1%86%B7%E1%84%82%E1%85%A6%E1%84%8B%E1%85%B5%E1%86%AF.png' },
  { title: '환율', content: '두 번째 슬라이드 내용', src: 'https://blog.fint.co.kr/app/uploads/2022/08/%E1%84%91%E1%85%B5%E1%86%AB%E1%84%90%E1%85%B3%E1%84%85%E1%85%A6%E1%84%90%E1%85%A5_%E1%84%92%E1%85%AA%E1%86%AB%E1%84%8B%E1%85%B2%E1%86%AF1.jpg' },
  { title: '지도', content: '세 번째 슬라이드 내용', src: 'https://blog.fint.co.kr/app/uploads/2023/05/featured.png' },
  // 추가적인 슬라이드 내용을 필요에 따라 배열에 추가
]);
</script>

<style scoped>
.carousel {
  width: 80%;
  margin: 0 auto;
}

.slide-content {
  text-align: center;
  padding: 20px;

}

img {
  width: 600px;
}
</style>
