```javascript
<body>
    <h1>Dog API</h1>
    <button id="get-dog-button">댕댕이내놔</button>
    <button id="get-cat-button">고양이내놔</button>
    <hr>
    <div id="animals"></div>

    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script>
        const DOG_API_URL = 'https://dog.ceo/api/breeds/image/random'
        const CAT_API_URL = 'https://api.thecatapi.com/v1/images/search'

        function getDog () {
            // 'Axios'를 사용해서 DOG API에 GET 요청을 보낸다.
            axios.get(DOG_API_URL)
            // 정상적으로 응답이 오면, 
              .then(function (res) {
                // 이미지 요소 만들기(크기 너무 크면 알아서 조절)
                const dogImg = document.createElement('img')
                const dogImgSrc = res.data.message
                // dogImg.src = dogImgSrc, 아래 코드와 같음.
                dogImg.setAttribute('src', dogImgSrc)
                dogImg.setAttribute('width', 300)
                dogImg.setAttribute('height', 400)
                
                // animals div에 이미지 요소 추가하기
                animalsDiv.append(dogImg)
              })
            // 이미지 URL을 활용해서 화면에 강아지 사진을 띄워준다. (or 사진을 계속 추가)
              .catch(function (err) {
                  console.log(err)
              })
        }

        function getCat () {
            axios.get(CAT_API_URL)
                .then(function (res) {
                    const catImg = document.createElement('img')
                    const catImgSrc = res.data[0].url
                    catImg.src = catImgSrc
                    catImg.width = 300
                    catImg.height = 350
                    
                    animalsDiv.append(catImg)
                })

                .catch(function (err) {
                    console.log(err)
                })
        }

        // '댕댕이내놔' 버튼을 클릭했을 경우
        const getDogButton = document.querySelector('#get-dog-button')
        const getCatButton = document.querySelector('#get-cat-button')
        const animalsDiv = document.querySelector('#animals')
        
        getDogButton.addEventListener('click', getDog)
        getCatButton.addEventListener('click', getCat)
    </script>
```

