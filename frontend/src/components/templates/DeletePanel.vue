<template>
  <v-card xs12 color="grey darken-2">
    <v-card-title>Delete</v-card-title>
    <v-spacer></v-spacer>
    <DeleteForm/>
  </v-card>
</template>

<script>
import DeleteForm from "@/components/organisms/DeleteForm.vue";

export default {
  name: "DetailPanel",
  components: {
    DeleteForm
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