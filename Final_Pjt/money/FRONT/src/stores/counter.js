import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const rates = ref([])
  const fins = ref([])
  const opts = ref([])
  const deps = ref([])
  const router = useRouter()
  const articles = ref([])
  const token = ref(null)
  const name = ref('')
  const currentUser = ref('')
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })


  const getFins = function () {
    axios({
      method: 'get',
      url: `${API_URL}/fin/deposit-products/`
    })
      .then((res) =>{
        fins.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logIn = async function (payload) {
    try {
      const { username, password } = payload;
  
      // 첫 번째 axios 요청
      const firstRes = await axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      });
  
      // 첫 번째 요청이 성공한 경우
      token.value = firstRes.data.key;
      name.value = username
      router.push({ name: 'HomeView' });
  
      // 두 번째 axios 요청
      const secondRes = await axios({
        method: 'get',
        url: `${API_URL}/profile/user/${username}/`,
      });
  
      // 두 번째 요청이 성공한 경우
      currentUser.value = secondRes.data
      console.log(111111111111111111111)
      // 추가 작업 수행 가능
    } catch (err) {
      // 오류 처리
      console.log(err);
    }
  };

  const signUp = function (payload) {
    const { username, password1, password2, age, money, salary, married, travel } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, age, money, salary,married, travel
      }
    })
      .then((res) => {
        console.log(res)
        const password = password1
        logIn({ username, password })
      })
      .catch((err) => {
        console.log(err)
      })
  }


  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        name.value = ''
        currentUser.value = ''
        // articles.value = []
        router.push({ name: 'HomeView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }


  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/articles/articles/`,
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
      .then((res) =>{
        // console.log(res)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getRates = function () {
    axios({
      method: 'get',
      url: `${API_URL}/exchange/rate/`
    })
      .then((res) => {
        rates.value = res.data
        console.log(rates.value)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  
  const getdeps = function () {
    axios({
      method: 'get',
      url: `${API_URL}/fin/Generaldeposit-products`
    })
      .then((res) =>{
        console.log(res)
        deps.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return { name, currentUser, articles, deps, fins, opts, API_URL, getRates, rates, getFins, getdeps, getArticles, signUp, logIn, token, isLogin, logOut }
},{persist:true})
