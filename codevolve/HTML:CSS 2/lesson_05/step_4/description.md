# CSS
### <body>
페이지의 배경이미지를 추가합니다. `body` 의 전체 영역에 이미지를 채워 넣기 위해서는 배경의 높이를 브라우저 전체 높이로 지정해야 합니다. 따라서  `body` 의 최소 높이에서 `body` 의 상/하 패딩 값을 빼서 전체 높이를 맞출 수 있습니다.
* `body`의 패딩은 상/하 `80px`, 좌/우 `16px`입니다.
* 최소 높이는 전체 `Viewport height`에서 `160px`만큼 뺀 값입니다. 
* 배경 이미지의 url/반복/x축 정렬/y축 정렬은 각각 `url("https://image.freepik.com/free-vector/matisse-inspired-shapes-seamless-pattern_1235-418.jpg") no-repeat center center`입니다.
* 배경 이미지가 모든 영역을 덮어 씁니다.


**Instructions**
1. `body`의 스타일 적용하기. 
    ```css
    body {
      margin: 0;
      padding: 80px 16px;
      min-height: calc(100vh - 160px);
      background: url("https://images.unsplash.com/photo-1485498128961-422168ba5f87?ixlib=rb-0.3.5&s=bb0e76f1949725c83131d875abaa0f1a&auto=format&fit=crop&w=2602&q=80") no-repeat center center;
      background-size: cover;
    }
    ```



### .menu-wrap
`.menu-wrap`는 메뉴판을 둘러싸는 공간입니다.

* `menu-wrap`의 마진은 상/하 `0`, 좌/우 `auto`입니다.
* 패딩은 `40px`입니다.
* 모서리의 둥글기는 `8px`입니다.
* 최대 넓이는 `400px`입니다.
* 배겅 색상은 `white`입니다.
* 그림자의 x축/y축/퍼짐(blur)/크기/색상은 `40px 40px 80px -40px rgba(50,50,80,.4)`입니다. 



**Instructions**
1. `.menu-wrap`의 스타일 적용하기.
    ```css
    .menu-wrap {
      margin: 0 auto;
      padding: 40px;
      border-radius: 8px;
      max-width: 400px;
      background-color: white;
      box-shadow: 40px 40px 80px -40px rgba(50,50,80,.4);
    }
    ```



### <header>

`header`는 카페의 이름과 로고가 들어갑니다. 

* `header`의 서체는 `'Satisfy', cursive` 입니다.
* 글은 가운데 정렬 입니다.

**Instructions**
1. `header`의 스타일 적용하기.
    ```css
    header {
      font-family: 'Satisfy', cursive;
      text-align: center;
    }
    ```
    



### <h4> 

`header`안에 포함된 `h4`는 카페의 이름입니다. 

* `header h4`의 마진은 `0` 입니다.
* 글씨의 사이즈는 `40px`입니다.
* 글씨의 색상은 `#FF5722`입니다.

**Instructions**
1. `header`의 스타일 적용하기.
    ```css
    header h4 {
      margin: 0;
      font-size: 40px;
      color: #FF5722;
    }
    ```
    



### .table-menu

`.table-menu`는 커피의 종류와 가격을 보여주는 메뉴판의 내용 공간입니다.

* `.table-menu`의 마진은 상/우/하/좌 `40px 0 0 0`입니다.
* 넓이는 `100%`입니다.
* 서체는 `'Questrial', sans-serif`입니다.
* 글씨 크기는 `24px`입니다.
* 글씨 색상은 `#455A64`입니다.
* 행간은 `40px`입니다.


**Instructions**
1. `.table-menu`의 스타일 적용하기.
    ```css
    .table-menu {
      margin: 40px 0 0 0;
      width: 100%;
      font-family: 'Questrial', sans-serif;
      font-size: 24px;
      color: #455A64;
      line-height: 40px;
    }
    ```



모두 완료했다면 **NEXT STEP** 버튼을 클릭하세요.

