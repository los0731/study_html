# 시작하기 전에 - 구글 아이콘
이 페이지에는 음성 검색 버튼과 구글 Apps 버튼에 아이콘을 사용할 예정입니다. 아이콘 이미지를 사용하는 방법은 여러가지가 있지만 (예를들어 이미지를 첨부할 수도 있고요.) 이 레슨에서는 웹 아이콘 폰트를 사용할 겁니다. `head`태그에 아이콘을 사용하기 위한 한줄의 코드가 첨부 되어있습니다. 

```html
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
```

이 코드가 추가된 상태에서 `i`태그를 사용해서 아이콘을 추가할 수 있습니다. 

```html
<i class="material-icons">mic</i>
<i class="material-icons">accessibility</i>
<i class="material-icons">assessment</i>
<i class="material-icons">alarm</i>
```

또 이 아이콘에 클래스를 추가하여 아이콘의 [크기를 조절][3]할 수 있습니다. 
```html
<i class="material-icons md-18">mic</i>
<i class="material-icons md-24">accessibility</i>
<i class="material-icons md-36">assessment</i>
<i class="material-icons md-48">alarm</i>
```

이 아이콘 폰트를 사용하는 더 자세한 방법을 알아보고 싶다면 [Material Design - Icon][2] 항목에 자세한 가이드가 나와있습니다.



# 시작하기
이 페이지는 크게 3부분으로 구분합니다. 네이게이션 영역, 컨텐트 영역, 푸터 영역입니다. 큰 뼈대 먼저 추가합니다.

**Instructions**
1. `body`태그 안에 `nav`태그를 추가하고, class는 `navigation`으로 적용하기. 
    ```html
    <body>
      <nav class="navigation"></nav>
    </body>
    ```
1. `<nav class="navigation">` 다음에 `div`태그를 추가하고, class는 `content`로 적용하기. 
    ```html
    <div class="content"></div>
    ```
1. `<div class="content">` 다음에 `footer`태그를 추가하고, class는 `footer`로 적용하기. 
    ```html
    <footer class="footer"></footer>
    ```



## 네비게이션
nav 태그는 탐색 링크들의 집합을 정의합니다. 눈으로 화면을 보지 않는 사람들을 위한 화면 판독기는 nav태그를 인식해서 페이지를 더 쉽게 탐색할 수 있도록 도와주기도 합니다. 이 페이지는 다음의 링크들을 가지고 있습니다.
> * About link
> * Store link
> * Gmail link
> * Images link
> * Apps button
> * Sign In button

그리고 About, Store는 왼편에, 나머지는 오른편에 배치되어있습니다. 따라서 왼쪽 영역과 오른쪽 영역을 구분합니다. 

**Instructions**
1. `<nav class="navigation">`태그 안에 2개의 `div`태그 추가하고, 클래스를 각각 `nav-left`, `nav-right`으로 적용하기. 
    ```html
    <nav class="navigation">
      <div class="nav-left"></div>
      <div class="nav-right"></div>
    </nav>
    ```
1. `<div class="nav-left">`태그 안에 2개의 `a`태그 추가하고 각각 내용 채우기. (실제 기능 개발은 아니기 때문에 href attribute는 비워둡시다.) 
    ```html
    <div class="nav-left">
      <a href="">About</a>
      <a href="">Store</a>
    </div>
    ```
1. `<div class="nav-right">`태그 안에 아래와 같이 4개의 `a`태그 추가하고 각각 내용 채우기. 버튼을 사용할 마지막 2개의 태그에는 클래스를 각각 `btn btn-apps`, `btn btn-sign-in`으로 적용하기. 그리고 3번째 태그에는 `apps`아이콘을 추가하고 크기 조절하는 클래스 `md-24`을 적용하기.   
    ```html
    <div class="nav-right">
      <a href="">Gmail</a>
      <a href="">Images</a>
      <a href="" class="btn btn-apps"><i class="material-icons md-24">apps</i></a>
      <a href="" class="btn btn-sign-in">Sign in</a>
    </div>
    ```



다음 페이지에서 컨텐트와 푸터의 HTML 코드를 작성합니다.
**NEXT STEP** 버튼을 클릭하세요.



## TIPS!

- `head`태그 안에 추가하는 css 태그 `<link rel="stylesheet" href="...">`를 추가하는 순서가 있는건가요? 

  > 네. 결론적으로 아래에 추가된 코드일 수록 우선순위가 높습니다. 따라서 가장 공통적이고 보편적인 스타일일 담당하는 코드를 위에, 상세한 스타일을 담당하는 코드를 아래에 둡니다.  
  > ```html
    `style-A.css`파일과 `style-B.css`파일을 사용한다고 생각합시다. 우리는 제품을 만드는 과정에서 style-A에서는 `h1 {color: black;}`이라고 하고, `style-B`에서는 `h1 {color: blue;}`로 지정하는 경우를 쉽게 만날 수 있습니다. 이때 어떤 스타일을 더 최종적으로 적용해야 할지 기준이 필요합니다. 
    ```


[2]:https://material.io/tools/icons
[3]:https://google.github.io/material-design-icons/#styling-icons-in-material-design