<template>
  <div class="container">
    <div class="card">
      <div class="card-header">
        <h4>
          <RouterLink to="/customer/create" class="btn btn-primary">Order Transport</RouterLink>
        </h4>
      </div>
      <div class="card-body">
        <table class="table table-bordered">
          <thead>
            <tr>
              <th>Customer-Id</th>
              <th>Name</th>
              <th>Type of order</th>
              <th>Date</th>
              <th>Pickup location</th>
              <th>Waypoint location</th>
              <th>Delivery location</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(customer, index) in this.customers" :key="index">
              <td>{{ customer.CustomerId }}</td>
              <td>{{ customer.CustomerName }}</td>
              <td>{{ customer.Department }}</td>
              <td>{{ customer.DateOfOrder }}</td>
              <td>{{ customer.AddressOfPickup }}</td>
              <td>{{ customer.AddressOfWaypoint }}</td>
              <td>{{ customer.AddressOfDelivery }}</td>
              <td>
                <RouterLink :to="{ path: '/customer/' + customer.CustomerId + '/edit' }" class="btn btn-success">
                  Edit
                </RouterLink>
                <button type="buttton" @click="deleteStudent(customer.CustomerId)" class="btn btn-danger float-end">
                  Delete
                </button>
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
  name: 'Customers',
  data() {
    return {
      customers: []
    }
  },
  mounted() {
    this.getData();
    //console.log("i am here")
  },
  methods: {
    getData() {
      axios.get('http://127.0.0.1:8000/customer').then(res => {
        this.customers = res.data
        console.log(this.customers)
      })
    },
    deleteStudent(customerId) {

      if (confirm('You want to delete this?')) {
        //console.log(customerId);

        axios.delete(`http://127.0.0.1:8000/customer/${customerId}`).then(res => {
          console.log("Udaj bol vymazaný");
          this.getData();
        }).catch(function (error) {
          if (error.response) {

            // if(error.response.status == 442){
            //     mythis.errorList == error.response.data.errors;
            // }
            console.log(error.response.data);
            console.log(error.response.status);
            console.log(error.response.headers);
          } else if (error.request) {
            console.log(error.request);
          } else {
            console.log('Error', error.message);
          }
        })
      }
    }
  }
}

</script>
