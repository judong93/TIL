import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [
      { title: 'Vue-tube 다시 만들어보기', completed: false},
      { title: 'Vue-Todo List 다시 만들어보기', completed: false},
    ]
  },
  getters: {
    completedTodosCount: function (state) {
      return state.todos.filter(todo => {
        return todo.completed
      }).length
    },
    uncompletedTodosCount: function (state) {
      return state.todos.filter(todo => {
        return !todo.completed
      }).length
    },
  },
  mutations: {
    CREATE_TODO: function (state, todoItem) {
      state.todos.push(todoItem)
    },
    DELETE_TODO: function (state, todoItem) {
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1)
    },
    UPDATE_TODO_STATUS: function (state, todoItem) {
      state.todos = state.todos.map(todo => {
        // 수정 대상이 맞으면 completed를 바꿔서 return
        if (todo === todoItem) {
          return {
            ...todo,
            completed: !todo.completed
          }
        }
        // 수정 대상이 아니면 원본 그대로 return
        return todo
      })
    }
  },
  actions: {
    createTodo: function ({ commit }, todoItem) {
      commit('CREATE_TODO', todoItem)
    },
    deleteTodo: function ({ commit }, todoItem) {
      commit('DELETE_TODO', todoItem)
    },
    updateTodoStatus: function({ commit }, todoItem) {
      commit('UPDATE_TODO_STATUS', todoItem)
    },
  },
})
