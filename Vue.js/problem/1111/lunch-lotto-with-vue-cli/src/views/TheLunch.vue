<template>
  <div>
    <CaptainYoungji/>
    <h2>점심메뉴 추천</h2>
    <button @click="pickOneInLunchMenu">Pick My Lunch Menu!</button>
    <p>오늘의 점심 메뉴: {{ selectedLunchMenu }}</p>
  </div>
</template>

<script>
import _ from 'lodash'
import CaptainYoungji from '@/components/CaptainYoungji.vue'

export default {  
  name: 'TheLunch',
  // 2. 컴포넌트 사용 등록하기
  components: {
    CaptainYoungji
  },
  data: function () {
    return {
      lunch: ['국밥', '짜장면', '햄버거'],
      selectedLunchMenu: '',
    }
  },
  methods: {
    pickOneInLunchMenu: function () {
      const randomIndex = _.random(this.lunch.length - 1)
      // console.log(randomIndex)
      this.selectedLunchMenu = this.lunch[randomIndex]
    }
  }
}
</script>

<style>

</style>
