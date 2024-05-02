<template>
  <HelloWorld msg="阔落塞该"/>

  <footer>
    <p>Copyright © 2024 阔落塞该. All rights reserved.</p>
    <p>
      <a href="https://beian.miit.gov.cn/" rel="noreferrer" target="_blank" class="link-space">鄂ICP备17026678号-3</a>
      <a href="https://beian.mps.gov.cn/#/query/webSearch?code=42050302000428" rel="noreferrer" target="_blank" class="link-space">鄂公网安备42050302000428</a>
    </p>
  </footer>
</template>

<script>
import HelloWorld from './components/kuoluosaigai.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
footer {
  text-align: center;
  padding: 1rem;
  background-color: #f7f8fc;
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
}
.link-space {
  margin-right: 10px;
}
a {
  color: #000;
}

a:visited {
  color: #000;
}

a:hover {
  color: #42b983;
}

a:active {
  color: #000;
}
</style>
