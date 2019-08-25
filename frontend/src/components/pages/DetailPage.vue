<template>
  <v-app id="inspire">
    <Sidebar/>
    <v-content>
      <v-container fluid fill-height>
        <v-layout justify-center>
          <v-container fluid grid-list-lg pa-2>
            <v-layout>
              <v-flex xs12>
                <DetailPanel/>
              </v-flex>
            </v-layout>
          </v-container>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>


<script>
import Sidebar from "@/components/templates/Sidebar.vue";
import DetailPanel from "@/components/templates/DetailPanel.vue";

export default {
  name: "SearchPage",
  components: {
    Sidebar,
    DetailPanel
  },
  props: {
    source: String
  },
  created() {
    this.$vuetify.theme.dark = true;
  }
};
</script>