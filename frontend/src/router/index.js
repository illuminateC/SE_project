import Vue from 'vue'
import VueRouter from 'vue-router'
import { Message } from 'element-ui';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: '/homepage',
    component: () => import('../views/HomeView.vue')
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/homepage',
    name: 'HomePage',
    component: () => import('../views/HomeView.vue')
  },
  {
    path: '/search',
    name: 'SearchPage',
    component: () => import('../views/SearchView.vue')
  },
  {
    path: '/block/:blockID',
    name: 'BlockPage',
    component: () => import('../views/BlockView.vue')
  },
  {
    path: '/followpage',
    name: 'FollowPage',
    component: () => import('../views/FollowView.vue'),
    meta: {
      requireAuth: true
    }
  },
  {
    path: '/testpage',
    name: 'TestPage',
    component: () => import('../views/AboutView.vue'),
    meta: {
      requireAuth: false
    }
  },
  {
    path: '/personalpage',
    name: 'PersonalPage',
    component: () => import('../views/SearchView.vue'),
    meta: {
      requireAuth: true
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('../views/Register.vue')
  },
  {
    path: '/userprofile',
    name: 'UserProfile',
    component: () => import('../views/UserProfile'),
    meta: {
      requireAuth: true
    }
  },
  {
    path: '/uploadview',
    name: 'upload',
    component: () => import('../views/UploadView.vue'),
    meta: {
      requireAuth: true
    }
  },
  {
    path: '/video/:videoID',
    name: 'video',
    component: () => import('../views/VideoView.vue')
  },
  {
    path: '/otherUser/:userID',
    name: 'OtherUser',
    component: () => import('../views/OtherUser.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  // 记得将LoginPage名字登记正确
  const userInfo = localStorage.getItem('user')
  if (to.path === '/login') {
    localStorage.setItem("preRoute", router.currentRoute.fullPath);
  }
  // 若用户未登录且访问的页面需要登录，则跳转至登录页面
  if (userInfo == null && to.meta.requireAuth) {
    Message({
      type: 'warning',
      message: '请先登录！'
    })
    next({
      name: 'Login',
    })
  }

  next()
})


export default router
