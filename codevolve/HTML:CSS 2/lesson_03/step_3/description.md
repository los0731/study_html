# CSS
### body 
온라인 명함을 더 잘 보여주기 위해 배경 색상을 선택합니다. 이번에는 [Google colors][1]에서 Blue Grey 50을 선택했습니다.
* `body`의 패딩은 `8px`입니다. 
* `body`의 폰트는 `Arial, Helvetica, sans-serif`입니다.* 
* `body`의 배경 색상은 `#ECEFF1`입니다.

**Instructions**
1. `body`의 스타일 적용하기. 
    ```css
    body {
      margin: 0;
      padding: 16px;
      font-family: Arial, Helvetica, sans-serif;
      background-color: #ECEFF1;
    }
    ```



### 명함
`business-card`는 화면의 가운데 위치해야 하고, 특정 넓이를 가지며, 모서리가 둥글어야합니다. 이 외에도 글자 정렬, 배경 컬러, 그림자를 스타일링 합니다. 여기서 배경 컬러가 [Google Colors][1]에서 Blue Grey 50이기 때문에, 그림자의 색상은 Blue Grey 200으로 하겠습니다. 
* 배경 색상은 `white`입니다.
* 마진은 위/아래 `40px`, 좌/우 `auto`입니다.
* 패딩은 상-하-좌-우 모두 `40px`입니다.
* border-radius은 `8px`입니다.
* 넓이는 `240px`입니다. 
* 글자 정렬은 `center`입니다.
* 그림자는 x축 `0`, y축 `16px`, 퍼짐(blur) `32px`, 크기 `-16px`, 컬러 `#B0BEC5;`입니다.

**Instructions**
1. `business-card`의 스타일 적용하기.
    ```css
    .business-card {
      background-color: white;
      margin: 40px auto;
      padding: 40px;
      border-radius: 8px;
      width: 240px;
      text-align: center;
      box-shadow: 0 16px 32px -16px #B0BEC5;
    }
    ```



### 이미지
이미지의 크기가 카드보다 크기 때문에 넓이를 주변에 맞게 변경해줘야합니다. 
* `.image`의 넓이가 `100%`입니다.

**Instructions**
1. `.image`의 스타일 적용하기.
    ```css
    .image {
      width: 100%;
    }
    ```
    
    
    
모두 완료했다면 **NEXT STEP** 버튼을 클릭하세요.



# TIPS! 
* `<body>`에 서체를 지정하면 그 하위의 모든 태그에 적용됩니다.
    > 어떤 프로퍼티들은 지정한 선택자에만 적용됩니다. 하지만 어떤 프로퍼티들은 지정한 선택자와 그 하위 모든 선택자에 적용되기도 합니다. `font-family`는 하위 선택자에 모두 적용되는 프로퍼티입니다. 따라서 이 페이지에서 사용하는 모든 글씨에 `Arial, Helvetica, sans-serif`를 적용하고 싶다면 모든 선택자에 반복적으로 `font-family`를 적용할 필요없이 `<body>`에만 적용하면 됩니다.     
* `font-family: Arial, Helvetica, sans-serif;`의 서체들이 여러개인 이유가 뭐죠?
    > 왼쪽에서부터 Arial을 적용하고, 만약 사용자의 컴퓨터에 해당 폰트가 없을 경우, 그 다음인 Helvetica를 적용하라는 의미 입니다. 또 만약 Helvetica가 없을 경우, san-serif가 적용됩니다.

[1]: https://material.io/design/color/#color-usage-palettes

