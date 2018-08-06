# HTML
이 페이지는 크게 3부분으로 구분합니다. 네이게이션 / 컨텐트 / 푸터입니다. 

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



## 네비게이션
`<nav>`는 탐색 링크들의 집합을 정의합니다. 눈으로 화면을 보지 않는 사람들을 위한 화면 판독기는 `<nav>`를 인식해서 페이지를 더 쉽게 탐색할 수 있도록 도와주기도 합니다. 따라서 탐색 링크들이 모인 네비게이션 영역에는 이 `<nav>`를 사용하는 것이 좋습니다. 이 페이지의 네비게이션에는 다음의 링크들이 있습니다.
> About link
> Store link
> Gmail link
> Images link
> Apps button
> Sign In button

그리고 About, Store는 왼편에, 나머지는 오른편에 배치되어있습니다. 따라서 왼쪽 영역과 오른쪽 영역을 구분합니다. 

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



다음 페이지에서는 컨텐트와 푸터의 HTML 코드를 작성합시다.
**NEXT STEP** 버튼을 클릭하세요.



## TIPS!

- `<head>` 안에 추가하는 css 태그 `<link rel="stylesheet" href="...">`를 추가하는 순서가 있는건가요? 

  > 네. 아래에 추가된 코드일 수록 우선순위가 높습니다. 따라서 가장 공통적이고 보편적인 스타일일 담당하는 코드를 위에, 상세한 스타일을 담당하는 코드를 아래에 둡니다.  
  > ```html
    `style-A.css`파일과 `style-B.css`파일을 사용한다고 생각합시다. 우리는 제품을 만드는 과정에서 style-A에서는 `h1 {color: black;}`이라고 하고, `style-B`에서는 `h1 {color: blue;}`로 지정하는 경우를 쉽게 만날 수 있습니다. 이때 어떤 스타일을 더 최종적으로 적용해야 할지 기준이 필요합니다. 
    ```


[2]:https://material.io/tools/icons
[3]:https://google.github.io/material-design-icons/#styling-icons-in-material-design