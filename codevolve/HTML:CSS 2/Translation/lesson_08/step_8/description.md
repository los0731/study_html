## .footer
마지막으로 푸터 영역의 스타일을 정의합니다. 푸터는 화면의 맨 하단에 고정되어 있어야 합니다. 
* `.footer`의 `position`은 `absolute`입니다.
* 아래에서 `0`만큼 떨어져 있습니다.
* 위 경계선은 `1px`의 직선이고 색상은 `#e4e4e4`입니다.
* 넓이는 브라우저 전체 입니다.
* Background color is `#f2f2f2`.

**Instructions**
1. Apply style to `.footer`.
    ```css
    .footer {
      position: absolute;
      bottom: 0;
      border-top: 1px solid #e4e4e4;
      width: 100vw;
      background-color: #f2f2f2;
    }
    ```



## .footer-right
푸터 안에 있는 두개의 `<div>`들은 서로 좌/우에 배치 되어야 합니다. 이번에는 `.footer-right`에 `float`속성을 이용해서 레이아웃을 잡아봅니다.        
- `.footer-right`의 `float`속성은 `right`입니다.
- 오른쪽 마진은 `25px`입니다.

**Instructions**
1. Apply style to `.form-search-wrap`.
   ```css
   .footer-right {
     float: right;
     margin-right: 25px;
   }
   ```



## <a> in .footer
이제, 푸터 안에 있는 모든 a태그들의 스타일을 정의 합니다.
- `.footer a`의 왼쪽 마진은 `25px`입니다.
- The font size is `13px`.
- 행간은 `40px`입니다.
- The font color is `#666`. 

**Instructions**
1. Apply style to `.footer a`.
   ```css
   .footer a {
     margin-left: 25px;
     font-size: 13px;
     line-height: 40px;
     color: #666;
   }
   ```



## a:hover in footer
마지막으로, 푸터 안에 있는 a 태그들이 hover 상태일때는 밑줄이 생겨야 합니다.      
- `.footer a:hover`의 텍스트에 밑줄이 생깁니다.

**Instructions**
1. Apply style to `.footer a:hover`.
   ```css
   .footer a:hover {
     text-decoration: underline;
   }
   ```



Click the **NEXT STEP** button.