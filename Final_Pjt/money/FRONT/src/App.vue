<template>
  <header v-if="router.currentRoute.value.name != 'MainPageView'">
    <nav class="custom-nav">
      <div class="nav-container">
        <div class="left-links">
          <RouterLink :to="{ name: 'HomeView' }" class="home-link">HOME</RouterLink>
        </div>
        <div class="right-links">
          <RouterLink :to="{ name: 'FinView' }">Fin</RouterLink>
          <RouterLink :to="{ name: 'MapView' }">Map</RouterLink>
          <RouterLink :to="{ name: 'ExchangeRateView' }">ExchangeRate</RouterLink>
          <RouterLink :to="{ name: 'ArticleView' }">Post</RouterLink>
          <!-- <RouterLink :to="{ name: 'Newjeans' }">뉴진스</RouterLink> -->
          <div v-if="store.isLogin" class="profile-section">
            <RouterLink :to="{ name: 'ProfileView', params: { username: store.name } }">프로필</RouterLink>
            <form @submit.prevent="store.logOut" class="logout-form">
              <input type="submit" value="로그아웃" class="logout-button">
            </form>
          </div>
          <div v-else>
            <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink>
            <RouterLink :to="{ name: 'LogInView' }">로그인</RouterLink>
          </div>
        </div>
      </div>
    </nav>
  </header>
  <div v-if="router.currentRoute.value.name != 'MainPageView'">
    <footer class="footer">
      <p>&copy; 2023 My Awesome App <small>SSAFY 10th KIM & LIM</small></p>
    </footer>
  </div>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { useRoute, useRouter } from 'vue-router';
import { useCounterStore } from '@/stores/counter'
import { ref, computed, onMounted } from 'vue'

const route = useRoute()
const router = useRouter()
console.log(router.currentRoute)
console.log(route)
const store = useCounterStore()
onMounted(() => {
  store.name
})

</script>

<style scoped>
header {
  position: sticky;
  /* position: fixed;  */
  top: 0;
  left: 0;
  width: 100%;
  /* z-index: 1000; */
}

.custom-nav {
  background-color: white;
  color: #fff;
  border-bottom: 2px solid #000;
}

.nav-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 60px; 
}

.left-links,
.right-links {
  display: flex;
  align-items: center;
}

.home-link {
  font-size: 1.5em;
  font-weight: bold;
}

.profile-section {
  display: flex;
  align-items: center;
}

.logout-form {
  margin-left: 10px;
}

.logout-button {
  background-color: white;
  color: black;
  border: none;
  padding: 8px 12px;
  cursor: pointer;
  font-size: 0.9em;
}

nav a {
  color: black;
  text-decoration: none;
  padding: 10px;
  transition: transform 0.3s;
  font-size: 0.9em;
}

nav a:hover {
  transform: scale(1.1);
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

.footer small {
  font-size: 0.2em;
  margin-left: 5px;
}

</style>