<template>
  <div>
    <button @click="deleteBrand" class="btn btn-danger">Delete Brand</button>
  </div>
</template>

<script>
export default {
  props: {
    brandId: {
      type: Number,
      required: true,
    },
  },
  methods: {
    async deleteBrand() {
      try {
        const response = await fetch(
          `http://localhost:8000/api/brands/${this.brandId}`,
          {
            method: "DELETE",
          },

          console.log(`deleted brand: ${this.brandId}`)
        );
        this.$emit("brandDeleted", this.brandId);
      } catch (error) {
        console.error("An error occurred:", error);
      }
    },
  },
};
</script>
