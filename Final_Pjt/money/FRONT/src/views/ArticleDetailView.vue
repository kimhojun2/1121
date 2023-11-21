<template>
    <div>
      <div v-if="!isEditing">
        <h1>{{ article_detail.title }}</h1>
        <h1>{{ article_detail.content }}</h1>
        <h1>{{ article_detail.created_at }}</h1>
        <h1>{{ article_detail.updated_at }}</h1>
        <p>userid : {{ article_detail.user }}</p>
        <button @click="goBack">목록으로 돌아가기</button>
        <button @click="startEditing">수정하기</button>
      </div>
      <div>
      <div v-if="isEditing">
        <!-- 수정 폼 -->
        <form @submit.prevent="submitForm">
          <label for="modifiedTitle">수정된 제목:</label>
          <input id="modifiedTitle" v-model="modifiedTitle" />
  
          <label for="modifiedContent">수정된 내용:</label>
          <textarea id="modifiedContent" v-model="modifiedContent"></textarea>
  
          <button type="submit">저장</button>
          <button @click="cancelEditing">취소</button>
        </form>
      </div>
    </div>
    </div>
  </template>

<script setup>
  import axios from 'axios'
  import { ref, onMounted } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import { useRoute, useRouter } from 'vue-router'

  const store = useCounterStore()
  const route = useRoute()
  const router = useRouter()
  const isEditing = ref(false)
  const modifiedTitle = ref('')
  const modifiedContent = ref('')
  const article_detail = ref([])

  const goBack = () => {
    router.go(-1)
    console.log('눌렸음')
  }

  const startEditing = () => {
    // 편집 시작 시, 기존 내용을 폼에 채워놓을 수 있습니다.
    modifiedTitle.value = article_detail.value.title
    modifiedContent.value = article_detail.value.content

    isEditing.value = true
  }

  const submitForm = () => {
    axios({
      method: 'put',
      url: `${store.API_URL}/articles/articles/${route.params.id}/`,
      data: {
        title: modifiedTitle.value,
        content: modifiedContent.value
        // Add other fields as needed
      },
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((res) => {
        article_detail.value = res.data
        // Optionally, update the local data with the modified article
        isEditing.value = false
      })
      .catch((err) => console.log(err))

  }

  const cancelEditing = () => {
    isEditing.value = false
  }

  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/articles/articles/${route.params.id}/`,
    })
      .then((res) => {
        article_detail.value = res.data
        console.log(res.data)
      })
      .catch((err) => console.log(err))
  })
</script>

<style scoped>
  /* Add your styles here */
</style>