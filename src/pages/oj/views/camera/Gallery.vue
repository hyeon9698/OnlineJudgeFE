<template>
  <div>
    <canvas></canvas>
    <button class="snap" v-on:click="$emit('submit')">보내기</button>
  </div>
</template>
<script>
export default {
  name: 'gallery'
}
</script>
