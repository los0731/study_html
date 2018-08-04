# CSS
### body

Medium 정책 페이지는 body 태그에 `font-size`, `font-size`, `color`, `line-height `와 같이 적용된 스타일이 많습니다. 이들의 공통점은 속성이 하위 태그에도 적용된다는 점 입니다. 그래서 사이트 전체의 기준이 되는 서체, 서체 크기, 서체 색상을 기준으로 정하고 시작할때 이렇게 최상위 태그인 body 태그에 속성을 부여합니다. body 태그에 스타일을 적용합시다.

* `body`의 마진은 `0`입니다.
* 패딩은 `0`입니다.
* 서체는 `'Source Serif Pro', serif`입니다.
* 글씨 크기는 `19px`입니다.
* 글씨 색상은 `#333`입니다.
* 행간은 `1.58`입니다.*
* 이 태그에는 안티앨리어싱을 적용합니다.*


**Instructions**
1. `body`의 스타일 적용하기. 
    ```css
    body {
    	margin: 0;
    	padding: 0;
    	font-family: 'Source Serif Pro', serif;
    	font-size: 19px;
    	line-height: 1.58;
    	color: #333;
    	-webkit-font-smoothing: antialiased;
    }
    ```



### 네비게이션 바

로고 텍스트가 있는 네비게이션 바의 스타일을 정의해봅시다. 

* `.navbar`의 아래 패팅은 `8px`입니다.
* 글은 가운데 정렬입니다.
* 서체는 `'Playfair Display', serif`입니다.
* 글씨 크기는  `39px`입니다.
* 글씨 두깨는 `bold`입니다.
* 행간은 `56px`입니다.


**Instructions**
1. `.navbar`의 스타일 적용하기.
    ```css
    .navbar {
        padding-bottom: 8px;
        text-align: center;
        font-family: 'Playfair Display', serif;
        font-size: 39px;
        font-weight: bold;
        line-height: 56px;
    }
    ```



### 히어로 이미지

이 페이지의 성격을 나타내는 히어로 이미지의 스타일을 지정해 봅시다. 배경에 사용하는 이미지는 [PEXELS][https://www.pexels.com/] 에서 찾아 이미지 주소를 복사해왔습니다.

* `.hero`의 넓이는 `100%`입니다.
* 높이는 `30vw`입니다.*
* 최소 높이는 `200px`입니다.
* 최대 높이는 `534px`입니다.
* 배경 이미지의 url/반복/x축 정렬/y축 정렬은 각각 `url("https://images.pexels.com/photos/840996/pexels-photo-840996.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260") no-repeat center center`입니다.
* 배경 이미지가 모든 영역을 덮어 씁니다.*


**Instructions**
1. `.hero`의 스타일 적용하기.
    ```css
    .hero {
        width: 100%;
        min-height: 200px;
        height: 30vw;
        max-height: 534px;
        background: url('https://images.pexels.com/photos/840996/pexels-photo-840996.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260') no-repeat center center;
        background-size: cover;
    }
    ```



**NEXT STEP** 버튼을 클릭하세요.



# TIPS!

- `background-size: cover;`은 어떤 의미인가요?

  > 배경 이미지를 넣을 공간에 넓이와 높이를 설정하고, 이미지의 url을 가져오면 이미지를 넣을 수 있습니다. 다만 이미지 사이즈의 비율이 고려되지 않고 공간에 들어가기 때문에, 전체 이미지를 보여주기 위해서는 `background-size`속성을 `cover`로 설정해주어야 합니다.   




