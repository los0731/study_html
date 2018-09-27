## .content
In the content area there are the Google logo image and the search input form. There are also `Google Search`, `I'm Feeling Lucky` buttons. 

**Instructions**

1. In `<div class="content">` add `<img>` and apply `src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"`, `alt="Google"`, `width="272"`

    ```html
    <img src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png" alt="Google" width="272">  
    ```
1. After the `<img>` add `<div>` and apply `class="form-search-wrap"`
    ```html
    <div class="form-search-wrap"></div>       
    ```
1. In `<div class="form-search-wrap">` add `<a>` and apply `class="btn-voice"` and add `mic` icon to the content. Add `<input>` and apply `type="text"`, `class="form-search"`.
    ```html
    <div class="form-search-wrap">
      <a href="" class="btn-voice"><i class="material-icons">mic</i></a>
      <input type="text" class="form-search">
    </div>
    ```
1. After `<div class="form-search-wrap">` add `<div>` and apply `class="buttons-wrap"`.
    ```html
    <div class="buttons-wrap"></div>
    ```
1. In `<div class="form-search-wrap">` add 2 `<a>`and apply respectively `class="btn-search"`, `class="btn-lucky"` and fill with contents.
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
1. In `<footer class="footer">` add 2 `<div>` and apply respectively `class="footer-right"`, `class="footer-left"`.
    ```html
    <footer class="footer">
      <div class="footer-right"></div>
      <div class="footer-left"></div>
    </footer>
    ```
1. In `<div class="footer-right">` add 3 `<a href="">` and fill each with contents.
    ```html
    <div class="footer-right">
      <a href="">Privacy</a>
      <a href="">Terms</a>
      <a href="">Settings</a>
    </div>
    ```
1. In `<div class="nav-right">` tag add 2 `<a href="">` and fill each with contents.   
    ```html
    <div class="footer-left">
      <a href="">Advertising</a>
      <a href="">Business</a>
    </div>
    ```

 

Click the **NEXT STEP** button.

