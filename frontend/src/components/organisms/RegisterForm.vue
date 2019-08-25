<template>
  <v-container fluid grid-list-xl>
    <v-layout wrap align-center>
      <v-flex xs12 sm4 d-flex>
        <v-select :items="titles" v-model="title" label="Title" outlined></v-select>
      </v-flex>
      <v-flex xs12 sm4 d-flex>
        <v-select :items="categories" v-model="category" label="Category" outlined></v-select>
      </v-flex>
      <v-flex xs12 sm4 d-flex>
        <v-select :items="contents" v-model="content" label="Content" outlined></v-select>
      </v-flex>
      <v-flex xs10 offset-xs1>
        <v-btn
          v-if="!alert"
          block
          color="secondary"
          dark
          @click="create({'title':title, 'category':category, 'content':content})"
        >Register</v-btn>
      </v-flex>
    </v-layout>
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
  </v-container>
</template> 

<script>
import { mapActions } from "vuex";
export default {
  name: "RegisterForm",
  methods: {
    ...mapActions(["create"])
  },
  data: () => ({
    titles: ["potato", "onion", "curry", "poak"],
    categories: ["food", "vagitable", "meat"],
    contents: ["good", "not good", "not bad", "bad"],
    alert: false
  })
};
</script>