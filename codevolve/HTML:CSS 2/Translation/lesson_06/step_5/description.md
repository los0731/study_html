### .container
We set the style of the container which carries the page's contents. No matter how wide it gets, the container should maintain the width of the browser. Also, it has to placed in the middle of the screen. 

* `container`의 마진은 상/하 `0`, 좌/우 `auto`입니다.
* 패딩은 상/하 `0`, 좌/우 `16px`입니다.
* The maximum width is `630px`.


**Instructions**
1. Apply style to `.container`.
    ```css
    .container {
      margin: 0 auto;
      padding: 0 16px;
      max-width: 630px;
    }
    ```



### .content 

The subtag of the container, the content, covers the headline group and body text. 

- `.content`의 아래 마진은 `70px`입니다.

**Instructions**

1. Apply style to `.content`.

   ```css
   .content {
     margin-bottom: 70px;
   }
   ```



### .headline-group

let's define the style of the headline group which covers the title and subheadings. To clearly distinguish it from the body text, we need to use the margin, to set the spacing, and change the font. 

* `.headline-group`의 마진은 상/우/하/좌 `64px 0 24px 0`입니다.
* The font is `'Heebo', sans-serif`.


**Instructions**
1. Apply style to `.headline-group`.
    ```css
    .headline-group {
      padding: 64px 0 24px 0;
      font-family: 'Heebo', sans-serif;
    }
    ```




Click the **NEXT STEP** button.