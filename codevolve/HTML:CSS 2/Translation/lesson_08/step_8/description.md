## .footer
Finally, we will define the style of the footer area. The footer must be pinned to the bottom of the screen.
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
The two `<div>`within the footer must be positioned left/right of each other. This time in `.footer-right` let's use `float` function to capture the layout
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



## .footer a
let's style all the `a` tags in the footer.
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



## footer a:hover
Last but not least, when the `a` tags in the footer are in the hover mode, they should get underlined.    
- `.footer a:hover`의 텍스트에 밑줄이 생깁니다.

**Instructions**
1. Apply style to `.footer a:hover`.
   ```css
   .footer a:hover {
     text-decoration: underline;
   }
   ```



Click the **NEXT STEP** button.