<template>
  <v-app id="inspire">
    <Sidebar/>
    <v-content>
      <v-container fluid fill-height>
        <v-layout justify-center>
          <v-container fluid grid-list-lg pa-2>
            <v-layout>
              <v-flex xs12>
                <ItemPanel/>
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
import ItemPanel from "@/components/templates/ItemPanel.vue";

export default {
  name: "SearchPage",
  components: {
    Sidebar,
    ItemPanel
  },
  props: {
    source: String
  },
  data: () => ({}),
  created() {
    this.$vuetify.theme.dark = true;
  }
};
</script>