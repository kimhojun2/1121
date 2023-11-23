<template>
  <div class="profile-container">
    
    <div v-if="isLoading" class="loading">Loading...</div>
    <div v-else>
      <div style="text-align: center; font-size: 30px; margin-bottom: 15px;"><strong>MY PROFILE</strong></div>
      <div class="profile-box" style="height: 140px; display: flex; justify-content: center; align-items: center;">
        <div>
        <span style="font-size: 20px;"><strong>{{ info.username }}</strong></span> 님의 회원 등급은 <span style="font-size: 20px;"><strong>FAMILY</strong></span> 입니다. <br>
            <!-- 수정 폼 -->
            <form v-if="isEditMode" @submit.prevent="submitForm">
        <label for="money">Money:</label>
        <input id="money" v-model="editedInfo.money" />

        <label for="salary">Salary:</label>
        <input id="salary" v-model="editedInfo.salary" />

        <label for="age">Age:</label>
        <input id="age" v-model="editedInfo.age" />

        <button type="submit">Save</button>
        <button @click="cancelEditMode">Cancel</button>
      </form>
      
      </div>
    </div>
    <!-- 수정 버튼 -->
    <button v-if="!isEditMode" @click="toggleEditMode">Edit Profile</button>
        <div class="info-container">
          <div>
          <div class="info-item">
            <strong>자산내역 : </strong> {{ info.money }}
          </div>
          <div class="info-item">
            <strong>소득 : </strong> {{ info.salary }}
          </div>
          <div class="info-item">
            <strong>나이 :</strong> {{ info.age }}
            <hr>
          </div>
        </div>
      <div>
          <div v-if="info.financial_products" class="info-item">
            <strong>가입 상품</strong>
            <div v-for="product in info.financial_products.split(',')" :key="product">
              <span class="product"> {{ product.trim() }}</span>
            </div>
          </div>
        </div>
        </div>
      


      <div class="recommended-products">
      <h1>추천상품</h1>
        <div v-for="recopro in recommendlist.recommended_products">
          {{ recopro }}
          <!-- {{ recommendlist.recommended_products }} -->

        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const info = ref(null)
const editedInfo = ref({
  money: 0,
  salary: 0,
  age: 0,
  financial_products: '',
})
const isEditMode = ref(false)
const isLoading = ref(true)
const recommendlist = ref([])



const toggleEditMode = () => {
  isEditMode.value = !isEditMode.value
  if (isEditMode.value) {
    // 수정 모드로 들어갈 때, 현재 정보를 복사하여 폼에 반영
    editedInfo.value = { ...info.value }
  }
}

const submitForm = () => {
  // 수정된 정보를 서버에 보내고, 응답을 받아서 처리하는 로직 추가
  axios({
    method: 'put',
    url: `${store.API_URL}/profile/accounts/profile_edit/${route.params.username}/`,
    data: editedInfo.value,
  })
    .then((res) => {
      // 서버 응답을 처리하거나, 필요하다면 상태를 업데이트할 수 있음
      // 여기에서는 간단히 수정 모드를 종료
      console.log(res)
      isEditMode.value = false
      axios({
    method: 'get',
    url: `${store.API_URL}/profile/accounts/${route.params.username}/`,
  })
    .then((res) => {
      info.value = res.data
    })
    .catch((err) => console.log(err))
    .finally(() => {
      isLoading.value = false
    })
      
    })
    .catch((err) => {
      // 서버 요청이 실패할 경우 처리
      console.error(err)
    })
}

const cancelEditMode = () => {
  // 수정 취소 시, 수정 폼을 닫고 수정된 데이터를 초기화
  isEditMode.value = false
  editedInfo.value = { ...info.value }
}

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/profile/accounts/${route.params.username}/`,
  })
    .then((res) => {
      info.value = res.data
    })
    .catch((err) => console.log(err))
    .finally(() => {
      isLoading.value = false
    })
    axios({
    method: 'get',
    url: `${store.API_URL}/profile/recommend/${store.name}/`,
  })
    .then((res) => {
      recommendlist.value = res.data
      console.log(res.data.recommended_products)
    })
    .catch((err) => console.log(err))
    .finally(() => {
      isLoading.value = false
    })


})


</script>

<style scoped>
/* 프로필 상자 */
.profile-box {
  display: flex;
  width: 790px;
  border: 2px solid black;
  background-color: lightgray; /* 색상 추가 */
  font-family: 'Noto Sans KR', sans-serif; /* Google Fonts에서 가져온 글꼴 */
  padding: 15px;
}

/* 정보 컨테이너 */
.info-container {
  width: 800px;
  margin-top: 40px;
  padding: 10px;
  border: 2px solid black;
  text-align: center;
  background-color: lightgray; /* 색상 추가 */
  font-family: 'Noto Sans KR', sans-serif; /* Google Fonts에서 가져온 글꼴 */
}

/* 추천 상품 */
.recommended-products {
  margin-top: 60px;
  width: 800px;
  padding: 10px;
  border: 2px solid black;
  text-align: center;
  background-color: lightgray; /* 색상 추가 */
  font-family: 'Noto Sans KR', sans-serif; /* Google Fonts에서 가져온 글꼴 */
}

/* 프로필 컨테이너 */
.profile-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 50px;
  font-family: 'Noto Sans KR', sans-serif; /* Google Fonts에서 가져온 글꼴 */
}


</style>


<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300&display=swap');
</style>