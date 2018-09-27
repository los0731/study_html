# HTML
This page has 3 major sections: navigation / contents / footer. 

**Instructions**
1. Add `<nav>` in `<body>` and apply `class="navigation"`.
    ```html
    <body>
      <nav class="navigation"></nav>
    </body>
    ```
1. After `<nav class="navigation"> add `<div>` and apply `class="content"`
    ```html
    <div class="content"></div>
    ```
1. After `<div class="content">` add `footer` tag and apply `class="footer"`
    ```html
    <footer class="footer"></footer>
    ```



## <nav>
`<nav>` defines a set of navigation links. For people who cannot see the screen, screen readers recognize `<nav>` and help them navigate the page more easily. that's why it's really good practise to use `<nav>` in the navigation area to get all the navigation links together. This page's navigation has the following links. 

> About link
> Store link
> Gmail link
> Images link
> Apps button
> Sign In button

About, Store are placed on the left, the rest are on the right. That means the left and right areas are seperated. 

**Instructions**
1. In the `<nav class="navigation">` tag add 2 `<div>` and apply `class="nav-left"`, `class="nav-right"` respectively
    ```html
    <nav class="navigation">
      <div class="nav-left"></div>
      <div class="nav-right"></div>
    </nav>
    ```

1. In the `<div class="nav-left">` tag add 2 `<a href="">` and fill with contents (leave the href attribute empty, as this is just practice programming).
    ```html
    <div class="nav-left">
      <a href="">About</a>
      <a href="">Store</a>
    </div>
    ```

1. In the `<div class="nav-right">` tag add 4 `<a href="">` and fill each with contents. 

    Apply respectively `class="btn btn-apps"`, `class="btn btn-sign-in"`to the last 2 tags, that will be used as buttons. 

    Also in `<a href="" class="btn btn-apps">` add `apps` icon and apply size adjustment of `class="md-24"`

    ```html
    <div class="nav-right">
      <a href="">Gmail</a>
      <a href="">Images</a>
      <a href="" class="btn btn-apps"><i class="material-icons md-24">apps</i></a>
      <a href="" class="btn btn-sign-in">Sign in</a>
    </div>
    ```



Next, let's write HTML code for the page's content and footer. 
Click the **NEXT STEP** button.



## TIPS!

- Is there a specific order of adding the CSS tag  `<link rel="stylesheet" href="...">` in the `<head>`?

  > Yes, there is. The code at the bottom, has higher priority. that's why the codes of all the common and universal styles are placed at the top and the oned responsible for the detailed styling are at the bottom. 
  >
  > Suppose you are using a file `style-A.css` and a file `style-B.css`. In the process of making our page, we can easily get into a situation where in `style-A` we define `h1 {color: black;}` and in `style-B` we define `h1 {color: blue;}`. In such case, we need criteria for which style to ultimately implement. 


[2]:https://material.io/tools/icons
[3]:https://google.github.io/material-design-icons/#styling-icons-in-material-design

