<template>
  <div class="article-detail-container">
    <div v-if="!isEditing" class="article-info-section">
      <hr>
      <h1 class="article-title">제목: {{ article_detail.title }}</h1>
      <p class="article-content">내용: {{ article_detail.content }}</p>
      <hr>

      <button @click="deleteArticle(article)" class="delete-button">게시글 삭제</button>
      <button @click="goBack" class="back-button">목록으로 돌아가기</button>

      <div v-if="store.token" class="edit-button-section">
        <div v-if="store.currentUser.id === article_detail.user">
          <button @click="startEditing" class="edit-button">수정하기</button>
        </div>
      </div>
    </div>

    <!-- 댓글 섹션 -->
    <div class="comment-section">
      <hr>
      <h1>댓글 목록</h1>
      <div v-if="article_detail.comment_set">
        <div v-for="comment in article_detail.comment_set" :key="comment.id" class="comment-item">
          <h3>{{ comment.content }}</h3>
          <button @click="deleteComment(comment)" class="delete-comment-button">댓글 지우기</button>
          <hr>
        </div>
      </div>

      <!-- 댓글 작성 폼 -->
      <form @submit.prevent="commentFrom" class="comment-form">
        <label for="comment_content">댓글 작성:</label>
        <input id="comment_content" v-model="comment_content" class="comment-input">
        <button type="submit" class="comment-submit-button">댓글달기</button>
      </form>
    </div>

    <!-- 수정 폼 섹션 -->
    <div v-if="isEditing" class="edit-form-section">
      <form @submit.prevent="submitForm" class="edit-form">
        <label for="modifiedTitle">수정된 제목:</label>
        <input id="modifiedTitle" v-model="modifiedTitle" class="edit-input" />

        <label for="modifiedContent">수정된 내용:</label>
        <textarea id="modifiedContent" v-model="modifiedContent" class="edit-textarea"></textarea>

        <button type="submit" class="edit-save-button">저장</button>
        <button @click="cancelEditing" class="edit-cancel-button">취소</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted, watch } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const isEditing = ref(false)
const modifiedTitle = ref('')
const modifiedContent = ref('')
const article_detail = ref([])
const author = ref({})
const comment_content = ref('')



const commentFrom = () => {
  axios({
    method: 'post',
    url: `${store.API_URL}/articles/articles/${article_detail.value.id}/comments/`,
    data: {
      content: comment_content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      article_detail.value.comment_set.push(res.data)
      comment_content.value = ''
    })
    .catch((err) => {
      console.log(err)
    })
}

const deleteComment = (comment) => {
  axios({
    method: 'delete',
    url: `${store.API_URL}/articles/comments/${comment.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      article_detail.value.comment_set = article_detail.value.comment_set.filter(c => c.id !== comment.id)
    })
    .catch((err) => {
      console.log(err)
    })
}


const deleteArticle = (article) => {
  axios({
    method: 'delete',
    url: `${store.API_URL}/articles/articles/${article_detail.value.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      store.getArticles
      router.push({ name: 'ArticleView' })
    })
    .catch((err) => {
      console.log(err)
    })
}


const goBack = () => {
  router.go(-1)
  console.log('눌렸음')
}

const startEditing = () => {
  // 편집 시작 시, 기존 내용을 폼에 채워놓을 수 있습니다.
  modifiedTitle.value = article_detail.value.title
  modifiedContent.value = article_detail.value.content
  isEditing.value = true
  console.log(isEditing.value)
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
    })
    .catch((err) => console.log(err))
    console.log(isEditing.value)
    
})
</script>

<style scoped>
.article-detail-container {
  max-width: 800px;
  margin: 0 auto;
}

.article-info-section,
.comment-section,
.edit-form-section {
  margin-bottom: 20px;
}

.article-title {
  font-size: 1.5em;
  margin-bottom: 10px;
}

.article-content,
.comment-item h3 {
  font-size: 1.2em;
}

.delete-button,
.back-button,
.edit-button,
.delete-comment-button,
.comment-submit-button,
.edit-save-button,
.edit-cancel-button {
  background-color: black;
  color: #fff;
  padding: 8px 12px; /* 패딩 조절 */
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-right: 10px;
  font-size: 0.9em; /* 폰트 크기 조절 */
}

.delete-button:hover,
.back-button:hover,
.edit-button:hover,
.delete-comment-button:hover,
.comment-submit-button:hover,
.edit-save-button:hover,
.edit-cancel-button:hover {
  background-color: black;
}

.comment-input,
.edit-input,
.edit-textarea {
  width: 100%;
  padding: 10px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 10px;
}

.edit-form {
  display: flex;
  flex-direction: column;
}
</style>