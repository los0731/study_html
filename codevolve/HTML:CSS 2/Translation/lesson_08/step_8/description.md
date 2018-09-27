## .footer
Finally, we will define the style of the footer area. The footer must be pinned to the bottom of the screen.
* `.footer`'s `position` is `absolute`.
* It's `0` from below.
* The top border is `1px` solid line and the color is `#e4e4e4`.
* The width is the entire browser.
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
- `.footer-right`'s `float` attribute is `right`.
- The right margin is `25px`.

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
- The left margin of `.footer a` is `25px`.
- The font size is `13px`.
- The line height is `40px`.
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
- `.footer a:hover`'s text is underlined.

**Instructions**
1. Apply style to `.footer a:hover`.
   ```css
   .footer a:hover {
     text-decoration: underline;
   }
   ```



Click the **NEXT STEP** button.