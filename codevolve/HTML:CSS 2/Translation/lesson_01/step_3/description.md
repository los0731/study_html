# CSS

### .container
Now click the `style.css` tab in the middle of the code editor. The `.container`, that has all the elements, should be in the middle of the screen and shouldn't be wider than the already predetermined width. 
* `.container`'s margin is `24px` top/down, `auto` left/right.
* Padding is `0` top/down, `16px` left/right.
* The maximum width is `960px`.

**Instructions**
1. Apply style to `.container`
    ```css
    .container {
      margin: 24px auto;
      padding: 0 16px;
      max-width: 960px;
    }
    ```



### Logo Image
let's style the logo image. 
- The width of `img` is `183px`.

**Instructions**
1. Apply style to `img`
    ```css
    img {
      width: 183px;
    }
    ```



Click the **NEXT STEP** button.



## TIPS
* What is the difference between margin or padding with 4 values vs 2 values? 

    > If you enter 4 values, they will be applied clockwise, starting from the top. You can shorten this process to entering 2 values, in which case the browser applies the first value to the top and bottom and the second to left and right. 
    >
    > margin: 10px 20px 10px 8px --> top / right / bottom / left
    >
    > margin: 10px 20px --> vertical(top/down) / Horizontal(left/right)

* Margin: auto;

    > The margin's `auto` value is automatically calculated by the browser for the maximum value. If left/right margins are set to `auto` the browser places the element in the middle of the screen. 

* What if you want to use a clear and focused image from the Internet? 

    > When using online images, you have to use an image file, that's twice it's size. it's tthat the image stays clear and focused on a high resolution display, like Apple Macbook's Retina. For example if you are going to have a 100x100 image on the web, the image's file should have the size of 200x200. 

* Is it important to reduce the file size of an image file?

    > The sort answer is yes. File size is very very important. It affects the speed of the final page To make the image file size smaller, I use online image optimization services, like https://tinypng.com. Personally, I don't use images bigger than `1MB`. In fact, if possible, I try to use images smaller than `100kb`. 

* 0px vs 0 

    > If you set a value as `0`, it's better not to put a unit like `px`. That way the code stays simple and clear (but FYI. `0px` is not a mistake!).