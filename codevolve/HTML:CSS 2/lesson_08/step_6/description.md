## .navigation
네비게이션 부분의 스타일을 정의해봅시다. 우선 네비게이션 안에는 `<div class="nav-left">`와 `<div class="nav-right">`가 있는데, 이 두개의 `<div>`를 좌/우에 배치해야합니다. 내부 요소들을 가로로 배치하기 좋은 방법은 `flex`를 이용하는 것입니다.

* `.navigation`의 `display`는 `flex`입니다.
* `flex`가 적용된 내부 요소들이 수직으로 중앙 정렬합니다.   
* `flex`가 적용된 내부 요소들이 좌/우 끝에 배치되도록 합니다.
* 패딩은 상/우/하/좌 `16px 30px 16px 10px`입니다.


**Instructions**
1. `.navigation`의 스타일 적용하기.
    ```css
    .navigation {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 16px 30px 16px 10px;
    }
    ```



## .navigation a
네비게이션 안에 있는 `a`의 스타일을 정리합니다.    

- `.navigation a`의 왼쪽 마진은 `15px`입니다.
- 글씨 크기는 `13px`입니다.
- 행간은 `16px`입니다.
- 글씨 색상은 `#333`입니다.

**Instructions**

1. `.navigation a`의 스타일 적용하기.
   ```css
   .navigation a {
     margin-left: 15px;
     font-size: 13px;
     line-height: 16px;
     color: #333;
   }
   ```



## .navigation a:hover:not(.btn)
네비게이션 안에 있는 `a:hover`에 대한 스타일이 필요합니다. 거기에 더해서 `.btn`를 가진 `<a>`는 별도의 스타일을 정의할 것이기 때문에, 여기서는 제외 해야합니다. 따라서 `:hover`와 `:not`선택자를 같이 활용합니다.   
- `.navigation a:hover:not(.btn)`의 투명도는 `.85`입니다.
- 글씨에 `underline`이 적용됩니다.


**Instructions**
1. `.navigation a:hover:not(.btn)`의 스타일 적용하기.
   ```css
   .navigation a:hover:not(.btn) {
     opacity: .85;
     text-decoration: underline;
   }
   ```



## .btn-apps
`a.btn-apps`의 스타일을 정의합니다. 여기서 저는 그냥 `.btn-apps`를 사용하지 않고, `a.btn-apps`를 사용하는데요. 그냥 클래스만 사용할 경우, 더 높은 우선순위의 다른 프로퍼티가 적용될 수 있습니다. 따라서 태그와 클래스를 같이 사용해서 우선순위를 한 단계 높일 수 있습니다.      

- `a.btn-apps`의 `display`속성은 `flex`입니다.
- 패딩은 `3px`입니다.
- 글씨 색상은 `#737373`입니다.

**Instructions**
1. `a.btn-apps`의 스타일 적용하기.
   ```css
   a.btn-apps {
     display: flex;
     padding: 3px;
     color: #737373;
   }
   ```



## .btn-sign-in
우측 상단에 Sign in 버튼의 스타일을 정의합니다.      

- `a.btn-sign-in`의 패딩은 상/하 `8px`, 좌/우 `13px`입니다.
- 모서리의 둥글기는 `2px`입니다.
- 글씨 두께는 `bold`입니다.
- 행간은 `14px`입니다.
- 글씨 색상은 `white`입니다.
- 배경 색상은 `#4387fd`입니다.

**Instructions**
1. `a.btn-sign-in`의 스타일 적용하기.
   ```css
   a.btn-sign-in {
     padding: 8px 13px;
     border-radius: 2px;
     font-weight: bold;
     line-height: 14px;
     color: white;
     background-color: #4387fd;
   }
   ```


## .btn-sign-in:active
어떤 요소에 마우스를 올리고 있는 상태를 `:hover`라고 하죠. 마우스를 클릭한 상태는 무엇일까요? Sign in 버튼의 `:active`상태에 대한 스타일을 적용합니다.      
- `a.btn-sign-in:active`의 배경 색상은 `#3c7ae4`입니다.
- 그림자의 내부/x축/y축/퍼짐(blur)/크기/색상은 `inset 0 2px 0 rgba(0,0,0,.15)`입니다.

**Instructions**
1. `a.btn-sign-in:active`의 스타일 적용하기.
   ```css
    a.btn-sign-in:active {
      background-color: #3c7ae4;
      box-shadow: inset 0 2px 0 rgba(0,0,0,.15);
    }
   ```



## .nav-right
Sign in 버튼까지 스타일리을 했다면 버튼들이 위-아래로 배치 되어있을 겁니다. `.nav-right`에 `flex`를 이용하여 버튼들을 가로로 정렬해 봅시다. 
- `.nav-right`의 `display`속성은 `flex`입니다.
- `flex`가 적용된 내부 요소들의 y축으로 중앙 정렬합니다.

**Instructions**
1. `.nav-right`의 스타일 적용하기.
   ```css
   .nav-right {
     display: flex;
     align-items: center;
   }
   ```



**NEXT STEP** 버튼을 클릭하세요. 