<template>
    <div>
      <h1>Fin</h1>
      <div class="router-links">
        <RouterLink :to="{ name: 'DepositView' }" class="custom-link" :class="{ 'active-link': $route.name === 'DepositView' }">DepositView</RouterLink>
        <RouterLink :to="{ name: 'SavingView' }" class="custom-link" :class="{ 'active-link': $route.name === 'SavingView' }">SavingView</RouterLink>
      </div>
      <RouterView />
    </div>
  </template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { onMounted } from 'vue'
// import depositList from '@/components/deposit/depositList.vue'
import { RouterLink } from 'vue-router'
const store = useCounterStore()

onMounted(()=>{
    store.getdeps()
    store.getFins()
    console.log(store)
    // store.getopt()

})

</script>

<style>
.router-links {
  display: flex;
  gap: 10px;
}

.custom-link {
  padding: 8px;
  background-color: #929394;
  color: #ffffff;
  text-decoration: none;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.custom-link:hover {
  background-color: #2a3336;
}

.active-link {
  background-color: #21b3e4; /* Change the color for active link */
}
</style>