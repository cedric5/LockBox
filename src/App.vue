<template>

  <div id="app">
    <Menu></Menu>
    <router-view />
  </div>
</template>

<script>
import Menu from "@/components/Menu.vue";

export default {
  name: "menu",
  components: {
    Menu
  }
};
</script>