<template>
  <v-card xs12 color="grey darken-2">
    <v-card-title>Register</v-card-title>
    <v-spacer></v-spacer>
    <RegisterForm/>
  </v-card>
</template>

<script>
import RegisterForm from "@/components/organisms/RegisterForm.vue";

export default {
  name: "RegisterPanel",
  components: {
    RegisterForm
  },
  data: () => ({
    flat: false,
    media: true,
    loading: false,
    actions: true,
    outlined: false,
    elevation: undefined,
    raised: false,
    width: 344,
    height: undefined
  })
};
</script>

<style scoped>
.v-input__slider {
  width: 100%;
}
</style>