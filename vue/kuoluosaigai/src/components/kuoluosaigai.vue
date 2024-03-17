<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <button @click="incrementCount">{{ count }}</button>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      count: 0 // 初始化计数器为0
    };
  },
  methods: {
    incrementCount() {
      this.count += 1; // 点击时增加计数
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

.custom-button {
  font-size: 18px; /* 设置字体大小 */
  padding: 500px 500px; /* 设置内边距以增大按钮面积 */
  width: 300px; /* 设置固定宽度 */
  height: 500px; /* 设置固定高度 */
}
</style>
