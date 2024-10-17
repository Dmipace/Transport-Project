<template>
    <div class="container mt-5">
        <div class="card">
            <div class="card-header">
                <h4>Add Order</h4>
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
                    <label for="">Beginning of the address</label>
                    <input type="text" v-model="model.customer.AddressOfPickup" class="form-control">
                </div>
                <div class="mb-3">
                    <label for="">Waypoint address</label>
                    <input type="text" v-model="model.customer.AddressOfWaypoint" class="form-control">
                </div>
                <div class="mb-3">
                    <label for="">End of the address</label>
                    <input type="text" v-model="model.customer.AddressOfDelivery" class="form-control">
                </div>
                <div class="mb-3">
                    <button type="button" @click="saveCustomer()" class="btn btn-primary">Save</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';


export default {
    name: 'customerCreate',
    data() {
        return {
            // errorList: '',
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
    methods: {
        saveCustomer() {

            var mythis = this;

            axios.post('http://127.0.0.1:8000/customer', this.model.customer).then(res => {
                console.log(res.data)
                alert("Successfully added");

                this.model.customer = {
                    CustomerName: '',
                    Department: '',
                    AddressOfPickup: '',
                    AddressOfWaypoint: '',
                    AddressOfDelivery: ''
                }
                // this.errorList = '';

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
    },
}

</script>
