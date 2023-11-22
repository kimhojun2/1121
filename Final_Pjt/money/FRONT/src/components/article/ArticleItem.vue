<template>
    <div>
      <h5>{{ article.id }}</h5>
      <RouterLink :to="{ name:'ArticleDetailView', params:{ id:article.id }}"><p>{{ article.title }}</p></RouterLink>
      <p>{{ article.content }}</p>
      <p>작성자 : {{ article.user.username }}</p>
      <p>댓글 수 : {{ article.comment_count }}</p>
      <hr>
    </div>

  </template>
  
  <script setup>
  import { RouterLink } from 'vue-router'
  import { onMounted, ref } from 'vue';
  import { useCounterStore } from '@/stores/counter'
  import { useRoute } from 'vue-router';

  const props = defineProps({
    article: Object
  })

  const route = useRoute()
  const store = useCounterStore()
  </script>