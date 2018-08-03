### 컨테이너
이 페이지의 내용들을 담고 있는 컨테이너의 스타일을 지정합니다. 컨테이너는 브라우저의 넓이가 아무리 넓어도 최대 넓이를 유지해야합니다. 그리고 화면의 가운데 위치해야합니다. 

* `container`의 마진은 위/아래 `0`, 좌/우 `auto`입니다.
* 패딩은 위/아래 `0`, 좌/우 `16px`입니다.
* 최대 넓이는 `630px`입니다.


**Instructions**
1. `.container`의 스타일 적용하기. 
    ```css
    .container {
      margin: 0 auto;
      padding: 0 16px;
      max-width: 630px;
    }
    ```



### 컨텐트

컨테이너 하위 태그인 컨텐트는 해드라인 그룹과 컨텐트 텍스트를 감싸고 있습니다.  

- `.content`의 아래 마진은 `70px`입니다.

**Instructions**

1. `.content`의 스타일 적용하기.

   ```css
   .content {
     margin-bottom: 70px;
   }
   ```



### 헤드라인 그룹

제목과 부제목을 감싸고 있는 헤드라인 그룹의 스타일을 지정해 봅시다. 바디 텍스트와 명확하게 구분하기 위해 마진을 이용해서 간격을 설정하고, 서체를 변경해야 합니다.

* `.headline-group`의 마진은 상/하/좌/우 `64px 0 24px 0`입니다.
* 서체는 `'Heebo', sans-serif`입니다.


**Instructions**
1. `.headline-group `의 스타일 적용하기.
    ```css
    .headline-group {
      padding: 64px 0 24px 0;
      font-family: 'Heebo', sans-serif;
    }
    ```




**NEXT STEP** 버튼을 클릭하세요.