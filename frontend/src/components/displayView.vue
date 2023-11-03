<template>
  <div>
    <button
      @click="dataVis(brand)"
      id="display"
      type="button"
      class="btn btn-primary p-2 m-2"
    >
      Display all brands and information
    </button>
    <div v-if="showData">
      <div v-for="brand in responseData" :key="brand.id">
        <!-- <p>ID: {{ brand.id }}</p> -->
        <h3>{{ brand.brand_name }}</h3>
        <p>Founded: {{ brand.date_founded }}</p>
        <p>Email: {{ brand.email }}</p>
        <p>Revenue: {{ brand.revenue }}</p>
        <!-- <button
          @click="openUpdateModal(brand)"
          type="button"
          class="btn btn-primary"
        >
          Update
        </button> -->
        <!-- :brandId="brand.id" -->
        <!-- <updateBrand :brandId="brand.id" @brand-updated="handleBrandUpdated" /> -->
        <random
          :brandId="brand.id"
          :brandData="brand"
          @brand-updated="handleBrandUpdated"
        />
        <deleteBrand @brandDeleted="handleBrandDeleted" :brandId="brand.id" />
        <br />
      </div>
    </div>
  </div>
</template>

<script>
import updateBrand from "./updateBrand.vue";
import deleteBrand from "./deleteBrand.vue";
import random from "./component2.vue";
export default {
  props: {
    responseData: {
      //if broken put responseData
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      showData: false,
      allBrands: [],
      selectedBrandData: {},
      selectedBrandID: 0,
    };
  },
  components: { updateBrand, deleteBrand, random },
  methods: {
    dataVis() {
      this.showData = !this.showData;
    },
    handleBrandUpdated(updatedBrand) {
      console.log("brand received: ", updatedBrand);
      // this.allBrands.push(updatedBrand);
      this.brandData = { ...updatedBrand };
      this.$emit("brandUpdated", updatedBrand);
    },
    handleBrandDeleted(deletedBrandId) {
      this.allBrands = this.allBrands.filter(
        (brand) => brand.id !== deletedBrandId
      );
      this.$emit("brandDeleted", deletedBrandId);
    },

    openUpdateModal(brand) {
      console.log("openUpdate method", brand);
      this.brandData = { ...brand };
    },
  },
};
</script>
