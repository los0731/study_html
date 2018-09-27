## .content
let's choose the style of the content area.
* `.content`의 위 패딩은 `136px`입니다.
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
- `.form-search-wrap`의 `position`은 `relative`입니다.
- 마진은 상/우/하/좌 `24px auto 0 auto`입니다.
- The width is `50%`.
- The maximum area is `584px`.
- The minimum area is `428px`.

**Instructions**
1. `.form-search-wrap`의 스타일 적용하기.
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
- `.form-search`의 패딩은 상/하 `5px`, 좌/우 `16px`입니다.
- `outline`을 제거합니다.
- No boundary line.
- 모서리의 둥글기는 `2px`입니다.
- 넓이는 `100%`에서 `32px`만큼 뺀 만큼의 길이 입니다.
- The font size is `16px`.
- 행간은 `34px`입니다.
- 그림자의 x축/y축/퍼짐(blur)/크기는 `0 2px 2px 0 rgba(0,0,0,0.16)`, `0 0 0 1px rgba(0,0,0,0.08)` 2개의 속성을 같이 사용합니다.
- `transition` 속성은 `.2s` 입니다.

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
- `.form-search:hover, .form-search:focus`의 그림자의 x축/y축/퍼짐(blur)/크기는 `0 3px 8px 0 rgba(0,0,0,0.2), 0 0 0 1px rgba(0,0,0,0.08)` 2개의 속성을 같이 사용합니다.

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

- `.btn-voice`의 `position`은 `absolute`입니다.
- 위에서부터 `10px`만큼 떨어져 있습니다.
- 오른쪽에서 `10px`만큼 떨어져 있습니다.
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
- `.buttons-wrap`의 위 마진은 `40px`입니다.

**Instructions**
1. Apply style to `.buttons-wrap`.
   ```css
   .buttons-wrap {
     margin-top: 40px;
   }
   ```



## .btn-secondary
let's go ahead and define the style of the two buttons.
- `.btn-secondary`의 마진은 상/하 `0`, 좌/우 `4px`입니다.
- 패딩은 상/하 `10px`, 좌/우 `16px`입니다.
- 경계선은 `1px`의 직선이지만 투명합니다.
- 모서리의 둥글기는 `2px`입니다.
- The font size is `13px`.
- 글씨 두께는 `bold`입니다.
- 행간은 `16px`입니다.
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