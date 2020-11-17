<template>
  <div id="app">
    <h1>TodoList</h1>
    <h2>완료 된 일: {{ completedTodosCount }}</h2>
    <h2>완료 되지 않은 일: {{ uncompletedTodosCount }}</h2>
    <TodoList/>
    <TodoForm/>
  </div>
</template>

<script>
import TodoList from '@/components/TodoList'
import TodoForm from '@/components/TodoForm'

export default {
  name: 'App',
  components: {
    TodoList,
    TodoForm,
  },
  computed: {
    completedTodosCount: function () {
      return this.$store.getters.completedTodosCount
    },
    uncompletedTodosCount: function () {
      return this.$store.getters.uncompletedTodosCount
    },
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
</style>
