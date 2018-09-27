## .content
In the content area there are the Google logo image and the search input form. There are also `Google Search`, `I'm Feeling Lucky` buttons. 

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
A footer is a reference section of a document, it contains information about the document. It usually has company information, terms of use, privacy policy and several other links. In the Google search page, there are the following information.
> * Privacy
> * Terms
> * Settings
> * Advertising
> * Business

The Privacy, Terms, Settings are on the right, the rest are placed on the left. Just like with `<nav class="navigation">` this section is seperated into two.

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

