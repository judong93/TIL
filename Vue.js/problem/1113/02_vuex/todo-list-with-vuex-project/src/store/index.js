import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [
      { title: '할 일1', completed: false},
      { title: '할 일2', completed: false},
    ]
  },
  getters: {
    completedTodosCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.completed === true
      }).length
    },
    uncompletedTodosCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.completed === false
      }).length
    }
  },
  mutations: {
    CREATE_TODO: function (state, todoItem) {
      // console.log('CREATE TODO CALL')
      // console.log(todoItem)
      // console.log(state.todos)
      state.todos.push(todoItem)
    },
    DELETE_TODO: function (state, todoItem) {
      const index = state.todos.indexOf(todoItem) // 유니크한 
      // ID값이 없으므로 indexOf를 사용!
      state.todos.splice(index, 1) // index부터 1개를 삭제하고
      // 기본 배열을 다시 만들겠다.
    },
    UPDATE_TODO_STATUS: function (state,todoItem) {
      //1. todos 배열을 반복하며
      state.todos = state.todos.map((todo) => {
        //2. 꺼내지는 todo가 들어온 todoItem과 동일한 경우
        if (todo === todoItem) {
          // 그 요소의 completed를 반대값으로 return
          return {
            ...todo,
            completed: !todo.completed
          }
        }
        //4. 같지 않으면 그대로 리턴
        return todo
      })
    }
  },
  actions: {
    createTodo: function ({ commit }, todoItem) {
      // console.log('createTOdo from actions called!')
      // console.log(context)
      // context.commit('CREATE_TODO', todoItem)

      // destructuring을 활용
      commit('CREATE_TODO', todoItem)
    },
    deleteTodo: function ({ commit }, todoItem) {
      commit('DELETE_TODO', todoItem)
    },
    updateTodoStatus: function ({ commit }, todoItem) {
      commit('UPDATE_TODO_STATUS', todoItem)
    },
  },
})
