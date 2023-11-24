<template>
  <div class="signup-container">
    <h1>Signup</h1>
    <form @submit.prevent="signUp" class="signup-form">
      <div class="form-group">
        <label for="username">ID:</label>
        <input type="text" id="username" v-model.trim="username">
      </div>

      <div class="form-group">
        <label for="password1">Password:</label>
        <input type="password" id="password1" v-model.trim="password1">
      </div>

      <div class="form-group">
        <label for="password2">Password 확인:</label>
        <input type="password" id="password2" v-model.trim="password2">
      </div>

      <div class="form-group">
        <label for="travel">1년 내 여행 횟수:</label>
        <input type="text" id="travel" v-model.trim="travel">
      </div>

      <div class="form-group">
        <label for="age">나이:</label>
        <input type="text" id="age" v-model.trim="age">
      </div>

      <div class="form-group">
        <label for="salary">월급:</label>
        <input type="text" id="salary" v-model.trim="salary">
      </div>

      <div class="form-group">
        <label for="money">자산:</label>
        <input type="text" id="money" v-model.trim="money">
      </div>

      <div class="form-group">
        <label>결혼 여부:</label>
        <input type="checkbox" v-model="married">
      </div>

      <div class="form-group">
        <button type="submit">가입</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const travel = ref(null)
const age = ref(null)
const salary = ref(null)
const money = ref(null)
const married = ref(false) // 초기값은 결혼하지 않은 상태로 설정

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    age: age.value,
    money: money.value,
    salary: salary.value,
    travel: travel.value,
    married: married.value // 결혼 여부 추가
  }
  console.log(payload)
  store.signUp(payload)
}


</script>

<style scoped>

.signup-container {
  max-width: 400px;
  margin: 0 auto;
}

.signup-form {
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

button {
  background-color: black;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  width: 100%;
}

/* button:hover {
  background-color: #45a049;
} */
</style>
