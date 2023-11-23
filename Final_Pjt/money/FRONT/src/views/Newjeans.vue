<template>
  <div>
    <h1>뉴진스 짱</h1>
    <carousel :perPageCustom="[[480, 1], [768, 2], [992, 3]]" :autoplay="3000" :loop="true" class="carousel" :wrap-around="true" :breakpoints="breakpoints">
      <pagination></pagination>
      <slide v-for="(box, index) in boxes" :key="index">
        <div class="slide-content">
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
  { title: '슬라이드 1', content: '첫 번째 슬라이드 내용' },
  { title: '슬라이드 2', content: '두 번째 슬라이드 내용' },
  { title: '슬라이드 3', content: '세 번째 슬라이드 내용' },
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
  border: 1px solid #ccc;
  border-radius: 5px;
}
</style>
