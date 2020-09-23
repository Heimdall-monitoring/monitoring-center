<template>
    <div class="probe">
        <h3>{{ probe.name }}</h3>
        <h4>{{ probe.description }}</h4>
    </div>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';
import Probe from '@/models/probe';

@Component
export default class SimpleProbe extends Vue {
    @Prop() private probe!: Probe;

    mounted() {
      console.log(this.probe);
    }
}
</script>

<style lang="scss" scoped>

</style>
