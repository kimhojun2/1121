<template>
    <header v-if="router.currentRoute.value.name != 'MainPageView'">
      <nav v-if="store.isLogin">
        <div class="nav-container">
              <RouterLink :to="{ name: 'HomeView' }">HOME</RouterLink>
              <RouterLink :to="{ name: 'FinView' }">Fin</RouterLink>
              <RouterLink :to="{ name: 'MapView' }">Map</RouterLink>
              <RouterLink :to="{ name: 'ExchangeRateView' }">ExchangeRate</RouterLink>
              <RouterLink :to="{ name: 'PostView' }">Posts</RouterLink>
              <RouterLink :to="{ name: 'Newjeans' }">뉴진스</RouterLink>
              <form @submit.prevent="store.logOut">
                <input type="submit" value="logOut">
              </form>
          </div>
        </nav>
      <nav v-else>
        <div class="nav-container">
          <RouterLink :to="{ name: 'SignUpView' }">SignUp</RouterLink>
          <RouterLink :to="{ name: 'LogInView' }">LogIn</RouterLink>
        </div>
    </nav>
  </header>
  <div v-if="router.currentRoute.value.name != 'MainPageView'">
    <footer class="footer">
      <!-- 여기에 footer 내용 추가 -->
      <p>&copy; 2023 My Awesome App <small>Sapphi 10th KIM & LIM</small></p>
    </footer>
  </div>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute()
const router = useRouter()
console.log(router.currentRoute)
console.log(route)
</script>

<style scoped>
/* 스타일링 추가 */
nav {
  background-color: #333;
  color: #fff;
}

.nav-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%; /* 높이를 100%로 설정하여 내용을 세로로 가운데 정렬 */
}

nav a {
  color: #fff;
  text-decoration: none;
  padding: 10px;
  transition: transform 0.3s; /* transition 속성을 추가하여 변환 효과를 부드럽게 만듭니다 */
  margin-right: 100px; /* 각 항목 사이의 오른쪽 마진을 조절합니다 */
}

nav a:hover {
  background-color: #555;
  transform: scale(1.1); /* hover 시에 스케일을 1.1로 확대합니다 */
}

.footer {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: #333;
  color: #fff;
  padding: 10px;
  text-align: center;
}

/* 푸터 내의 small 태그에 대한 스타일 */
.footer small {
  font-size: 0.2em; /* 조그맣게 만듭니다. */
  margin-left: 5px; /* Copy 텍스트와 원래 텍스트 사이의 여백을 조절합니다. */
}
</style>

