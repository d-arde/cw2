<template>
  <button
    type="button"
    id="add"
    class="btn btn-primary p-2 m-2"
    data-bs-toggle="modal"
    data-bs-target="#addModal"
  >
    Add Car Brand
  </button>
  <div class="modal fade" id="addModal">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="addModalLabel">Add Car Brand</h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
          ></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="postBrand" id="addForm" class="form-group">
            <label for="brandName">Brand Name: </label>
            <input
              type="text"
              name="brandName"
              id="brandName"
              class="form-control"
            />
            <label for="brandDateFounded">Brand Date Founded: </label>
            <input
              type="date"
              name="brandDateFounded"
              id="brandDateFounded"
              class="form-control"
            />
            <label for="brandEmail">Brand Email: </label>
            <input
              type="text"
              name="brandEmail"
              id="brandEmail"
              class="form-control"
            />
            <label for="brandRevenue">Brand Revenue: </label>
            <input
              type="text"
              name="brandRevenue"
              id="brandRevenue"
              class="form-control"
            />
            <br />
            <div class="modal-footer">
              <input
                type="submit"
                value="Submit"
                class="btn btn-primary"
                data-bs-dismiss="modal"
              />
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  emits: ["brandAdded"],
  methods: {
    async postBrand(submitEvent) {
      const details = {
        name: submitEvent.target.elements.brandName.value,
        date: submitEvent.target.elements.brandDateFounded.value,
        email: submitEvent.target.elements.brandEmail.value,
        revenue: submitEvent.target.elements.brandRevenue.value,
      };
      try {
        const response = await fetch("http://localhost:8000/api/test.json", {
          method: "POST",
          body: JSON.stringify(details),
        });

        if (response.status === 200) {
          const addedBrand = await response.json();
          console.log("brand added: ", addedBrand);
          this.$emit("brandAdded", addedBrand);
        }
      } catch (error) {
        console.error("error: ", error);
      }
    },
  },
};
</script>
