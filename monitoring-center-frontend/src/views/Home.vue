<template>
  <div class="home">
    (TMP) List of current configured probes
    <probes-list></probes-list>
  </div>
</template>

<script>
import ProbesList from '@/components/ProbesList.vue';

export default {
  name: 'Home',
  components: {
    ProbesList,
  },
};
</script>
