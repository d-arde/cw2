<template>
  <!-- @click="openUpdateModal(selectedBrandData)" -->
  <!-- @click="fetchID(brandId)" -->
  <button
    @click="openUpdateModal()"
    type="button"
    id="update"
    class="btn btn-primary p-2 m-2"
    data-bs-toggle="modal"
    data-bs-target="`#updateModal${brandId}`"
  >
    Update Car Brand
  </button>
  <div class="modal fade" :id="`updateModal${brandId}`">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="updateModalLabel">
            Update Car Brand (component2)
          </h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
          ></button>
        </div>
        <div class="modal-body">
          <form id="updateForm" class="form-group" v-if="updateBrandData">
            <!-- <label for="brandID">Brand ID: </label>
              <input
                type="text"
                v-model="updateBrandData.id"
                placeholder="Brand ID"
                class="form-control"
              /> -->
            <label for="brandName">Brand Name: </label>
            <input
              type="text"
              v-model="updateBrandData.brand_name"
              placeholder="Brand Name"
              class="form-control"
              id="updateName"
            />
          </form>
          <button @click="updateBrand()" class="btn btn-primary">
            Update Brand
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    modalID: String,
    brandData: {
      type: Object,
      required: true,
    },
    brandId: {
      type: Number,
      required: true,
    },
  },
  emits: ["brand-updated", "updatePressed"],
  data() {
    return {
      // localBrandData: { ...this.brandData },
      // updateBrandData: { ...this.brandData }, //delete this if it breaks
      updateBrandData: {},
    };
  },
  methods: {
    async updateBrand() {
      try {
        if (Object.keys(this.updateBrandData).length > 0) {
          // Check if updateBrandData is not null
          const updatedData = {
            brand_name: this.updateBrandData.brand_name,
            date_founded: this.updateBrandData.date_founded,
            email: this.updateBrandData.email,
            revenue: this.updateBrandData.revenue,
          };

          const response = await fetch(
            `http://localhost:8000/api/brands/${this.brandId}/`,
            {
              method: "PUT",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify(updatedData),
            }
          );

          console.log("API Response:", response);

          if (response.status === 200) {
            // Brand successfully updated
            console.log("Brand updated successfully");

            this.$emit("brand-updated", this.updateBrandData);
          } else {
            // Handle errors or display a message if the update fails
            console.error("Brand update failed");
          }
        }
      } catch (error) {
        console.error("An error occurred:", error);
      }
    },

    async fetchID(id) {
      try {
        const response = await fetch(
          `http://localhost:8000/api/brands/${id}/`,
          {
            method: "GET",
          }
        );
        if (response.ok) {
          const data = await response.json();
          this.updateBrandData = data;
          console.log("fetchID worked", this.updateBrandData);
        } else {
          console.error("fetched to get data from fetchID method");
        }
      } catch (error) {
        console.error("An error occured: ", error);
      }
    },

    openUpdateModal() {
      this.fetchID(this.brandId);
    },
  },
};
</script>
