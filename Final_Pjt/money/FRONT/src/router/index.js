import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import FinView from '@/views/Fin/FinView.vue'
import DepositView from '@/views/Fin/DepositView.vue'
import DepositDetailView from '@/views/Fin/DepositDetailView.vue'
import SavingView from '@/views/Fin/SavingView.vue'
import SavingDetailView from '@/views/Fin/SavingDetailView.vue'
import MapView from '@/views/MapView.vue'
import ExchangeRateView from '@/views/ExchangeRateView.vue'
import ArticleView from '@/views/ArticleView.vue'
import Newjeans from '@/views/Newjeans.vue'
import MainPageView from '@/views/MainPageView.vue'
// import DepositDetailView from '@/views/DepositDetailView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import CreateView from '@/views/CreateView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/FinView',
      name: 'FinView',
      component: FinView,
      redirect: '/FinView/DepositView',
      children: [
        {
          path: '/FinView',
          name: 'FinView',
          component: FinView
        },
        {
          path: 'DepositView',
          name: 'DepositView',
          component: DepositView
        },
        {
          path: 'SavingView',
          name: 'SavingView',
          component: SavingView
        },
        {
          path: 'deposits/:id',
          name: 'DepositDetailView',
          component: DepositDetailView
        },
        {
          path: 'savings/:id',
          name: 'SavingDetailView',
          component: SavingDetailView
        },

      ]
    },
    {
      path: '/MapView',
      name: 'MapView',
      component: MapView
    },
    {
      path: '/ExchangeRateView',
      name: 'ExchangeRateView',
      component: ExchangeRateView
    },
    {
      path: '/ArticleView',
      name: 'ArticleView',
      component: ArticleView
    },
    {
      path: '/Newjeans',
      name: 'Newjeans',
      component: Newjeans
    },
    {
      path: '/HomeView',
      name: 'HomeView',
      component: HomeView
    },
    {
      path: '/',
      name: 'MainPageView',
      component: MainPageView
    },
    // {
    //   path: '/DepositDetailView/:id',
    //   name: 'DepositDetailView',
    //   component: DepositDetailView,
    // },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
      path: '/ProfileView/:username',
      name: 'ProfileView',
      component: ProfileView
    },
    {
      path: '/ArticleDetailView/:id/',
      name: 'ArticleDetailView',
      component: ArticleDetailView
    },
    // {
    //   path: '/DepositView',
    //   name: 'DepositView',
    //   component: DepositView
    // },
    // {
    //   path: '/SavingView',
    //   name: 'SavingView',
    //   component: SavingView
    // },
    
    
  ]
})

export default router
