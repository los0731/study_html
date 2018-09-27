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

* The margin of `.card` is `80px` top/down, `auto` left/right.
* The maximum width is `350px`.
* The shadow's x-axis/y-axis/blur/size/color is `0 20px 20px 0 rgba(0, 0, 0,.08)`.
* The rounded edges are `3px`.
* The `transition` attribute is `.24s`.


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

* `.card:hover`'s shadow's x-axis/y-axis/blur/size/color is ``0 40px 40px 0 rgba(0, 0, 0,.16)`.
* Use `transform` to move `20px` upwards.


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

* There are no text decorations in `a`'s text.
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

