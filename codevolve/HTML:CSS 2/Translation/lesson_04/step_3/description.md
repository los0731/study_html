# CSS
### <body>
To create a style, where the receipt seems to float on the background, let's go for a more grey background, rather than white. For the background color we use `Blue Grey 50` from [Google colors][999]. 
* The background color is `#ECEFF1`.

**Instructions**
1. Apply style to `body`.
    ```css
    body {
      background-color: #ECEFF1;
    }
    ```



### .container
The container sets the receipt in the middle of the screen, at a certain, predetermined width. 
* `.container`의 마진은 상/하 `80px`, 좌/우 `auto`입니다.
* The maximum width is `400px`.

**Instructions**
1. Apply style to `.container`.
    ```css
    .container {
      margin: 80px auto;
      max-width: 400px;
    }
    ```



### .table-receipt

let's define the style of the receipt inside the container. 
* `.table-receipt`의 경계선들이 겹쳐서 한줄로 표시되도록 합니다. 
* The width is `100%`.
* Background color is `white`.
* 그림자의 x축/y축/퍼짐(blur)/크기/색상은 `40px 40px 80px -8px #B0BEC5`입니다.

**Instructions**
1. Apply style to `.table-receipt`
    ```css
    .table-receipt {
    	border-collapse: collapse;
    	width: 100%;
    	background-color: white;
    	box-shadow: 40px 40px 80px -8px #B0BEC5;
    }
    ```



### <th> 
let's define the style of `th`, the title part of the receipt. In this lesson when we input a selector, we will call it `.table-receipt th`. 
* `.table-receipt th ` 의 패딩은 `24px`입니다.
* The width is `100%`.
* The font color is `white`.
* Background color is `#2196F3`. 이 색상은 [Google colors][999]의 Blue 500과 같습니다.

**Instructions**
1. Apply style to `.table-receipt th`.

    ```css
    .table-receipt th {
    	padding: 24px;
    	width: 100%;
    	color: white;
    	font-size: 24px;
    	background-color: #2196F3;
    }
    ```


Click the **NEXT STEP** button.

 


## TIPS! 
* Reasons for omitting the CSS selector. 
    > If, like in the previous case, you enter the selector very precisely, you can write as follows.   
    > ```css
    > table.table-receipt thead tr th {...}
    > ```
    > However, if you think that using classes for the selected range is appropriate, you can omit certain code, making your coding shorter and more efficient. 
    > ```css
    > .table-receipt th {...}
    > ```
    > A good argument for writing short and concise code is that it helps understand it quicker. Especially when other people have to look through it.
* What's `border-collapse`?

    > [border-collapse][2] is a CSS property, which sets overlapping properties for table cell borders. The values can be set as collapsed or seperate. 
    >
    > For `collapse`: the table cells' borders are integrated. That is, they overlap and look like one line. 
    >
    > For `separate`: by default, the table cells' borders are separate and are visible as two lines. 

[1]: https://www.w3schools.com/cssref/css_selectors.asp
[2]: https://www.w3schools.com/CSSref/tryit.asp?filename=trycss_border-collapse
[999]: https://material.io/design/color/#color-usage-palettes