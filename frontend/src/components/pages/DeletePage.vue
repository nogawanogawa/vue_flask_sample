<template>
  <v-app id="inspire">
    <Sidebar/>
    <v-content>
      <v-container fluid fill-height>
        <v-layout justify-center>
          <v-flex xs12>
            <DeletePanel/>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import Sidebar from "@/components/templates/Sidebar.vue";
import DeletePanel from "@/components/templates/DeletePanel.vue";

export default {
  name: "SearchPage",
  components: {
    Sidebar,
    DeletePanel
  },
  props: {
    source: String
  },
  created() {
    this.$vuetify.theme.dark = true;
  }
};
</script>