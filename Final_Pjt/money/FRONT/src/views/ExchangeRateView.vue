<template>
    <div>
      <ExchangeList />
    </div>
  </template>
  
<script setup>
import { useCounterStore } from '@/stores/counter'
import { onMounted } from 'vue'
import ExchangeList from '@/components/exchange/ExchangeList.vue';
  
  const store = useCounterStore()

  onMounted(() => {
    store.getRates()
  })
  </script>
  
  <style>
  
  </style>
  