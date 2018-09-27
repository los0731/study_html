# HTML
Start by using `<div>` to make the frame of the card.

**Instructions**
1. Add `<div>` within `<body>` and apply `class="birthday-card`.
    ```html
    <div class="birthday-card"></div>
    ```



### .birthday-card
Add elements of card in `<div class="birthday-card">`.

**Instructions**
1. Add `<img>`, and apply `src="https://image.freepik.com/free-vector/birthday-background-with-hand-drawn-gift_23-2147645419.jpg"` and `alt="Birthday image"`. 
    ```html
    <img src="https://image.freepik.com/free-vector/birthday-background-with-hand-drawn-gift_23-2147645419.jpg" alt="Birthday Image">
    ```
1. Using `<h1>`, enter card text contents, after the image 
    ```html
    <h1>Happy Birthday. Hope you are having a great day Michelle.</h1> 
    ```
1. After the contents, use `<h3>` to enter the card author 
    ```html
    <h3>from Frank</h3>
    ```



### Leave the image's source for now.
If you are not a designer, it's difficult to make and use your own graphic sources. that's why when you need an image, you can use free source sites. Here are some popular sites that you can check out:
* https://www.freepik.com/ (You can use graphic images/illustrations for personal/commercial use, but you have to leave in the source)
* https://www.pexels.com/ (For pictures taken by professional photographers, you don't have to leave in the source. )
* https://www.iconfinder.com/free_icons (For free icons, when used for personal/commercial, source must be left in. )

You can download the image source file from here or you can click the right mouse button and `save image address` to use the picture in our project. The important thing is not violate the copyrights.     

**Instructions**
1. Below `<div class="birthday-card">` add `<h6>` and apply `class="sources-link"` to it.
    ```html
    <h6 class="sources-link"></h6>
    ```
1. Inside `<h6>` add`<a>` and after applying `href="https://www.freepik.com/free-photos-vectors/background"`to it, add the content below 
    ```html
    <h6 class="sources-link">
      <a href="https://www.freepik.com/free-photos-vectors/background">Background vector created by Freepik</a>
    </h6> 
    ```



Click the **NEXT STEP** button.



## TIPS
* The reason for adding `alt` attribute to images

    > `Alt` attribute is an abbreviation for `alternate`. it's the alternate text that you see when the picture is not displayed normally. For example, when the user cannot see the screen, she can `hear the image` through a screen-reader. that's when you hear what's inside the `alt` attribute. Also, when the network connection is not good and the image fails to load, the `alt` content is displayed. 