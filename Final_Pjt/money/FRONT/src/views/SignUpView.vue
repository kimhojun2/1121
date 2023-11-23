<template>
  <div>
    <h1>Signup</h1>
    <form @submit.prevent="signUp">
      ID : <input type="text" v-model.trim="username">
      <br>
      Password : <input type="password" v-model.trim="password1">
      <br>
      password 확인:<input type="password" v-model.trim="password2">
      <br>
      1년 내 여행횟수 : <input type="travel" v-model.trim="travel">
      <br>
      나이 : <input type="age" v-model.trim="age">
      <br>
      월급 : <input type="salary" v-model.trim="salary">
      <br>
      자산 : <input type="money" v-model.trim="money">
      <br>
      결혼 여부: <input type="checkbox" v-model="married">
      <br>
      <input type="submit" value="가입">
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

<style>

</style>
