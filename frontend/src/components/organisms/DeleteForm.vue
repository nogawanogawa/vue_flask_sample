<template>
  <v-container fluid grid-list-xl>
    <v-layout wrap align-center>
      <v-flex xs12 sm4 d-flex>
        <v-text-field v-model="$store.state.title" label="Title" outlined disabled></v-text-field>
      </v-flex>
      <v-flex xs12 sm4 d-flex>
        <v-text-field v-model="$store.state.category" label="Category" outlined disabled></v-text-field>
      </v-flex>
      <v-flex xs12 sm4 d-flex>
        <v-text-field v-model="$store.state.content" label="Content" outlined disabled></v-text-field>
      </v-flex>
      <v-flex xs10 offset-xs1>
        <v-btn
          v-if="!alert"
          block
          color="secondary"
          dark
          @click="del({'index':$store.state.index, 'title':title, 'category':category, 'content':content});click()"
        >Delete</v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template> 

<script>
import { mapActions } from "vuex";

export default {
  name: "DeleteForm",
  methods: {
    ...mapActions(["del"]),
    click() {
      alert("削除完了");
      this.$router.push({ path: "/Detail" });
    }
  },
  data: () => ({
    items: ["a", "b", "c", "d"],
    alert: false
  })
};
</script>