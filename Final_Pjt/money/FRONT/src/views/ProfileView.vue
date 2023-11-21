<template>
  <div class="profile-container">
    <div v-if="isLoading" class="loading">Loading...</div>
    <div v-else>
      <div class="profile-box">
        <h1 class="username">{{ info.username }}</h1>
        <div class="info-container">
          <div class="info-item">
            <strong>Money:</strong> {{ info.money }}
          </div>
          <div class="info-item">
            <strong>Salary:</strong> {{ info.salary }}
          </div>
          <div class="info-item">
            <strong>Age:</strong> {{ info.age }}
          </div>
          <div v-if="info.financial_products" class="info-item">
            <strong>Financial Products:</strong>
            <div v-for="product in info.financial_products.split(',')" :key="product">
              <span class="product">{{ product.trim() }}</span>
            </div>
          </div>
        </div>
      </div>

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

      <!-- 수정 버튼 -->
      <button v-if="!isEditMode" @click="toggleEditMode">Edit Profile</button>
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
})

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
</script>

<style scoped>
.profile-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.profile-box {
  max-width: 400px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.loading {
  font-size: 18px;
  text-align: center;
}

.username {
  font-size: 24px;
  margin-bottom: 10px;
}

.info-container {
  margin-top: 20px;
}

.info-item {
  margin-bottom: 10px;
}

.product {
  background-color: #f0f0f0;
  padding: 5px;
  margin-right: 5px;
  display: inline-block;
  border-radius: 5px;
}
</style>