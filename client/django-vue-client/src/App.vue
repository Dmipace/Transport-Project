<template>

  <body>
    <div>
      <div id="app" class="container">
        <h3 class="d-flex justify-content-center">
          Vue.js Front End + Django
        </h3>
        <h5 class="d-flex justify-content-center">
          Transport Customer Management System
        </h5>
        <nav class="navbar navbar-expand-sm bg-light navbar-dark">
          <ul class="navbar-nav">
            <li class="nav-item m-1">
              <router-link class="btn btn-light btn-outline-primary" to="/home">Home</router-link>
            </li>
            <li class="nav-item m-1"> <router-link class="btn btn-light btn-outline-primary"
                to="/department">Departments</router-link> </li>
            <li class="nav-item m-1"> <router-link class="btn btn-light btn-outline-primary"
                to="/customer">Customers</router-link>
            </li>
          </ul>
        </nav>
        <main>
          <router-view />
        </main>
      </div>
    </div>
  </body>
</template>

<!-- <script lang="ts">
import { ref, defineComponent } from 'vue'

export default defineComponent({
  name: 'App',
  props: {
    msg: {
      type: String,
      required: true
    }
  },
  setup() {
    const count = ref(0)
    return { count }
  }
})

</script> -->

<style></style>
