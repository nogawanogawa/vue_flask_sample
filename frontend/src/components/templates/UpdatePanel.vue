<template>
  <v-card xs12 color="grey darken-2">
    <v-card-title>Update</v-card-title>
    <v-spacer></v-spacer>
    <UpdateForm/>
  </v-card>
</template>

<script>
import UpdateForm from "@/components/organisms/UpdateForm.vue";

export default {
  name: "DetailPanel",
  components: {
    UpdateForm
  },
  data: () => ({}),
  methods: {
    click() {
      this.$router.push({ path: "/Home" });
    }
  }
};
</script>

<style scoped>
.v-input__slider {
  width: 100%;
}
</style>