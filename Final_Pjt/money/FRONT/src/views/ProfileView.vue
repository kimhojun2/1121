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
      </div>
    </div>
  </template>

<script setup>
import axios from 'axios'
import { ref, computed, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import { useRoute, useRouter } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const info = ref(null)
const isLoading = ref(true);
const userinfo_2 = ref()
const ans = ref(0)
onMounted(() => {
    axios({
        method : 'get',
        url: `${store.API_URL}/profile/accounts/${route.params.username}/`,
    }) .then((res) => {
        info.value = res.data
        userinfo_2.value = res.data
        // console.log(res.data)
        store.userinfo.value = res.data
        console.log(store.userinfo)
    }) .catch((err)=> console.log(err))
    .finally(() => {
          isLoading.value = false; // Set isLoading to false once the request is complete
        });
})

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