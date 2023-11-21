<template>
  <div>
    <div
      :style="{ transform: `translateX(-${currentIndex * 100}%)` }"
      class="carousel"
    >
      <div v-for="(content, index) in contents" :key="index" class="carousel-item">
        <div class="content_auto_box">
          <h1>{{ content }}</h1>
        </div>
      </div>
    </div>
    <button class="arrow left" @click="prevSlide">&#8592; 이전</button>
    <button class="arrow right" @click="nextSlide">다음 &#8594;</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const contents = ['화면 1', '화면 2', '화면 3'];
const currentIndex = ref(0);

onMounted(() => {
  // 5초마다 화면 전환을 위한 setInterval 설정
  setInterval(() => {
    nextSlide();
  }, 5000);
});

const nextSlide = () => {
  currentIndex.value = (currentIndex.value + 1) % contents.length;
};

const prevSlide = () => {
  currentIndex.value = (currentIndex.value - 1 + contents.length) % contents.length;
};
</script>

<style>
.carousel {
  display: flex;
  transition: transform 0.5s ease;
}

.carousel-item {
  flex: 0 0 100%;
}

.arrow {
  font-size: 1.5em;
  margin: 0.5em;
  cursor: pointer;
}

.left {
  float: left;
}

.right {
  float: right;
}

.content_auto_box {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%; /* 부모의 높이를 기준으로 가운데 정렬 */
}

h1 {
  margin: 0; /* 기본 마진 제거 */
}
</style>
