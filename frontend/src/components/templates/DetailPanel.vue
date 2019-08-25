<template>
  <v-card xs12 color="grey darken-2">
    <v-card-title>Detail</v-card-title>
    <v-spacer></v-spacer>
    <DetailForm/>
    <v-layout>
      <v-flex xs12>
        <v-card-actions>
          <v-btn text @click="click_1()">Update</v-btn>
          <v-btn text @click="click_2()">Delete</v-btn>
        </v-card-actions>
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>
import DetailForm from "@/components/organisms/DetailForm.vue";

export default {
  name: "DetailPanel",
  components: {
    DetailForm
  },
  data: () => ({}),
  methods: {
    click_1() {
      this.$router.push({ path: "/Update" });
    },
    click_2() {
      this.$router.push({ path: "/Delete" });
    }
  }
};
</script>

<style scoped>
.v-input__slider {
  width: 100%;
}
</style>