<template>
  <div class="login-container">
    <h1>로그인</h1>
    <form @submit.prevent="logIn" class="login-form">
      <div class="form-group">
        <label for="username">ID:</label>
        <input type="text" id="username" v-model.trim="username">
      </div>

      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model.trim="password">
      </div>

      <div class="form-group">
        <button type="submit" class="login-button">로그인</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const username = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 0 auto;
  margin-top: 10rem;
}

.login-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-top: 5px;
}

.login-button {
  background-color: black;
  color: white;
  padding: 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  width: 100%;
}

/* .login-button:hover {
  background-color: #45a049;
} */
</style>
