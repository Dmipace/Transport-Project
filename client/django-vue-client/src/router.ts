import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Customer from '@/views/Customers.vue'
import Department from '@/views/Departments.vue'
import CustomerCreate from './views/CustomersCreate.vue'
import CustomerEdit from './views/CustomersEdit.vue'

export default createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/home',
      component: Home,
    },
    {
      path: '/customer',
      component: Customer,
    },
    {
      path: '/customer/create',
      component: CustomerCreate,
    },
    {
      path: '/customer/:id/edit',
      component: CustomerEdit,
    },
    {
      path: '/department',
      component: Department,
    },
  ],
})

