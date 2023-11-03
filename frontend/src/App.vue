<template>
  <div class="container p-3">
    <div class="h1 text-center border rounded bg-light p-2 mb-3">
      Database of Car Brands
    </div>
    <div class="mb-3 text-center">
      <addBrand @brandAdded="handleBrandRefresh"></addBrand>
      <displayView
        @brandUpdated="handleBrandRefresh"
        @brandDeleted="handleBrandRefresh"
        :responseData="response_data"
      ></displayView>
    </div>
  </div>
</template>

<script>
import displayView from "./components/displayView.vue";
import addBrand from "./components/addBrand.vue";

export default {
  props: {},
  components: {
    displayView,
    addBrand,
  },
  data() {
    return {
      response_data: [],
    };
  },
  methods: {
    // handleEmit(data) {
    //   this.response_data = data;
    // },
    async handleBrandRefresh() {
      // dont change params to be populated
      // console.log("brand added in app.vue", addedBrand);
      // this.response_data.push(addedBrand);
      // this.$emit("brandAdded", addedBrand);
      try {
        const response = await fetch("http://localhost:8000/api/test.json");
        this.response_data = await response.json();
        console.log("working?", this.response_data);
      } catch (error) {
        console.error("Error: ", error);
      }
    },
  },
  async mounted() {
    this.handleBrandRefresh(); // dont change
  },
  computed: {},
};
</script>
