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
    </v-layout>
  </v-container>
</template> 

<script>
export default {
  name: "DetailForm",
  data: () => ({})
};
</script>