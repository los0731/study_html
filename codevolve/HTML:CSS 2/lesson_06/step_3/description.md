# 스타일
## body
페이스북 디자인 페이지는 배경의 아주 약한 grey를 사용합니다. 또 `body`태그에서 전체 서체를 별도로 지정했습니다.  
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
* Transition은 `.24s`입니다.


**Instructions**
1. `menu-wrap`클래스의 스타일 적용하기.
    ```css
    .card {
    	margin: 80px auto;
    	max-width: 350px;
    	box-shadow: 0 20px 20px rgba(0, 0, 0,.08);
    	transition: .24s;
    }
    ```



## 카드에 마우스를 올렸을 때.
Hover는 해당 요소에 마우스를 올린 상태를 말합니다. 마우스를 사용하는 데스크탑에서 클릭이 가능한 상태라는걸 설명하는 가장 좋은 UI가 hover입니다. 카드의 hover 스타일을 지정해봅시다.
위에 사용한 `transition: .24s;`에 의해서, 일반 상태에서 hover 상태로, hover 상태에서 일반 상태로 더 부드럽게 변화하게 됩니다.

* `.card:hover`의 그림자는 x축 `0`, y축 `40px`, 퍼짐(blur) `40px`, 컬러 `rgba(0, 0, 0,.16)` 입니다.
* 위로 20px만큼 이동합니다.


**Instructions**
1. `menu`클래스의 스타일 적용하기.
    ```css
    .card:hover {
    	box-shadow: 0 40px 40px rgba(0, 0, 0,.16);
    	transform: translateY(-20px);
    }
    ```



## a 태그
우리는 `<div class="card">` 

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

