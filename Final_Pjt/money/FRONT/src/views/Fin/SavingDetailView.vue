<template>
  <div>
    <div v-if="isLoading">Loading...</div>
    <div v-else>
      <div>
        <h1>상품 이름: {{ saving.fin_prdt_nm }}</h1>
        <h1>{{ saving.fin_prdt_cd }}</h1>
        <button @click="selectitem" class="custom-button" :class="{ 'selected': isAlreadySelected }">
          {{ isAlreadySelected ? '해지하기' : '가입하기' }}
        </button>
      </div>
      <h2>은행 이름: {{ saving.kor_co_nm }}</h2>
      <div v-for="option in saving.options" :key="option.id">
        <div>
          단/복: {{ option.intr_rate_type_nm }}
          금리: {{ option.intr_rate }}
          최고 금리:{{ option.intr_rate2 }}
          예금 기간:{{ option.save_trm }}
        </div>
      </div>
      <button @click="goBack">목록으로 돌아가기</button>
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
  const saving = ref(null)
  const isLoading = ref(true);
  const list = ref(store.currentUser.financial_products);
  const isAlreadySelected = ref(false);
  
  const goBack = () => {
      router.go(-1)
      console.log('눌렸음')
  }
  
  
  const selectitem = function () {
  axios({
    method: 'put',
    url: `${store.API_URL}/profile/accounts/${store.name}/`,
    data: {
      financial_products: saving.value.fin_prdt_cd,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      list.value = res.data;
      store.currentUser.financial_products = list.value;
      isAlreadySelected.value = String(list.value.financial_products).includes(saving.value.fin_prdt_cd);
      console.log(isAlreadySelected.value);
    })
    .catch((err) => {
      console.log(err);
    });
};




onMounted(async () => {
  store.currentUser
  console.log('list : ', list)
  try {
    const res = await axios.get(`${store.API_URL}/fin/saving-product/${route.params.id}/`);
    saving.value = res.data;
    console.log(res)
    if (store.currentUser) {
      if (list.value) {
        isAlreadySelected.value = String(list.value.financial_products).includes(saving.value.fin_prdt_cd);
    }}
    isLoading.value = false;
  } catch (err) {
    console.log(err);
  }
});
  
  
  
  </script>
  
  <style scoped>
  .custom-button {
    background-color: #4CAF50; /* Green */
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    transition-duration: 0.4s;
    cursor: pointer;
    border-radius: 8px;
    border: none; /* 테두리 없애기 */
  }


  .selected {
    background-color: #FF0000; /* Red */
  }
</style>