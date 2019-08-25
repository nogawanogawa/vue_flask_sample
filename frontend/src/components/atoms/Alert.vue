<template>
  <div>
    <v-alert
      v-model="alert"
      border="left"
      close-text="Close Alert"
      color="success"
      dark
      dismissible
    >登録成功</v-alert>
  </div>
</template>

<script>
export default {
  name: "Alert",
  data() {
    return {
      alert: true
    };
  }
};
</script>