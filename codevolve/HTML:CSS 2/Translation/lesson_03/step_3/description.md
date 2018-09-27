# CSS
### <body> 
To better showcase the online business card, we will choose a background color. In [Google colors][1] choose `Blue Grey 50`. 
* `body`의 마진은 `0`으로 적용되어 있습니다.
* Padding is `8px`.
* The font is `Arial, Helvetica, sans-serif`.
* Background color is `#ECEFF1`.

**Instructions**
1. Apply style to `body`.
    ```css
    body {
      margin: 0;
      padding: 16px;
      font-family: Arial, Helvetica, sans-serif;
      background-color: #ECEFF1;
    }
    ```



### .business-card
`business-card` should be placed in the middle of the screen, and it should have a specific width and rounded corners. We will also style the font alignment, background color, shadow. Since the background color here is [Google Colors][1]'s `Blue Grey 50`, we will make the shadow color `Blue Grey 200`. 

* Background color is `white`.
* 마진은 상/하 `40px`, 좌/우 `auto`입니다.
* 패딩은 상/우/하/좌 모두 `40px`입니다.
* 모서리의 둥글기는 `8px`입니다.
* The width is `240px`.
* 글은 가운데 정렬 입니다.
* 그림자의 x축/y축/퍼짐(blur)/크기/색상은 `0 16px 32px -16px #B0BEC5;`입니다.

**Instructions**
1. Apply style to `business-card`.
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



### .image
The size of the image must be reduced to match the size of the card.
* The width of `.image` is `100%`.

**Instructions**
1. Apply style to `.image`.
    ```css
    .image {
      width: 100%;
    }
    ```

Click the **NEXT STEP** button.



## TIPS! 
* If you specify a font in the `<body>`, it will apply to all the tags after it. 

    > Some properties apply to sections they are defined in. However, some properties apply not only to the sections they are specified in, but to all the sections following them. `font-family` is such a property, that applies to sections herethenon. Therefore, if you want to use the fonts `Arial, Helvetica, sans-serif` on all the text on this page, you don't have to define `font-family` for each section, but just for `<body>`.  
* Why are there multiple different fonts specified in `font-family: Arial, Helvetica, sans-serif;`? 

    > Starting from the left, `Arial` font will be applied to the text. If the user doesn't have that font installed on their computer, it means that `Helvetica` will be applied. And if they don't have Helvetica, the font of the text will be set to `san-serif`. 

[1]: https://material.io/design/color/#color-usage-palettes

