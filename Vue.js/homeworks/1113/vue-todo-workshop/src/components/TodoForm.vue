<template>
  <div>
    <input v-model.trim="todoTitle"
     @keypress.enter="createTodo" 
     type="text"
    >
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
            const todoItem = {
                title: this.todoTitle,
                completed: false,
            }
            // &&todoItem.title.trim() 이걸 그냥 v-model.trim 쓰면 같은로직임.
            if (todoItem.title) {
                this.$store.dispatch('createTodo', todoItem)
            }
            this.todoTitle = ''
        },
    }
}
</script>

<style>

</style>