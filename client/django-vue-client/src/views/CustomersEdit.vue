<template>
    <div class="container mt-5">
        <div class="card">
            <div class="card-header">
                <h4>Edit customers order</h4>
            </div>
            <div class="card-body">
                <div class="mb-3">
                    <label for="">Name</label>
                    <input type="text" v-model="model.customer.CustomerName" class="form-control">
                </div>
                <div class="mb-3">
                    <label for="order">Type of order:
                        <select id="order" name="order" v-model="model.customer.Department">
                            <option value="delivery">Delivery</option>
                            <option value="pickup">Pickup</option>
                        </select>
                    </label>
                </div>
                <div class="mb-3">
                    <label for="">Pickup Address</label>
                    <input type="text" v-model="model.customer.AddressOfPickup" class="form-control">
                </div>
                <div class="mb-3">
                    <label for="">Waypoint Address</label>
                    <input type="text" v-model="model.customer.AddressOfWaypoint" class="form-control">
                </div>
                <div class="mb-3">
                    <label for="">Delivery Address</label>
                    <input type="text" v-model="model.customer.AddressOfDelivery" class="form-control">
                </div>
                <div class="mb-3">
                    <button type="button" @click="updateCustomer" class="btn btn-primary">Update</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';


export default {
    name: 'customerEdit',
    data() {
        return {
            customerId: '',
            errorList: '',
            model: {
                customer: {
                    CustomerName: '',
                    Department: '',
                    AddressOfPickup: '',
                    AddressOfWaypoint: '',
                    AddressOfDelivery: ''
                }
            }
        }
    },
    mounted() {
        //console.log(this.$route.params.id)
        this.customerId = this.$route.params.id
        this.getCustomerData(this.$route.params.id);

    },
    methods: {
        getCustomerData(customerId) {
            axios.get(`http://127.0.0.1:8000/customer/${customerId}/edit`).then(res => {
                console.log(res.data);

                this.model.customer = res.data
            }).catch(function (error) {
                if (error.response) {

                    if (error.response.status == 404) {
                        alert("This id is not found.");
                    }
                }
            })
        },
        updateCustomer() {

            var mythis = this;

            axios.put(`http://127.0.0.1:8000/customer/${this.customerId}/edit`, this.model.customer).then(res => {
                console.log(res.data)
                alert("Successfully added");


                this.errorList = '';

            }).catch(function (error) {
                if (error.response) {

                    if (error.response.status == 404) {
                        console.log(error)
                    }
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
    },
}

</script>
