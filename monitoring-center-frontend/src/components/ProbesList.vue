<template>
    <div>
        list:
        <div v-for="probe in probes" :key="probe.uuid">
          <simple-probe :probe="probe"></simple-probe>
        </div>
    </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Probe from '@/models/probe';
import SimpleProbe from '@/components/SimpleProbe.vue';
import ProbeService from '@/utils/ProbeService';

@Component({
  components: {
    SimpleProbe,
  },
})
export default class ProbesList extends Vue {
    private probes: Probe[] = [];

    private probesService: ProbeService = new ProbeService('http://localhost:5000/api');

    refreshList() {
      this.probesService.getAllProbes()
        .then((probes) => {
          this.probes = probes;
          // console.log(this.probes);
        })
        .catch((e) => {
          console.error(e);
        });
    }

    mounted() {
      this.refreshList();
    }
}
</script>
