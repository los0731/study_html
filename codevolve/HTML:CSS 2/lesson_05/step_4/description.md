# 스타일
## body
메뉴판을 돋보이게 하기 위해 배경에 화려한 패턴 이미지를 넣습니다.
* `body`의 배경 이미지는 `https://image.freepik.com/free-vector/matisse-inspired-shapes-seamless-pattern_1235-418.jpg`입니다.
 

**Instructions**
1. `body`의 스타일 적용하기. 
    ```css
    body {
        background: url("https://image.freepik.com/free-vector/matisse-inspired-shapes-seamless-pattern_1235-418.jpg")
    }
    ```

## menu-wrap
`menu-wrap` 클래스는 메뉴판을 둘러싸는 공간입니다.

* `menu-wrap`의 배경 컬러는 `white`입니다.
* `menu-wrap`의 최대 넓이는 `600px`입니다.
* `menu-wrap`의 margin은 상-하 `80px` 좌-우 `40px`입니다. 
* `menu-wrap`의 padding은 `40px`입니다.
* `menu-wrap`의 border-radius는 `24px`입니다.


**Instructions**
1. `menu-wrap`클래스의 스타일 적용하기.
    ```css
    .menu-wrap {
      background-color: white;
      max-width: 600px; 
      margin: 80px auto; 
      padding: 40px;
      border-radius: 24px; 
    }
    ```

## menu
`menu` 클래스는 실제 메뉴판의 내용을 채우는 공간입니다.

* `menu`의 경계선 두께는 `8px`, 선의 모양은 `solid`, 색깔은 `#FCE4EC` 입니다.
* `menu`의 padding는 `24px`입니다.


**Instructions**
1. `menu`클래스의 스타일 적용하기.
    ```css
    .menu {
      border: 8px solid #FCE4EC;
      padding: 24px;
    }
    ```

## header
`header` 클래스는 가게의 이름과 로고를 넣을 공간입니다. 

* `header`의 텍스트 정렬은 `center`입니다.
* `header`클래스 안에서 사용되는 `h4`의 텍스트 굵기는 `100`입니다.
* `header`클래스 안에서 사용되는 `h4`의 텍스트 사이즈는 `40px`입니다.
* `header`클래스 안에서 사용되는 `h4`의 텍스트 컬러는 `#E91E63`입니다.

**Instructions**
1. `header`의 스타일 적용하기.
    ```css
    .header {
      text-align: center;
    }
    header h4 {
        font-weight: 100;
        font-size: 40px; 
        color: #E91E63; 
    }
    ```
    
## table-menu
`table-menu` 클래스는 커피의 종류와 가격을 보여주는 메뉴판의 내용 공간입니다.

* `table-menu`의 넓이는 `100%`입니다.
* `table-menu`의 margin은 상 `40px`, 하-좌-우 `0`입니다.
* `table-menu`의 table-layout은 `fixed`입니다.


**Instructions**
1. `table-menu`의 스타일 적용하기.
    ```css
    .table-menu {
      width: 100%;
      margin: 40px 0 0 0;
      table-layout: fixed;
    }
    ```

## table-menu의 세부 태그
`table-menu` 클래스의 `th`는 메뉴의 첫 번째 행을 나타냅니다.
`table-menu` 클래스의 `td`는 메뉴의 두 번째~네 번째 행을 나타냅니다.
`table-menu` 클래스의 `t-title`은 메뉴 종류의 이름을 나타냅니다.
`table-menu` 클래스의 `t-size`은 메뉴 종류의 사이즈 및 가격을 나타냅니다.

* `table-menu`클래스 안에서 사용되는 `th`, `td`의 padding은 상-하 `8px`, 좌-우 `0`입니다.
* `table-menu`클래스 안에서 사용되는 `th`, `td`의 폰트 크기는 `14px` 입니다.
* `table-menu`클래스 안에서 사용되는 `th`의 폰트 컬러는 `#E91E63` 입니다.
* `table-menu`클래스 안에서 사용되는 `th`의 `border-bottom`의 선 두께는 `2px`, 모양은 `solid`, 컬러는 `#FCE4EC` 입니다.
* `table-menu`클래스 안에서 사용되는 `td`의 폰트 컬러는 `#455A64` 입니다.
* `table-menu`클래스 안에서 사용되는 `t-title`의 텍스트 정렬은 `left` 입니다.
* `table-menu`클래스 안에서 사용되는 `t-size`의 넓이는 `64px` 입니다.
* `table-menu`클래스 안에서 사용되는 `t-size`의 텍스트 정렬은 `center` 입니다.


**Instructions**
1. `table-menu`의 스타일 적용하기.
    ```css
    .table-menu th, 
    .table-menu td {
    padding: 8px 0;
    font-size: 14px; 
    }
    .table-menu th {
    color: #E91E63;
    border-bottom: 2px solid #FCE4EC;
    }
    .table-menu td {
    color: #455A64;
    }
    .t-title {
    text-align: left;
    }
    .t-size {
    width: 64px;
    text-align: center; 
    }
    ```

모두 완료했다면 **NEXT STEP** 버튼을 클릭하세요.

