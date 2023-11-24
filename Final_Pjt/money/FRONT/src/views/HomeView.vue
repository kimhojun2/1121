<template>
  <div class="container">
    <div class="section">
      <carousel :perPageCustom="[[480, 1], [768, 2], [992, 3]]" :autoplay="3000" :loop="true" class="carousel" :wrap-around="true">
      <slide v-for="(box, index) in boxes" :key="index">
        <div class="slide-content">
          <img :src="box.src" alt="Carousel Slide">
          <h2>{{ box.title }}</h2>
        </div>
      </slide>
    </carousel>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import 'vue3-carousel/dist/carousel.css';
import { Carousel, Slide, Pagination } from 'vue3-carousel';

const boxes = ref([
  { title: '금융상품', content: '첫 번째 슬라이드 내용', src: 'https://blog.fint.co.kr/app/uploads/2023/05/featured.png' },
  { title: '환율', content: '두 번째 슬라이드 내용', src: 'https://blog.fint.co.kr/app/uploads/2022/08/%E1%84%91%E1%85%B5%E1%86%AB%E1%84%90%E1%85%B3%E1%84%85%E1%85%A6%E1%84%90%E1%85%A5_%E1%84%92%E1%85%AA%E1%86%AB%E1%84%8B%E1%85%B2%E1%86%AF1.jpg' },
  { title: '은행검색', content: '세 번째 슬라이드 내용', src: 'https://blog.fint.co.kr/app/uploads/2022/09/%E1%84%91%E1%85%B5%E1%86%AB%E1%84%90%E1%85%B3%E1%84%85%E1%85%A6%E1%84%90%E1%85%A5_220913_%E1%84%8A%E1%85%A5%E1%86%B7%E1%84%82%E1%85%A6%E1%84%8B%E1%85%B5%E1%86%AF.png' },
  // 추가적인 슬라이드 내용을 필요에 따라 배열에 추가
]);
</script>


<style scoped>
.container {
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.section {
  margin-top: 5rem;
  flex: 1;
}

.image {
  max-width: 100%; /* 이미지의 최대 너비를 부모 요소의 크기에 맞게 조절 */
  max-height: 100%; /* 이미지의 최대 높이를 부모 요소의 크기에 맞게 조절 */
  height: auto; /* 가로 비율에 맞게 자동 조절 */
}

.section2_box {
  max-width: 30%;
  margin: 300px auto; /* 가운데 정렬을 위한 margin 설정 */
  text-align: left; /* 텍스트를 왼쪽 정렬로 설정 */
}

.section3_box {
  max-width: 50%; /* 이미지의 최대 너비를 지정 (필요에 따라 조절) */
  margin: 0 auto; /* 가운데 정렬을 위한 margin 설정 */
  padding-left: 200px;
}

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
