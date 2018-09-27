## .navigation

let's define the style of the navigation part. First, in the navigation there are `<div class="nav-left">` and `<div class="nav-right">`, where both `<div>` have to be dispatched on the left/right. To dispatch the elements inside horizontally, it is good to use `flex` function. 

* `.navigation`'s `display` is `flex`.
* The elements inside that have `flex` applied, are arranged centrally and vertically.
* The elements inside that have `flex` applied, are dispatched on the left/right.
* For the padding is `16px 30px 16px 10px` for top/right/down/left.


**Instructions**
1. Apply style to `.navigation`.
    ```css
    .navigation {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 16px 30px 16px 10px;
    }
    ```



## .navigation a
let's arrange the style of `a` in the navigation. 

- The margin of `.navigation a` is `15px`.
- The font size is `13px`.
- The line height is `16px`.
- The font color is `#333`.

**Instructions**

1. Apply style to `.navigation a`.
   ```css
   .navigation a {
     margin-left: 15px;
     font-size: 13px;
     line-height: 16px;
     color: #333;
   }
   ```



## .navigation a:hover
`a:hover`, which is inside the navigation, needs a style. Additionally, the  `<a>`there will have a seperate style defined with a `.btn`, so here we have to exclude it. that's why we will use the `:hover` and `:not` selectors together. 

- `.navigation a:hover:not(.btn)`의 투명도는 `.85`입니다.
- The text has `underline` applied.


**Instructions**
1. Apply style to `.navigation a:hover:not(.btn)`.
   ```css
   .navigation a:hover:not(.btn) {
     opacity: .85;
     text-decoration: underline;
   }
   ```



## .btn-apps

We will now arrange the style of `a.btn-apps`. Here, I don't just use `.btn-apps` but `a.btn-apps`. If we use just a class here, other higher priority properties may get applied. that's why we use the tag and class together to rise the priority higher. 

- `a.btn-apps`'s `display` attribute is `flex`.
- Padding is `3px`.
- The font color is `#737373`.

**Instructions**
1. Apply style to `a.btn-apps`.
   ```css
   a.btn-apps {
     display: flex;
     padding: 3px;
     color: #737373;
   }
   ```



## .btn-sign-in

In the upper right corner, define the style of the 'sign-in` button.  

- The padding of `a.btn-sign-in` is `8px` top/down, `13px` left/right.
- The rounded edges are `2px`.
- The font-weight is `bold`.
- The line height is `14px`.
- The font color is `white`.
- Background color is `#4387fd`.

**Instructions**
1. Apply style to `a.btn-sign-in`.
   ```css
   a.btn-sign-in {
     padding: 8px 13px;
     border-radius: 2px;
     font-weight: bold;
     line-height: 14px;
     color: white;
     background-color: #4387fd;
   }
   ```


## .btn-sign-in:active
If you move your mouse over an element it says `:hover`, doesn't it? What happens when you click the mouse? Active mode is applied to the 'sign-in` button!
- Background color of `a.btn-sign-in:active` is `#3c7ae4`.
- The shadow's x-axis/y-axis/blur/size/color is  `inset 0 2px 0 rgba(0,0,0,.15)`.

**Instructions**
1. Apply style to `a.btn-sign-in:active`. 
   ```css
    a.btn-sign-in:active {
      background-color: #3c7ae4;
      box-shadow: inset 0 2px 0 rgba(0,0,0,.15);
    }
   ```



## .nav-right
Once you've styled the `sign-in` button, the buttons will be placed from top to down. In `.nav-right` let's use `flex` to arrange the buttons horizontally.
- `.nav-right`'s `display` attribute is `flex`.
- The internal elements which have `flex` applied, are centered at the y-axis.

**Instructions**
1. Apply style to `.nav-right`.
   ```css
   .nav-right {
     display: flex;
     align-items: center;
   }
   ```



Click the **NEXT STEP** button.