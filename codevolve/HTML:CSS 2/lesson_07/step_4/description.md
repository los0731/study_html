# 스타일
## body
바디의 스타일을 지정해 봅시다.  

* `body`의 마진과 패딩은 모두 `0`입니다.
* `body`의 서체는 `"Times New Roman", Times, serif`입니다.
* `body`의 폰트 컬러는 `#333`입니다.
* `body`의 폰트 사이즈는 `18px`입니다.
* `body`의 행간은 `1.58`입니다.


**Instructions**
1. `body`의 스타일 적용하기. 
    ```css
    body {
        margin: 0;
        padding: 0;
        font-family: "Times New Roman", Times, serif;
    	color: #333;
        font-size: 18px;
        line-height: 1.58;
    }
    ```

## 네비게이션바
네비게이션바의 스타일을 지정해 봅시다.

* `.navbar`의 폰트 사이즈는 `32px`입니다.
* `.navbar`의 폰트 굵기는 `900`입니다.
* `.navbar`의 행간은 `64px`입니다.
* `.navbar`의 텍스트 정렬 방식은 `center`입니다.


**Instructions**
1. `.navbar`클래스의 스타일 적용하기.
    ```css
    .navbar {
    	font-size: 32px;
        font-weight: 900;
        line-height: 64px;
        text-align: center;
    }
    ```

## 이미지
페이지의 성격을 나타내는 hero 이미지의 스타일을 지정해 봅시다.

* `.hero`의 넓이는 `100%`입니다.
* `.hero`의 높이는 `320px`입니다.
* `.hero`의 배경 이미지는 `'https://images.pexels.com/photos/872957/pexels-photo-872957.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260'`입니다.
* `hero`의 배경 사이즈는 `cover`*입니다.


**Instructions**
1. `.hero`클래스의 스타일 적용하기.
    ```css
    .hero {
    	width: 100% 
        height:320px;
        background: url('https://images.pexels.com/photos/872957/pexels-photo-872957.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260') no-repeat center;
        background-size: cover;  
    }
    ```

## TIPS!

- `background-size: cover;`은 어떤 의미인가요?

  > 배경 이미지를 넣을 공간에 넓이와 높이를 설정하고, 이미지의 url을 가져오면 이미지를 넣을 수 있습니다. 다만 이미지 사이즈의 비율이 고려되지 않고 공간에 들어가기 때문에, 전체 이미지를 보여주기 위해서는 `background-size`속성을 `cover`로 설정해주어야 합니다.   


다음 스탭에서 페이지의 본문을 스타일링 합니다. **NEXT STEP** 버튼을 클릭하세요.

