# CSS
### <body>

Medium's policy page uses a lot of styles for the body tag, like `font-size`, `font-size`, `color`, `line-height`. What they have is common is that the properties can be also applied to the tags that follow the body. that's why we start by setting the basic attributes for the entire site, like font, font size, font color, in the top-level the body tag. let's define the body tag's style. 

* The margin of `body` is `0`.
* Padding is `0`.
* The font is `'Source Serif Pro', serif`.
* The font size is `19px`.
* line height is `1.58`.
* The font color is `#333`.
* Apply Anti-Aliasing.


**Instructions**
1. Apply style to `body`.
    ```css
    body {
    	margin: 0;
    	padding: 0;
    	font-family: 'Source Serif Pro', serif;
    	font-size: 19px;
    	line-height: 1.58;
    	color: #333;
    	-webkit-font-smoothing: antialiased;
    }
    ```



### .navbar 

let's set the style for the navigation bar, which includes the logo text. 

* The padding below .navbar` is `8px`.
* The letters are centered.
* The font is `'Playfair Display', serif`.
* The font size is `39px`.
* The font-weight is `bold`.
* The line height is `56px`.


**Instructions**
1. Apply style to `.navbar`.
    ```css
    .navbar {
        padding-bottom: 8px;
        text-align: center;
        font-family: 'Playfair Display', serif;
        font-size: 39px;
        font-weight: bold;
        line-height: 56px;
    }
    ```



### .hero 

let's define the hero image style, to set the theme for this page. We found an image for the background at [PEXELS][https://www.pexels.com/] and copied it's address. 

* The width of `.hero` is `100%`.
* The height is `30vw`.
* Minimum height is `200px`.
* The maximum height is `534px`.
* The background image's url/repetition/x-axis range/y-axis range is each set to `url("https://images.pexels.com/photos/840996/pexels-photo-840996.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260") no-repeat center center`.
* Background image overwrites all areas.


**Instructions**
1. Apply style to `.hero`
    ```css
    .hero {
        width: 100%;
        min-height: 200px;
        height: 30vw;
        max-height: 534px;
        background: url('https://images.pexels.com/photos/840996/pexels-photo-840996.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260') no-repeat center center;
        background-size: cover;
    }
    ```



Click the **NEXT STEP** button.



## TIPS!

- What meaning does `background-size: cover;` have?

  > You can set the width and height of the space where you'll put the background image and you can import the image itself by just copying and pasting the url. However, because the image's size proportions are not being considered here, in order to see the whole image, the `background-size` property should be set as `cover`.




