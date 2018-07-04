# 스타일
## body 
카드의 색을 하얀색으로 만들 것이기 때문에, 카드가 잘 보이도록 배경은 보라색으로 설정합니다. 
* `body`의 배경 컬러는 `#512DA8`입니다.
* `body`의 padding은 `16px`입니다. 

**Instructions**
1. `body`의 스타일 적용하기. 
    ```css
    body {
      margin: 0;
      padding: 16px;
      background-color: #512DA8;
    }
    ```



## 생일 카드
`birthday-card`는 화면의 가운데 위치해야합니다. 종이 카드 처럼 보이게 하기 위해서 하얀 배경과 적절한 크기 제한이 필요합니다. 
* `birthday-card`의 margin은 위/아래 `40px`, 좌/우 `auto`입니다.
* `birthday-card`의 padding은 `16px`입니다.
* `birthday-card`의 최대 넓이는 `400px`입니다. 
* `birthday-card`의 배경 컬러는 `white`입니다.
* `birthday-card`의 글자 정렬은 `center`입니다.
* `birthday-card`의 그림자는 x축 `0`, y축 `24px`, 퍼짐(blur) `40px`, 크기 `-8px`, 컬러 `#311B92` 입니다.

**Instructions**
1. `birthday-card`의 스타일 적용하기.
    ```css
    .birthday-card {
      margin: 40px auto;
      padding: 16px;
      max-width: 400px;
      background-color: white;
      text-align: center;
      box-shadow: 0 24px 40px -8px #311B92;
    }
    ```



## 이미지
이미지의 크기가 카드보다 크기 때문에 넓이를 주변에 맞게 변경해줘야합니다. 
* `img`의 넓이가 `100%`입니다.

**Instructions**
1. `img`의 스타일 적용하기.
    ```css
    .birthday-card img {
      width: 100%;
    }
    ```
    
    
    
## 출처
출처는 작은 글씨로 카드 아래에 약하게 표시되었으면 좋겠습니다. 따라서 아래와 같이 스타일링합니다. 

* `sources-link`는 가운데 정렬입니다.
* `sources-link` 하위 `a`태그의 컬러는 `#311B92`입니다. 
* `sources-link` 하위 `a`태그의 밑줄을 제거합니다. 

**Instructions**
1. `.sources-link`의 스타일 적용하기.
    ```css
    .sources-link {
      text-align: center;
    }
    ```
1. `.sources-link` 하위 `a`의 스타일 적용하기.
    ```css
    .sources-link a {
      color: #311B92;
      text-decoration: none;
    }
    ```



모두 완료했다면 **NEXT STEP** 버튼을 클릭하세요.



## TIPS! 
* 컬러를 사용하는 기준은 무엇인가요? 
    > 본인이 디자이너가 아니라면, [Google Colors][1]에서 500번 계열의 컬러를 사용하시는걸 추천합니다. 이번 예시에서 사용한 배경컬러도 Deep purple 900 컬러를 사용하였습니다.   
* 그림자 컬러가 black이 아닌가요?
    > 많은 디자이너들이 그림자에 black을 사용하지 않습니다. 그림자는 배경 컬러와 밀접합니다. 따라서 그림자의 색상을 선택할 경우, 배경 컬러보다 조금 어두운 컬러를 선택하길 추천합니다. 예를덜어 위의 google colors의 `blue 500`의 배경는 `blue 700`을 그림자 컬러로 사용하면 자연스러운 그림자를 연출 할 수 있습니다. 
* 자세히 보니 값들의 수치가 8의 배수 아닌가요? 
    > 맞습니다. [눈썰미가 좋으시군요!?][2]

[1]: https://material.io/design/color/#color-usage-palettes
[2]: https://builttoadapt.io/intro-to-the-8-point-grid-system-d2573cde8632

