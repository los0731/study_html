# HTML
Using `<div>`, we create a card. Inside it let's use `<a>` to add a link. The main element of the card goes into `<a>`. The following elements gare part of the card. 
> - Hero image (the image used in the card)
> - Title
> - Body text
> - Dividing line
> - Contents type
> - `VIEW MORE` text that appears when we hover over it. 

**Instructions**
1. Add `<div>` within `<body>` and apply `class="card"`.
    ```html
    <body>
      <div class="card"></div>
    </body>
    ```
1. Add `<a>` within `<div class="card">` and apply `href="https://facebook.design/videos/designing-at-facebook"`.
    ```html
    <div class="card">
      <a href="https://facebook.design/videos/designing-at-facebook"></a>
    </div>
    ```



### .card-hero 
Hero image is usually big, take up the full screen and is set on top of the designated area. Hero image sets the tone for the page, sparks curiosity in the users before reading the contents or simply conveys the general message of the text. This element will be handled with CSS, so for now we just leave an empty tag and class. 

**Instructions**
1. Add `<div>` within `<a>` and apply `class="card-hero"`.
    ```html
    <a href="https://facebook.design/videos/designing-at-facebook">
      <div class="card-hero"></div>
    </a>
    ```



### .card-block
Other than the hero image, the rest of the elements (title, descriptions, dividing lines, tags etc.) will be grouped together. These elements are called `card-block`. 

**Instructions**
1. Add `<div>` below `<div class="card-hero">` and apply `class="card-block"`
    ```html
    <div class="card-hero"></div>
    <div class="card-block"></div> 
    ```

1. Add `<h2>` in `<div class="card-block">` and, after applying `class="card-title"`, fill out the contents.

    ```html
    <div class="card-block">
      <h2 class="card-title">Designing at Facebook</h2> 
    </div>  
    ```

1. After `<h2 class="card-title>` add `<p>` and, after applying `class="card-description"`, fill out with contents.
    ```html
    <p class="card-description">Get a sneak peek at the design process at Facebook from product designers Cat Audi and George Kedenburg III.</p>       
    ```

1. Add `<hr>` below `<p class="card-description">` and apply `class="card-hrclass="`.
    ```html
    <hr class="card-hr">       
    ```

1. After `<hr class="card-hr">` add 2 `<h6>` and, after applying respectively `class="card-type"`, `class="card-tag"`, fill out with contents.
    ```html
    <h6 class="card-type">VIDEO</h6>
    <h6 class="card-tag">VIEW MORE</h6>
    ```


Click the **NEXT STEP** button.



## TIPS!

- Why does `<div class="card-hero">` use `<div>` instead of `<img>`?

  > Most hero images use `background` property in the `<div>` tag not the `<img>`. The reason for that is as follows: 
  >
  > - Usually, the hero images shown on the list, are imported from original pages, so the ratios of the images vary a lot. The `ìmg` tag has a fixed ratio, meaning the image can get stretched or narrowed down when forced to be displayed that way on the page. 
  > - Because the area proportions have to constantly change to fit the various devices (desktop, mobile tablet), using `<img>` is limiting for us. 

