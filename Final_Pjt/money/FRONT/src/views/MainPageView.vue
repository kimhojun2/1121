<template>
    <div class="center-container">
      <RouterLink to="HomeView" class="start-button">시작하기</RouterLink>
    </div>
    <video ref="backgroundVideo" class="fullscreen-video" muted loop autoplay>
        <source src="@/assets/money.mp4" type="video/mp4">
    </video>
  </template>
  
  <script setup>
  import { RouterLink, RouterView } from 'vue-router'
  </script>
  
  <style scoped>
 .center-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.start-button {
  padding: 10px 20px;
  font-size: 40px;
 
  color: #ecf0f1; /* 글자색 변경 */
  text-decoration: none;
  border-radius: 5px;
  border: none; 
  transition: background-color 0.3s;
}

.start-button:hover {
  background-color: #34495e; /* hover 시 어두운 색으로 변경 */
}

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
  