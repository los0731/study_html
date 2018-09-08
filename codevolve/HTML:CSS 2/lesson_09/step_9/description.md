## footer

`<footer>` 는 지역 언어 버튼, 도움말/개인정보 보호/약관 버튼을 포함합니다. `footer`의 스타일을 지정합니다.

- `footer`의 위 마진은 `16px`입니다. 

**Instructions**

1. `footer`의 스타일 적용하기.

   ```css
   footer {
     margin-top: 16px;
   }
   ```



## .btn-locale

`<footer>` 안에 위치한 지역 언어 버튼 `<select class="btn-locale">`의 스타일을 지정합니다. `<select>`는 태그의 특성상 dropdown mark가 표시되고, 일부 스타일이 적용되지 않습니다. 때문에 `-webkit-appearance: none;`를 적용하여 기본 속성을 제거 후 스타일을 적용할 수 있습니다.

- `.btn-locale`의 위 마진은 `16px`입니다. 
- .`btn-locale`의 `-webkit-appearance` 속성은 `none`입니다.
- `display` 속성은 `inline-block`입니다.
- 왼쪽 마진은 `-16px`입니다.
- 경계선이 없습니다.
- 글씨 크기는 `12px`입니다.
- 배경 색상은 투명합니다.
- 배경 이미지는 `url('https://image.flaticon.com/icons/svg/60/60995.svg')`입니다.
- 배경 이미지는 반복되지 않습니다.
- 배경 이미지의 위치는 x축/y축  `calc(100% - 14px) 50%`입니다.
- 배경 이미지의 크기는 `8px`입니다.

**Instructions**

1. .`btn-locale`의 스타일 적용하기.

   ```css
   .btn-locale {
     -webkit-appearance: none;
     display: inline-block;
     margin-left: -16px;
     padding: 8px 28px 8px 16px;
     border: 0;
     font-size: 12px;
     background-color: transparent;
     background-image: url('https://image.flaticon.com/icons/svg/60/60995.svg');
     background-repeat: no-repeat;
     background-position: calc(100% - 14px) 50%;
     background-size: 8px;
     outline: none;
   }
   ```



## .btn-locale:focus

지역 언어 버튼 `:focus` 스타일을 지정합니다.

- `.btn-locale:focus`의 배경 색상은 `#e0e0e0`입니다. 

**Instructions**

1. `.btn-locale:focus`의 스타일 적용하기.

   ```css
   .btn-locale:focus {
     background-color: #e0e0e0;
   }
   ```



## .list-footer

`<footer>` 안에 위치한 옵션 버튼들의 리스트 `<ul class="list-footer">`의 스타일을 지정합니다. 

- `.list-footer`의 `list-style` 속성은 `none`입니다. 
- `display` 속성은 `inline-block`입니다.
- 마진은 `0 -16px 0 0`입니다.
- 패딩은 `0`입니다.
- `float` 속성은 `right`입니다.

**Instructions**

1. `.list-footer`의 스타일 적용하기.

   ```css
   .list-footer {
     list-style: none;
     display: inline-block;
     margin: 0 -16px 0 0;
     padding: 0;
     float: right;
   }
   ```



## .list-footer li

`.list-footer` 안에 위치한 `li` 의 스타일을 지정합니다.

- `.list-footer li`의 `display` 속성은 `inline-block`입니다.

**Instructions**

1. `.list-footer li`의 스타일 적용하기.

   ```css
   .list-footer li {
     display: inline-block;
   }
   ```



## .btn-list-footer

`.btn-list-footer`의 스타일을 지정합니다.

- `.btn-list-footer`의 패딩은 `8px 16px`입니다.
- 모서리의 둥글기는 `4px`입니다.
- 글씨 색상은 `#757575`입니다.
- 글씨 크기는 `12px`입니다.

**Instructions**

1. `.btn-list-footer`의 스타일 적용하기.

   ```css
   .btn-list-footer {
     padding: 8px 16px;
     border-radius: 4px;
     color: #757575;
     font-size: 12px;
   }
   ```



## .btn-list-footer:focus

`.btn-list-footer:focus`의 스타일을 지정합니다.

- `.btn-list-footer:focus`의 배경 색상은 `#e0e0e0`입니다.

**Instructions**

1. `.btn-list-footer:focus`의 스타일 적용하기.

   ```css
   .btn-list-footer:focus {
     background-color: #e0e0e0;
   }
   
   ```





**NEXT STEP** 버튼을 클릭하세요.

