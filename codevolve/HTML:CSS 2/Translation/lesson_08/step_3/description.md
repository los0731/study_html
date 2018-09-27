# HTML
This page has 3 major sections: navigation / contents / footer. 

**Instructions**
1. `<body>`안에 `<nav>`를 추가하고, `class="navigation"`적용하기. 
    ```html
    <body>
      <nav class="navigation"></nav>
    </body>
    ```
1. `<nav class="navigation">`다음에 `<div>`를 추가하고, `class="content"`적용하기. 
    ```html
    <div class="content"></div>
    ```
1. `<div class="content">`다음에 `footer`태그를 추가하고, `class="footer"` 적용하기. 
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
1. `<nav class="navigation">`태그 안에 2개의 `<div>`를 추가하고, 각각 `class="nav-left"`, `class="nav-right"` 적용하기. 
    ```html
    <nav class="navigation">
      <div class="nav-left"></div>
      <div class="nav-right"></div>
    </nav>
    ```
1. `<div class="nav-left">`태그 안에 2개의 `<a href="">`를 추가하고, 내용 채우기. (실제 기능 개발은 아니기 때문에 href attribute는 비워둡시다.) 
    ```html
    <div class="nav-left">
      <a href="">About</a>
      <a href="">Store</a>
    </div>
    ```
1. `<div class="nav-right">`태그 안에 아래와 같이 4개의 `<a href="">` 추가하고 각각 내용 채우기. 버튼으로 사용할 마지막 2개의 태그에는 각각 `class="btn btn-apps"`, `class="btn btn-sign-in"` 적용하기. 그리고 `<a href="" class="btn btn-apps">`에 `apps`아이콘을 추가하고 크기 조절하는 `class="md-24"` 적용하기.   
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

