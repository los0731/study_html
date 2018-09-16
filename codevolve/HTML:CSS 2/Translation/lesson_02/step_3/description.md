# CSS
### <body>
Set the color of the card to white and the background to purple.

* `body`의 마진은 `0`으로 적용되어 있습니다.
* 패딩은 상/우/하/좌 모두`16px`입니다.
* Background color is `#512DA8`.

**Instructions**
1. Apply style to `body`. 
    ```css
    body {
      margin: 0;
      padding: 16px;
      background-color: #512DA8;
    }
    ```



### .birthday-card
`.birthday-card`는 카드를 작성할 공간입니다.
* 마진은 상/하 `40px`, 좌/우 `auto`입니다.
* Padding is `16px`
* The maximum width is `400px`.
* Background color is `white`.
* 글자 정렬은 `center`입니다.
* 그림자의 x축/y축/퍼짐(blur)/크기/색상은 `0 24px 40px -8px #311B92`입니다.

**Instructions**
1. Apply style to `birthday-card`.
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



Click the **NEXT STEP** button.



## TIPS!
* 색상을 사용하는 기준은 무엇인가요?
    > 디자이너가 아니라면, [Google Colors][https://material.io/design/color/#color-usage-palettes]에서 500번 계열의 색상을 사용하시는걸 추천합니다. 500번 계열은 우리가 흔히 플랫한 컬러라고 할 수 있는 맑고 선명한 컬러들 입니다. 숫자가 낮아질 수록 밝아지고, 높아질 수록 어두워지죠.
    > 거기에 저는 보통 1가지 색상을 선택하고(이것을 테마 컬러 라고 부릅니다.) 나머지는 Blue grey 컬러로 통일 하는것을 선호합니다. 그 외에는 의미에 맞는 색상만 사용합니다.  
    > - 링크의 의미를 가지고 있는 것에는 Blue500
    > - 위험, 삭제, 제거, 에러 등 부정적인 의미에는 Red500
    > - 경고, 주의, 주목해야하는 요소에는 Orange 500
    > - 업로드 완료, 작성 완료, 성공, 정답등 매우 긍정적인 요소에는 Green500
* 그림자 컬러가 black이 아닌가요?

    > 흔히 그림자의 값을 줄 때 사용하는 색상이 Black입니다. 하지만 많은 디자이너들이 그림자에 Black을 사용하지 않습니다. 그림자는 배경 컬러와 밀접합니다. 따라서 그림자의 색상을 선택할 경우, 배경 컬러보다 조금 어두운 색상을 선택하길 추천합니다. 예를 들어 위의 google colors의 흰색 배경에는 Blue grey 50~300을, 배경 색이 Blue 500이라면 Blue 700~900을 그림자 컬러로 사용하면 자연스러운 그림자를 연출할 수 있습니다.  조금 전문적으로 접근하면 투명한 값을 사용하기도 합니다. 흰색 배경을 기준으로 값을 추천하자면 `rgba(50,50,80,.08)`정도로 약간 푸르스름한 회색을 투명하게 사용하면 배경색과 어우러져 자연스러운 연출이 가능합니다.
* 자세히 보니 값들의 수치가 8의 배수 아닌가요?
    > 맞습니다. 8의 배수로 레이아웃, 간격, 크기, 수치 등을 사용사는 목적은 다음과 같습니다.
      1. 예상하기 쉬워서, 곧 협업하기 쉽습니다. 디자이너만 아는 값들이 아닌 대충 예상이 가능한 값이되기때문에, 디자이너 없이도 개발자 혼자 수정하기 수월합니다. 
      2. 다양한 디바이스/디스플레이를 만족하는 효율적인 레이아웃을 구현할 수 있습니다. 
      3. 규칙적이고 일관적인 사용자 경험을 제공할 수 있습니다.
      (더 자세히 알아봅시다 - https://builttoadapt.io/intro-to-the-8-point-grid-system-d2573cde8632 )" 