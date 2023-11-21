<template>
    <div>
        <h3>PostList component</h3>
        <hr>
    </div>
    <div v-if="store.articles">
        <ArticleItem 
            v-for=" article in store.articles"
            :key="article.id"
            :article="article"
        />
    </div>
    <div v-else>
        게시글이 없습니다.
    </div>
</template>

<script setup>
import ArticleItem from '@/components/article/ArticleItem.vue'
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()
</script>

<style scoped>

</style>