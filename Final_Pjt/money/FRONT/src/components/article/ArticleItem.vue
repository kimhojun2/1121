<template>
    <div>
      <h5>{{ article.id }}</h5>
      <RouterLink :to="{ name: 'ArticleDetailView', params:{ id:article.id }}"><p>{{ article.title }}</p></RouterLink>
      <p>{{ article.content }}</p>
      <hr>
    </div>
  </template>
  
  <script setup>
  import { RouterLink } from 'vue-router'
  import { onMounted } from 'vue';
  defineProps({
    article: Object
  })



  </script>
  