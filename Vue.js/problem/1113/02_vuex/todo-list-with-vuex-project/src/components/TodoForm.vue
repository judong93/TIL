<template>
  <div>
      <input type="text" v-model.trim="todoTitle" @keypress.enter="createTodo">
      <button @click="createTodo">Add</button>
  </div>
</template>

<script>
export default {
    name: 'TodoForm',
    data: function () {
        return {
            todoTitle: '',
        }
    },
    methods: {
        createTodo: function () {
            // console.log(this.$store)
            const todoItem = {
                title: this.todoTitle,
                completed: false,
            }
            // this.$store.commit('CREATE_TODO', todoItem)
            // &&todoItem.title.trim() 이걸 그냥 v-model.trim 쓰면 같은로직임.
            if (todoItem.title) {
                this.$store.dispatch('createTodo', todoItem)
            }
            this.todoTitle = ''
        }
    }
}
</script>

<style>

</style>