## .content
let's choose the style of the content area.
* `.content` top padding is `136px`.
* The letters are centered.

**Instructions**
1. Apply style to `.content`.
    ```css
    .content {
      padding-top: 136px;
      text-align: center;
    }
    ```



## .form-search-wrap
The element around the search form and voice search button should be set as `position: relative;`. The reason for this is explained further along in the `voice search button` part. let's go on with applying other styles.
- `.form-search-wrap`'s `position` is `relative`.
- The margin for top/right/down/left is `24px auto 0 auto`.
- The width is `50%`.
- The maximum area is `584px`.
- The minimum area is `428px`.

**Instructions**
1. Apply the style of `.form-search-wrap`.
   ```css
   .form-search-wrap {
     position: relative;
     margin: 24px auto 0 auto;
     width: 50%;
     max-width: 584px;
     min-width: 428px;
   }
   ```



## .form-search
The most important element on this page will be, of course, the search form. let's choose the style for this form.
- The padding of `.form-search` is `5px` top/down, `16px` left/right.
- Remove `outline`.
- No boundary line.
- The rounded edges are `2px`.
- The width is the difference between `100%` and `32px`.
- The font size is `16px`.
- The line height is `34px`.
- The shadow's x-axis/y-axis/blur/size/color has 2 attributes of `0 2px 2px 0 rgba(0,0,0,0.16)`, `0 0 0 1px rgba(0,0,0,0.08)`
- `transition`attribute is `.2s` .

**Instructions**
1. Apply style to `.navigation a:hover:not(.btn)`.
   ```css
   .form-search {
     padding: 5px 16px;
     outline: none;
     border: 0;
     border-radius: 2px;
     width: calc(100% - 32px);
     font-size: 16px;
     line-height: 34px;
     box-shadow: 0 2px 2px 0 rgba(0,0,0,0.16), 0 0 0 1px rgba(0,0,0,0.08);
     transition: .2s;
   }
   ```



## .form-search:hover, .form-search:hover
By hovering the mouse over it or by clicking the form, make sure that the shadows are slightly longer, when the form is in focus.  
- `.form-search:hover, .form-search:focus`'s shadows' x-axis/y-axis/blur/size/color has 2 attributes of `0 3px 8px 0 rgba(0,0,0,0.2), 0 0 0 1px rgba(0,0,0,0.08)`.

**Instructions**
1. Apply style to `.form-search:hover,` and `.form-search:focus`.
   ```css
   .form-search:hover,
   .form-search:focus {
     box-shadow: 0 3px 8px 0 rgba(0,0,0,0.2), 0 0 0 1px rgba(0,0,0,0.08);
   }
   ```



## .btn-voice
The voice search button, represented by the microphone icon, should be placed within the the search form, and to do so the `position` properties should be set to `absolute`. let's try to do this now.  

- `.btn-voice`'s `position` is `absolute`.
- It's `10px` from above.
- It's `10px` from the right.
- The font color is `#4387fd`.

**Instructions**
1. Apply style to `.btn-voice`.
   ```css
   .btn-voice {
     position: absolute;
     top: 10px;
     right: 12px;
     color: #4387fd;
   }
   ```


## .buttons-wrap
Go ahead and style the two buttons under the search form. Before doing that though, let's define the space between those those two elements.    
- The margin of `.buttons-wrap` is 40px.

**Instructions**
1. Apply style to `.buttons-wrap`.
   ```css
   .buttons-wrap {
     margin-top: 40px;
   }
   ```



## .btn-secondary
let's go ahead and define the style of the two buttons.
- Margin of `.btn-secondary` is `0` for top/down `4px` for left/right.
- Padding is `10px` top/down, `16px` left/right.
- The border is a `1px` solid line, but it's transparent.
- The rounded edges are `2px`.
- The font size is `13px`.
- The font-weight is `bold`..
- The line height is `16px`.
- The font color is `#757575`.
- Background color is `#f2f2f2`.

**Instructions**
1. Apply style to `.nav-right`.
   ```css
   .btn-secondary {
     margin: 0 4px;
     padding: 10px 16px;
     border: 1px solid transparent;
     border-radius: 2px;
     font-size: 13px;
     font-weight: bold;
     line-height: 16px;
     color: #757575;
     background-color: #f2f2f2;
   }
   ```



## .btn-secondary:hover

let's apply the following styles to the `hover` mode of this button.
- `.btn-secondary:hover`'s border line's color is `#c6c6c6`.
- The font color is `#222`.
- The shadow's x-axis/y-axis/blur/size is `0 1px 1px rgba(0,0,0,0.1);`.

**Instructions**
1. Apply style to `.btn-secondary:hover`.
   ```css
   .btn-secondary:hover {
     border-color: #c6c6c6;
     color: #222;
     box-shadow: 0 1px 1px rgba(0,0,0,0.1);
   }
   ```



Click the **NEXT STEP** button.