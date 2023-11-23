<template>
  <div>
    <h1>게시판</h1>
    <div v-if="store.token">
    <RouterLink :to="{ name: 'CreateView' }">
      [CREATE]
    </RouterLink>
    </div>
    <ArticleList />
  </div>
</template>

<script setup>

import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/article/ArticleList.vue'

const store = useCounterStore()

onMounted(() => {
  store.getArticles()
  console.log(store)
})

</script>

<style>

</style>
