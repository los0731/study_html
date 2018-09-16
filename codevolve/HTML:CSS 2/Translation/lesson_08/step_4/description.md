## .content
컨텐트 영역에는 구글 로고 이미지와 검색 입력폼이 있습니다. 그리고 'Google Search', 'I'm Feeling Lucky'버튼도 있습니다.

**Instructions**

1. `<div class="content">`안에 `<img>`를 추가하고, `src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"`, `alt="Google"`, `width="272"` 적용하기.

    ```html
    <img src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png" alt="Google" width="272">  
    ```
1. `<img>`  아래에 `<div>`를 추가하고, `class="form-search-wrap"` 적용하기 
    ```html
    <div class="form-search-wrap"></div>       
    ```
1. `<div class="form-search-wrap">`안에 `<a>`를 추가하고 `class="btn-voice"`로 적용 및 내용에 `mic`아이콘을 추가하기. 그리고 `<input>`를 추가하고 `type="text"`, `class="form-search"` 적용하기   
    ```html
    <div class="form-search-wrap">
      <a href="" class="btn-voice"><i class="material-icons">mic</i></a>
      <input type="text" class="form-search">
    </div>
    ```
1. `<div class="form-search-wrap">`다음에 `<div>`를 추가하고 `class="buttons-wrap"` 적용하기  
    ```html
    <div class="buttons-wrap"></div>
    ```
1. `<div class="form-search-wrap">`안에 2개의 `<a>`를 추가하고 각각 `class="btn-search"`, `class="btn-lucky"` 적용 및 내용 채우기. 
    ```html
    <div class="buttons-wrap">
      <a href="" class="btn-search">Google Search</a>
      <a href="" class="btn-lucky">I'm Feeling Lucky</a>
    </div>
    ```



## .footer
푸터는 문서에 대한 꼬릿말로서, 그 문서에 대한 정보를 담고 있습니다. 보통 회사 정보나, 이용약관, 개인정보 보호정책, 그리고 몇몇 다른 링크를 첨부하죠. Google 검색 페이지는 다음의 정보들을 담고 있습니다. 
> * Privacy
> * Terms
> * Settings
> * Advertising
> * Business

그리고 Privacy, Terms, Settings는 오른편에, 나머지는 왼편에 배치되어있습니다. 따라서 작성한 `<nav class="navigation">`과 마찬가지로 양쪽 영역을 구분합니다.

**Instructions**
1. `<footer class="footer">`안에 2개의 `<div>`추가하고, 각각 `class="footer-right"`, `class="footer-left"` 적용하기. 
    ```html
    <footer class="footer">
      <div class="footer-right"></div>
      <div class="footer-left"></div>
    </footer>
    ```
1. `<div class="footer-right">`안에 3개의 `<a href="">` 추가하고 각각 내용 채우기. 
    ```html
    <div class="footer-right">
      <a href="">Privacy</a>
      <a href="">Terms</a>
      <a href="">Settings</a>
    </div>
    ```
1. `<div class="nav-right">`태그 안에 2개의 `<a href="">` 추가하고 각각 내용 채우기.   
    ```html
    <div class="footer-left">
      <a href="">Advertising</a>
      <a href="">Business</a>
    </div>
    ```


 Click the **NEXT STEP** button.

