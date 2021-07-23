<template>
    <div>
        <Camera v-on:takePicture='this.takePicture'/>
        <Gallery v-on:submit='this.submit'/>
    </div>
</template>

<script>
import Camera from './Camera.vue'
import Gallery from './Gallery.vue'
export default {
  name: 'CAM',
  components: {
    Camera,
    Gallery
  },
  methods: {
    takePicture () {
      console.log('캡처되었습니다.')
      let ratio = (window.innerHeight < window.innerWidth) ? 16 / 9 : 9 / 16
      const picture = document.querySelector('canvas')
      picture.width = (window.innerWidth < 1280) ? window.innerWidth : 1280
      picture.height = window.innerWidth / ratio
      const ctx = picture.getContext('2d')
      ctx.imageSmoothingEnabled = true
      ctx.imageSmoothingQuality = 'high'
      ctx.drawImage(document.querySelector('video'), 0, 0, picture.width, picture.height)
    },
    submit () {
      let ratio = (window.innerHeight < window.innerWidth) ? 16 / 9 : 9 / 16
      const sendImage = document.querySelector('canvas')
      sendImage.width = (window.innerWidth < 1280) ? window.innerWidth : 1280
      sendImage.height = window.innerWidth / ratio
      const ctx = sendImage.getContext('2d')
      ctx.imageSmoothingEnabled = true
      ctx.imageSmoothingQuality = 'high'
      ctx.drawImage(document.querySelector('video'), 0, 0, sendImage.width, sendImage.height)
      console.log(ctx)
    }
  }
}
</script>
