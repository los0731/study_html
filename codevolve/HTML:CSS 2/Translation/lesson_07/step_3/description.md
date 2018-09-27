# CSS
### <body>
Facebook design page uses a very light grey background. Also there's a separate font assigned to the whole area. 
* Background color of `body` is `#FCFCFC`.
* The font is `'San Francisco', -apple-system, BlinkMacSystemFont, '.SFNSText-Regular', Roboto, 'Helvetica Neue', Helvetica, Arial, sans-serif`.(This is actually a font for Facebook design.)


**Instructions**
1. Apply style to `body`
    ```css
    body {
    	background-color: #FCFCFC;
    	font-family: 'San Francisco', -apple-system, BlinkMacSystemFont, '.SFNSText-Regular', Roboto, 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    ```



### .card
let's define the style of the card. 

* `.card`의 마진은 상/하 `80px`좌/우 `auto`입니다.
* The maximum width is `350px`.
* 그림자의 x축/y축/퍼짐(blur)/크기/색상은 `0 20px 20px 0 rgba(0, 0, 0,.08)`입니다. 
* 모서리의 둥글기는 `3px`입니다.
* `transition` 속성은 `.24s`입니다.


**Instructions**
1. Apply style to `.card`.
    ```css
    .card {
    	margin: 80px auto;
    	max-width: 350px;
    	box-shadow: 0 20px 20px rgba(0, 0, 0,.08);
        border-radius: 3px;
    	transition: .24s;
    }
    ```



### .card:hover
`:hover` refers to the hovering the mouse over an element. it's the best UI practice to explain to desktop users that they can click their mouse on an element. let's define the hover style of the card. Thanks to using the `transition: .24s;` at the top, the transition from normal state to hover and back to normal is much smoother. 

* `.card:hover`의 그림자는 x축/y축/퍼짐(blur)/크기/색상은 `0 40px 40px 0 rgba(0, 0, 0,.16)`입니다.
* `transform` 을 사용하여 위로 `20px` 움직입니다.


**Instructions**
1. Apply style to `.card:hover`.
    ```css
    .card:hover {
    	box-shadow: 0 40px 40px rgba(0, 0, 0,.16);
    	transform: translateY(-20px);
    }
    ```



### <a>
In `<a>` the text is by default blue and underlined. that's why we have to define the style separately and remove all the decorative elements. 

* `a`의 글씨의 장식이 없습니다.
* The font color is `#1D2129`.

**Instructions**
1. Apply style to `a`.
    ```css
    a {
    	text-decoration: none;
    	color: #1D2129;
    }
    ```





Click the **NEXT STEP** button.





## TIPS!

- Transition attribute 

  > **CSS transitions** offer a way to adjust the animation speed when CSS attributes are changing. Instead of making immediate attribute changes, we can make the attribute change happen smoothly over a period of time. For example, if you change the color of an element from white to black, the change will occur instantaneously. If you use CSS transitions, all the changes take place over period of time, which can be set accordingly. 
  >
  > 출처: [Mozilla CSS transitions][https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions]

