<template>
  <div class="container">
    <div class="card">
      <div class="card-header">
        <h4>
          <!-- <RouterLink to="/department/create" class="btn btn-primary">Add Department</RouterLink> -->
        </h4>
      </div>
      <div class="card-body">
        <table class="table table-bordered">
          <thead>
            <tr>
              <th>
                Customer-Id
              </th>
              <th>Department</th>
              <th>Customer Name</th>
              <th>Date of order</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(department, index) in this.departments" :key="index">
              <td>{{ department.CustomerId }}</td>
              <td>{{ department.Department }}</td>
              <td>{{ department.CustomerName }}</td>
              <td>{{ department.DateOfOrder }}</td>
              <td>
                <!-- <RouterLink to="/" class="btn btn-success">
                  Edit
                </RouterLink> -->
                <!-- <button type="buttton" class="btn btn-danger float-end">
                  Delete
                </button> -->
              </td>
            </tr>
          </tbody>
        </table>

      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  name: 'Departments',
  data() {
    return {
      departments: [],
      DepartmentIdFilter: "",
      DepartmentNameFilter: "",
      departmentsWithoutFilter: [],
      DepartmentId: 0,
      DepartmentName: "",
    }
  },
  mounted() {
    this.getData();
    //console.log("i am here")
  },
  methods: {
    getData() {
      axios.get('http://127.0.0.1:8000/customer').then(res => {
        this.departments = res.data
        this.departmentsWithoutFilter = res.data;
        console.log(this.departments)
      })
    },

  }
}

</script>
