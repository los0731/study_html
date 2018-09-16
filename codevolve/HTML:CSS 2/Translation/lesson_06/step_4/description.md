# CSS
### <body>

Medium 정책 페이지는 body 태그에 `font-size`, `font-size`, `color`, `line-height `와 같이 적용된 스타일이 많습니다. 이들의 공통점은 속성이 하위 태그에도 적용된다는 점 입니다. 그래서 사이트 전체의 기준이 되는 서체, 서체 크기, 서체 색상을 기준으로 정하고 시작할때 이렇게 최상위 태그인 body 태그에 속성을 부여합니다. body 태그에 스타일을 적용합시다.

* The margin of `body` is `0`.
* Padding is `0`.
* The font is `'Source Serif Pro', serif`.
* The font size is `19px`.
* 행간은 `1.58`입니다.
* The font color is `#333`.
* Apply Anti-Aliasing.


**Instructions**
1. Apply style to `body`.
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



### .navbar 

로고 텍스트가 있는 네비게이션 바의 스타일을 정의해봅시다. 

* `.navbar`의 아래 패딩은 `8px`입니다.
* The letters are centered.
* The font is `'Playfair Display', serif`.
* The font size is `39px`.
* 글씨 두께는 `bold`입니다.
* 행간은 `56px`입니다.


**Instructions**
1. Apply style to `.navbar`.
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



### .hero 

이 페이지의 성격을 나타내는 히어로 이미지의 스타일을 지정해 봅시다. 배경에 사용하는 이미지는 [PEXELS][https://www.pexels.com/] 에서 찾아 이미지 주소를 복사해왔습니다.

* The width of `.hero` is `100%`.
* The height is `30vw`.
* Minimum height is `200px`.
* The maximum height is `534px`.
* 배경 이미지의 url/반복/x축 정렬/y축 정렬은 각각 `url("https://images.pexels.com/photos/840996/pexels-photo-840996.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260") no-repeat center center`입니다.
* 배경 이미지가 모든 영역을 덮어 씁니다.


**Instructions**
1. Apply style to `.hero`
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



Click the **NEXT STEP** button.



## TIPS!

- `background-size: cover;`은 어떤 의미인가요?

  > 배경 이미지를 넣을 공간에 넓이와 높이를 설정하고, 이미지의 url을 가져오면 이미지를 넣을 수 있습니다. 다만 이미지 사이즈의 비율이 고려되지 않고 공간에 들어가기 때문에, 전체 이미지를 보여주기 위해서는 `background-size`속성을 `cover`로 설정해주어야 합니다.   




