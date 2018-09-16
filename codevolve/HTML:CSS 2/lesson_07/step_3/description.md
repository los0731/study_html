# CSS
### <body>
페이스북 디자인 페이지는 배경의 아주 연한 회색을 사용합니다. 또 전체 영역에 별도의 서체를 지정하고 있어요.
* `body`의 배경 색상은 `#FCFCFC`입니다.
* 서체는 `'San Francisco', -apple-system, BlinkMacSystemFont, '.SFNSText-Regular', Roboto, 'Helvetica Neue', Helvetica, Arial, sans-serif`입니다. (실제 facebook design의 서체입니다.)


**Instructions**
1. `body`의 스타일 적용하기. 
    ```css
    body {
    	background-color: #FCFCFC;
    	font-family: 'San Francisco', -apple-system, BlinkMacSystemFont, '.SFNSText-Regular', Roboto, 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    ```



### .card
카드의 스타일을 지정해 봅시다.  

* `.card`의 마진은 상/하 `80px`좌/우 `auto`입니다.
* 최대 넓이는 `350px`입니다.
* 그림자의 x축/y축/퍼짐(blur)/크기/색상은 `0 20px 20px 0 rgba(0, 0, 0,.08)`입니다. 
* 모서리의 둥글기는 `3px`입니다.
* `transition` 속성은 `.24s`입니다.


**Instructions**
1. `.card`의 스타일 적용하기.
    ```css
    .card {
    	margin: 80px auto;
    	max-width: 350px;
    	box-shadow: 0 20px 20px rgba(0, 0, 0,.08);
        border-radius: 3px;
    	transition: .24s;
    }
    ```



### .card:hover
`:hover`는 해당 요소에 마우스를 올린 상태를 말합니다. 마우스를 사용하는 데스크탑에서 클릭이 가능한 상태라는걸 설명하는 가장 좋은 UI가 hover입니다. 카드의 hover 스타일을 지정해봅시다. 위에 사용한 `transition: .24s;`에 의해서, 일반 상태에서 hover 상태로, hover 상태에서 일반 상태로 더 부드럽게 변화하게 됩니다.

* `.card:hover`의 그림자는 x축/y축/퍼짐(blur)/크기/색상은 `0 40px 40px 0 rgba(0, 0, 0,.16)`입니다.
* `transform` 을 사용하여 위로 `20px` 움직입니다.


**Instructions**
1. `.card:hover`의 스타일 적용하기.
    ```css
    .card:hover {
    	box-shadow: 0 40px 40px rgba(0, 0, 0,.16);
    	transform: translateY(-20px);
    }
    ```



### <a>
`<a>`에는 기본적으로 글씨에 파랑색과 밑줄이 적용되어 있습니다. 따라서 별도로 스타일을 지정하여 장식 요소들을 제거해야 합니다. 

* `a`의 글씨의 장식이 없습니다.
* 글씨 색상은 `#1D2129`입니다.

**Instructions**
1. `a`의 스타일 적용하기.
    ```css
    a {
    	text-decoration: none;
    	color: #1D2129;
    }
    ```





다음 스탭에서 카드의 세부 요소들을 스타일링 합니다. **NEXT STEP** 버튼을 클릭하세요.





## TIPS!

- 트렌지션 속성

  > **CSS 트랜지션(transitions)**은 CSS 속성을 변경할 때 애니메이션 속도를 조절하는 방법을 제공합니다. 속성 변경이 즉시 영향을 미치게 하는 대신, 그 속성의 변화가 일정 기간에 걸쳐 일어나도록 할 수 있습니다. 예를 들어, 여러분이 어떤 요소의 색상을 흰색에서 검은색으로 변경한다면, 변화는 대개 즉시 일어납니다. CSS 트랜지션을 이용하면, 모두 커스터마이즈 가능한 어떤 가속도 곡선을 따르는 시간 주기마다 변화가 일어납니다.
  >
  > 출처: [모질라 CSS 트랜지션][https://developer.mozilla.org/ko/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions]