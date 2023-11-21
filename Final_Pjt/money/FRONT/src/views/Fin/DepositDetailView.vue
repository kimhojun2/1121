<template>
  <div>
    <div v-if="isLoading">Loading...</div>
    <div v-else>
      <!-- Your actual content goes here -->
      <div>
        <h1>상품 이름 : {{ deposit.fin_prdt_nm }}</h1>
        <button @click="selectitem">가입하기</button>
      </div>  
      <h2>은행 이름 : {{ deposit.kor_co_nm }}</h2>
        <div v-for="option in deposit.options">
            <div>
                단/복 : {{ option.intr_rate_type_nm }}
                금리 : {{ option.intr_rate }}
                최고 금리 :{{ option.intr_rate2 }}
                예금 기간 :{{ option.save_trm }}
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
const deposit = ref(null)
const isLoading = ref(true);
const goBack = () => {
    router.go(-1)
    console.log('눌렸음')
}
const selectitem = function () {
    axios({
      method: 'put',
      url: `${store.API_URL}/profile/accounts/${store.name}/`,
      data: {
        // username: store.name,
        financial_products : deposit.value.fin_prdt_cd
      },
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
  }


onMounted(() => {
    store.name
    axios({
        method : 'get',
        url: `${store.API_URL}/fin/deposit-product/${route.params.id}/`,
    }) .then((res) => {
        deposit.value = res.data
        console.log(res.data)
    }) .catch((err)=> console.log(err))
    .finally(() => {
          isLoading.value = false; // Set isLoading to false once the request is complete
        });
})



</script>

<style scoped>

</style>