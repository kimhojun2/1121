<template>
    <div>
      <div class="table-container">
        <table>
          <thead>
            <tr class="first">
              <th>은행</th>
              <th>상품명</th>
              <th>금융상품코드</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="deposit in filteredDeposits" :key="deposit.id">
              <td>{{ deposit.kor_co_nm }}</td>
              <td>
                <RouterLink :to="{ name: 'DepositDetailView', params: { id: deposit.fin_prdt_cd }}">
                  {{ deposit.fin_prdt_nm }}</RouterLink>
                
              </td>
              <td>{{ deposit.fin_prdt_cd }}</td>
              <td>{{ deposit }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </template>

<script setup>  
import { ref, computed, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'

const store = useCounterStore();



defineProps({
    filteredDeposits: Object
})




</script>

<style scoped>
.table-container {
  max-height: 800px; /* 표의 최대 높이를 지정 */
  overflow-y: auto; /* 세로 스크롤이 필요한 경우 스크롤 표시 */
}

table {
  width: 100%; /* 표의 너비를 100%로 설정 */
  border-collapse: collapse; /* 테두리가 겹치지 않도록 설정 */
}

th, td {
  border: 1px solid #ddd; /* 테두리 스타일 지정 */
  padding: 8px; /* 셀 안의 내용과 테두리 사이의 간격 설정 */
  text-align: left; /* 텍스트를 왼쪽 정렬로 설정 */
}

th {
  background-color: #f2f2f2; /* 헤더 셀의 배경색 설정 */
}
</style>