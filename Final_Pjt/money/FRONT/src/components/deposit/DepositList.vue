
<template>
  <div>
    <h3>예금상품 목록</h3>

    <select v-model="selectedBank">
      <option value="">전체</option>
      <option v-for="bank in bankOptions" :key="bank" :value="bank">{{ bank }}</option>
    </select>
    
    <select v-model="selectedTerm" @change="filterFins">
      <option value="">전체</option>
      <option v-for="term in termOptions" :key="term" :value="term">{{ term }}</option>
    </select>

    <button @click="filterFins">선택</button>

    <div v-if="filteredFins.length > 0" class="box">
      <table>
        <thead>
          <tr>
            <th class="box2">은행명</th>
            <th class="box2">상품명</th>
            <th class="box2">옵션</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="dep in filteredFins" :key="dep.id" class="box3">
            <td>{{ dep.kor_co_nm }}</td>
            <td>
              <RouterLink :to="{ name: 'DepositDetailView', params: { id: dep.fin_prdt_nm}}">{{ dep.fin_prdt_nm }}</RouterLink>
            </td>
            <td>
              <div class="option-container">
                <div v-for="opt in getFilteredOptions(dep.options)" :key="opt.id" class="option-item">
                  <p>({{ opt.intr_rate_type_nm }})</p>
                  <p>{{ opt.save_trm }}개월 이율: {{ opt.intr_rate }}</p>
                </div>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else>
      선택된 은행이나 이자 기간에 해당하는 항목이 없습니다.
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const selectedBank = ref('')
const selectedTerm = ref('')
const filteredFins = ref([])

const bankOptions = Array.from(new Set(store.deps.map(dep => dep.kor_co_nm)))
const termOptions = Array.from(new Set(store.deps.flatMap(dep => dep.options.map(opt => opt.save_trm))))

const filterFins = () => {
  if (selectedBank.value || selectedTerm.value) {
    filteredFins.value = store.deps.filter(dep => {
      const matchBank = selectedBank.value ? dep.kor_co_nm === selectedBank.value : true
      const matchTerm = selectedTerm.value ? dep.options.some(opt => opt.save_trm === selectedTerm.value) : true
      return matchBank && matchTerm
    })
  } else {
    filteredFins.value = store.deps
  }
}

// const filterFinsBySelectedBankAndTerm = () => {
//   filterFins()
// }

// 6개월 이상의 옵션만 반환하는 함수
const getFilteredOptions = options => {
  if (selectedTerm.value) {
    return options.filter(opt => opt.save_trm === selectedTerm.value)
  } else {
    return options
  }
}
</script>

<style scoped>
.option-container {
  display: flex;
  /* gap: 20px; */
}

.option-item {
  display: flex;
  /* padding: 10px; */
  width: 200px;
  
}
.box {
  border: 1px solid black;
}

.box2 {
  width: 200px;
  background-color: lightblue;
  border: 1px solid black;
}

.box3 {
  background-color: lightgray;
  border: 1px solid black;
  
}
</style>
