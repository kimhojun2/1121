<template>
    <div>
      <!-- 다른 컨텐츠를 추가할 수 있습니다 -->
      <div class="content">
        <h1>My Awesome Website</h1>
        <p>Some content here...</p>
      </div>
  
      <!-- 비디오 요소를 추가하고 소스를 지정합니다 -->
      <!-- <video ref="backgroundVideo" class="fullscreen-video" muted loop autoplay>
        <source src="@/assets/myVideo.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video> -->
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  
  const backgroundVideo = ref(null);
  </script>
  
  <style scoped>
  /* 전체 화면으로 비디오를 확장하도록 스타일링 */
  .fullscreen-video {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover; /* 비디오 비율 유지 및 전체 화면 채우기 */
    z-index: -1; /* 다른 컨텐츠 위로 올리기 위해 z-index를 설정합니다 */
  }
  
  .content {
    position: relative; /* 다른 컨텐츠를 위치시키기 위해 position을 설정합니다 */
    z-index: 1; /* 비디오 뒤로 이동시키기 위해 z-index를 설정합니다 */
    color: #fff; /* 다른 컨텐츠의 텍스트 색상 설정 (예시) */
  }
  </style>
  