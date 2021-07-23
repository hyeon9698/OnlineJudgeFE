<template>
    <div class="camera">
        <video autoplay class="feed"></video>
        <button class="snap" v-on:click="$emit('takePicture')">캡처</button>
        <Gallery />
    </div>
</template>


<script>
import Gallery from './Gallery.vue'
export default {
  name: 'camera',
  components: Gallery,
  methods: {
    init () {
      if ('mediaDevices' in navigator && 'getUserMedia' in navigator.mediaDevices) {
        let constraints = {
          video: {
            width: {
              min: 640,
              ideal: 1280,
              max: 1920
            },
            height: {
              min: 360,
              ideal: 720,
              max: 1080
            }
          }
        }
        navigator.mediaDevices.getUserMedia(constraints).then(stream => {
          const videoPlayer = document.querySelector('video')
          videoPlayer.srcObject = stream
        }).catch(console.error)
      }
    }
  },
  beforeMount () {
    this.init()
  }
}
</script>
