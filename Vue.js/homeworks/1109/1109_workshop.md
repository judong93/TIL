```html
    <div id="app">
        <button @click="pickLunch">점심 메뉴 선택!</button>
        <p>{{ selectedLunch }}</p>
        <hr>
        <button @click="pickLotto">로또 번호!</button>
        <p>{{ lotto }}</p>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.20/lodash.min.js">		</script>
    <script>
        const app = new Vue({
            el: '#app',
            data: {
                lunchMenu: ['떡볶이', '스테이크', '파스타'],
                selectedLunch: '',
                lottoNumbers: _.range(1, 46),
                lotto: '',
            },
            methods: {
                pickLunch: function () {
                    this.selectedLunch = _.sample(this.lunchMenu)
                },
                pickLotto: function () {
                    const randomNumbers = _.sampleSize(this.lottoNumbers, 6)
                    const sortedNumbers = _.sortBy(randomNumbers)
                    this.lotto = sortedNumbers
                }
            },
        })
    </script>
```

