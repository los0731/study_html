# content
컨텐트 영역의 스타일을 적용합시다.
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



## form-search-wrap
검색 폼과 음성 검색 버튼을 감싸고 있는 이 요소는 `position: relative;`으로 지정해주어야 합니다. 이유는 이후에 나올 음성 검색 버튼에서 설명하겠습니다. 다음의 스타일들을 적용해 봅시다.      
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



## form-search
이 페이지에서 가장 중요한 요소라면 역시 검색 폼일 겁니다. 이 검색 폼의 스타일을 적용해 봅시다.
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



## form-search - hover, focus
검색 폼의 마우스를 올리거나 클릭해서 폼에 포커스 되어 있을 때, 그림자가 살짝 길어지도록 해야합니다.      
- `.form-search:hover, .form-search:focus`의 그림자의 x축/y축/퍼짐(blur)/크기는 `0 3px 8px 0 rgba(0,0,0,0.2), 0 0 0 1px rgba(0,0,0,0.08)` 2개의 속성을 같이 사용합니다.

**Instructions**
1. Apply style to `.form-search:hover,` and `.form-search:focus`.
   ```css
   .form-search:hover,
   .form-search:focus {
     box-shadow: 0 3px 8px 0 rgba(0,0,0,0.2), 0 0 0 1px rgba(0,0,0,0.08);
   }
   ```



## btn-voice
마이크 아이콘을 사용하는 음성 검색 버튼은 검색 폼 안에 위치하도록 해야하는데, 그렇기 위해서는 `position`속성을 `absolute`로 지정해 주어야 합니다. 한번 해봅시다.      

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


## buttons-wrap
검색 폼 아래에 있는 2개의 버튼에 스타일을 지정합니다. 물론 그전에 그 둘을 싸고 있는 이 요소에 간격부터 정의 합시다.      
- `.buttons-wrap`의 위 마진은 `40px`입니다.

**Instructions**
1. Apply style to `.buttons-wrap`.
   ```css
   .buttons-wrap {
     margin-top: 40px;
   }
   ```



## btn-secondary
본격적으로 두 버튼의 스타일을 정의합니다.  
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


## btn-secondary - hover
이 버튼의 hover 상태에는 다음과 같은 스타일을 적용합니다.  
- `.btn-secondary:hover`의 경계선의 색상은 `#c6c6c6`입니다. 
- The font color is `#222`.
- 그림자의 x축/y축/퍼짐(blur)/크기는 `0 1px 1px rgba(0,0,0,0.1);`입니다.

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