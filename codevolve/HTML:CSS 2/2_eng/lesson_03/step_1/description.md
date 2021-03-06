# HTML

## <div class="business-card"\>

We're going to put the business card on a very light grey background. Start with using `<div>` to make an outline for the business card.  

**lesson3_step1_instruction1**
1. Add `<div>` within `<body>` and apply `class="business-card"`.
    ```html
    <div class="business-card"></div>
    ```



## Fill out the contents of the business card
In `<div class="business-card">` we add the card elements. In this card there is an image that illustrates the appropriate concept, name, information (job position, phone number, email). We take an image from `iconfinder.com` and then we will use a list tag, without any specific order of elements, to arrange the information (job position, phone number, email).

**lesson3_step1_instruction2**
1. Add `<img>` and apply `class="image"` and `alt="Profile image"`.

    ```html
    <div class="business-card">
       <img class="image" src="https://cdn3.iconfinder.com/data/icons/fantasy-and-role-play-game-adventure-quest/512/Orc-512.png" alt="Profile image">
     </div> 
    ```
1. Add `<h2>` and apply `class="name"`.
    ```html
    <img class="image" src="..." alt="...">
    <h2 class="name">Jonathan Harris</h2>  
    ```
1. Add `<ul>` and apply `class="information"`. 
    ```html
    <h2 class="name">...</h2> 
    <ul class="information"></ul> 
    ```
1. In the `<ul>`, add `<li>` and apply the following classes to each of the information: job position/phone number/email. 
    ```html
    <ul class="information">
      <li class="job">Orc</li>
      <li class="phone">+1.23.456.7890</li>
      <li class="mail">jonathan@blackrockclan.com</li>
    </ul> 
    ```



Click the **NEXT STEP** button.


