# 스타일
## body
페이스북 디자인 페이지는 배경의 아주 약한 grey를 사용합니다. 또 전체 영역에 별도의 서체를 지정하고 있어요.
* `body`의 배경 컬러는 `#FCFCFC`입니다.
* 서체는 `'San Francisco', -apple-system, BlinkMacSystemFont, '.SFNSText-Regular', Roboto, 'Helvetica Neue', Helvetica, Arial, sans-serif`입니다.


**Instructions**
1. `body`의 스타일 적용하기. 
    ```css
    body {
    	background-color: #FCFCFC;
    	font-family: 'San Francisco', -apple-system, BlinkMacSystemFont, '.SFNSText-Regular', Roboto, 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    ```



## 카드
카드의 스타일을 지정해 봅시다.  

* `.card`의 마진은 margin은 상-하 `80px` 좌-우 `auto`입니다.
* 최대 넓이는 `350px`입니다.
* 그림자는 x축 `0`, y축 `20px`, 퍼짐(blur) `20px`, 컬러 `rgba(0, 0, 0,.08)` 입니다. 
* 외곽 모서리의 반지름은 `3px`입니다.
* Transition은 `.24s`입니다.


**Instructions**
1. `.card`클래스의 스타일 적용하기.
    ```css
    .card {
    	margin: 80px auto;
    	max-width: 350px;
    	box-shadow: 0 20px 20px rgba(0, 0, 0,.08);
        border-radius: 3px;
    	transition: .24s;
    }
    ```



## 카드에 마우스를 올렸을 때.
Hover는 해당 요소에 마우스를 올린 상태를 말합니다. 마우스를 사용하는 데스크탑에서 클릭이 가능한 상태라는걸 설명하는 가장 좋은 UI가 hover입니다. 카드의 hover 스타일을 지정해봅시다. 위에 사용한 `transition: .24s;`에 의해서, 일반 상태에서 hover 상태로, hover 상태에서 일반 상태로 더 부드럽게 변화하게 됩니다.

* `.card:hover`의 그림자는 x축 `0`, y축 `40px`, 퍼짐(blur) `40px`, 컬러 `rgba(0, 0, 0,.16)` 입니다.
* 위로 20px만큼 이동합니다.


**Instructions**
1. `.card:hover`클래스의 스타일 적용하기.
    ```css
    .card:hover {
    	box-shadow: 0 40px 40px rgba(0, 0, 0,.16);
    	transform: translateY(-20px);
    }
    ```



## a 태그
이 카드는 hypertext가 적용되어 있어서, blue 컬러와 underline이 적용되어 있습니다. 따라서 a 태그에서 이런 데코레이션들을 제거해 주어야 합니다. 

* `a`의 `text-decoration`은 `none`입니다.
* 글씨 컬러는 `#1D2129`입니다.

**Instructions**
1. `a`의 스타일 적용하기.
    ```css
    a {
    	text-decoration: none;
    	color: #1D2129;
    }
    ```





다음 스탭에서 카드의 세부 요소들을 스타일링 합니다. **NEXT STEP** 버튼을 클릭하세요.

