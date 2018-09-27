# CSS
### <body>
We now add the page's background image. In order to fill the entire `body` area, the background has to be set as the height of the entire browser. And so, we can set the entire height as the difference between the `body`'s minimum height and `body`'s up/down padding value. 
* The padding of `body` is `80px` top/down, `16px left/right.
* The minimum height value is the difference between the total `Viewport height` and `160px`.
* The background image's url/repetition/x-axis range/y-axis range is each set to `url("https://image.freepik.com/free-vector/matisse-inspired-shapes-seamless-pattern_1235-418.jpg") no-repeat center center`.
* Background image overwrites all areas.


**Instructions**
1. Apply style to `body`.
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
`.menu-wrap` is the space surrounding the menu.

* The margin of `menu-wrap` is `0` top/down, `auto` left/right.
* Padding is `40px`.
* The rounded edges are `8px`.
* The maximum width is `400px`.
* Background color is `white`
* The shadow's x-axis/y-axis/blur/size/color is  `40px 40px 80px -40px rgba(50,50,80,.4)`.



**Instructions**
1. Apply style to `.menu-wrap`.
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
`header` contains the name and logo of the cafe.

* The font of `header` is `'Satisfy', cursive`.
* The letters are centered.

**Instructions**
1. Apply style to `header`.
    ```css
    header {
      font-family: 'Satisfy', cursive;
      text-align: center;
    }
    ```
    



### <h4> 

`h4` included in the `header` is the name of the cafe.

* The margin of `header h4` is `0`.
* The font size is `40px`.
* The font color is `#FF5722`.

**Instructions**
1. Apply style to `header`.
    ```css
    header h4 {
      margin: 0;
      font-size: 40px;
      color: #FF5722;
    }
    ```
    



### .table-menu

`.table-menu` is the area where the coffee types and the prices are to be displayed. 

* The margin of `.table-menu` is `40px 0 0 0` for top/right/down/left.
* The width is `100%`.
* The font is `'Questrial', sans-serif`.
* The font size is `24px`.
* The font color is `#455A64`.
* The line height is `40px`.


**Instructions**
1. Apply style to `.table-menu`.
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



Click the **NEXT STEP** button.

