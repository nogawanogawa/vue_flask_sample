<template>
  <v-app id="inspire">
    <Sidebar/>
    <v-content>
      <v-container fluid fill-height>
        <v-layout justify-center>
          <v-flex xs12>
            <UpdatePanel/>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import Sidebar from "@/components/templates/Sidebar.vue";
import UpdatePanel from "@/components/templates/UpdatePanel.vue";

export default {
  name: "SearchPage",
  components: {
    Sidebar,
    UpdatePanel
  },
  props: {
    source: String
  },
  created() {
    this.$vuetify.theme.dark = true;
  }
};
</script>