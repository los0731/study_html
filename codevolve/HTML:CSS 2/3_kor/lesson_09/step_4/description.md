# CSS
## a, p, select
이 페이지에서 공통적으로 사용하게되는 요소들은 클래스로 지정하기 전에 해당 태그 전체의 스타일을 지정할 수 있습니다. 버튼으로 사용하게될 태그(`<a> <p> <select>`)들의 스타일을 지정합니다.
* `a` 와 `p`와 `select`의 글씨 크기는 `15px`입니다.
* `transition` 속성은 `.2s .1s`입니다.


**Instructions**
1. `a, p, select`의 스타일 적용하기. 
    ```css
    a, p, select {
      font-size: 15px;
      transition: .2s .1s;
    }
    ```



## a

역시 모든 `a`에 공통적으로 밑줄을 제거하고 글씨 색상과 두깨를 조정합니다. 

- `a`의 글씨의 장식이 없습니다.
- 글씨 색상은 `1a73e8`입니다.
- 글씨 두깨는 `500`입니다.

**Instructions**

1. `a`의 스타일 적용하기.

   ```css
   a {
     text-decoration: none;
     color: #1a73e8;
     font-weight: 700;
   }
   ```



## .container

컨테이너에 `flex`속성을 적용하여 내부 요소인  `<div class="card-login-wrap">`   가 화면의 중앙에 배치되도록 합니다.

- `.container`의 `display`는 `flex`입니다.
- `flex`가 적용된 내부 요소들이 수직으로 중앙 정렬합니다.   
- `flex`가 적용된 내부 요소들이 좌/우 끝에 배치되도록 합니다.
- 최소 높이는 `100vh`입니다.

**Instructions**

1. `a`의 스타일 적용하기.

   ```css
   .container {
     display: flex;
     align-items: center;
     justify-content: center;
     min-height: 100vh;
   }
   ```



## .card-login-wrap

`<div class="card-login-wrap">` 는 입력폼을 감싸고 있는 태그입니다. 패딩과 최대 넓이를 적용하여 적절한 영역을 만듭니다.

- `.card-login-wrap`의 패딩은 `24px`입니다.
- 최대 넓이는 `450px`입니다.
- 글씨 색상은 `#212121`입니다.

**Instructions**

1. `.card-login-wrap`의 스타일 적용하기.

   ```css
   .card-login-wrap {
     padding: 24px;
     max-width: 450px;
     color: #212121;
   }
   ```





**NEXT STEP** 버튼을 클릭하세요.

