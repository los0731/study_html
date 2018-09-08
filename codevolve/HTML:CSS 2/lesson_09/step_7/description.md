## .card-form

이 다음에 우리가 해야할 스타일링은 많이 복잡해보일 수 있습니다. 직접 코드를 작성하기 전에 어떤 순서로 스타일을 적용하는지 알아봅시다. 

```html
1. card-form은 input과 label을 감싸고 있습니다.
2. card-form에 마진을 사용하여 간격을 조정합니다.
3. input의 스타일을 지정합니다.
4. label의 스타일을 지정합니다.
5. input이 focus(클릭해서 커서가 깜빡이는) 상태가 되면, 파란색 라인이 highlight되도록 합니다.
6. input의 focus와 valid(내용을 입력했을때) 상태가 되면, 그 다음에 오는 label의 크기가 작아지면서 input위로 이동하도록 합니다.
```

자, 이제 `input`과 `label`을 감싸고 있는 `<div class="card-form">`의 스타일을 지정합니다. 

- `.card-form`의 위 마진은 `64px`입니다.

**Instructions**

1. `.card-form`의 스타일 적용하기.

   ```css
   .card-form {
     margin-top: 64px;
   }
   ```



## .card-form input

`input`의 스타일을 지정합니다. 머테리얼 디자인의 `input` 스타일은 경계선 대신 밑줄을 사용하는 특징이 있습니다. 우리는 밑줄에 `box-shadow`를 사용할 것입니다.4

- `.card-form input`의 포지션 속성은 `relative`입니다.
- 패딩은 `8px 0`입니다.
- 경계선이 없습니다.
- 넓이는 `100%`입니다.
- 글씨 크기는 `16px`입니다.
- 배경 색상은 투명합니다.
- 그림자의 내부/x축/y축/퍼짐(blur)/크기/색상은 `inset 0 -1px rgba(0,0,0,.12)`입니다.
- `transition` 속성은 `.4s` 입니다.
- 아웃라인이 없습니다.

**Instructions**

1. `.card-form input`의 스타일 적용하기.

   ```css
   .card-form input {
     position: relative;
     padding: 8px 0;
     border: 0;
     width: 100%;
     font-size: 16px;
     background-color: transparent;
     box-shadow: inset 0 -1px rgba(0,0,0,.12);
     transition: .4s;
     outline: none;
   }
   ```



## .card-form label

`label`의 스타일을 지정합니다. 보통 `<input>`에는 `placeholder`라는 속성이 있습니다. `placeholder`는 `input`에 내용이 없을때 특정 글씨를 표시하는 속성으로 보통 `이메일을 입력하세요.`와 같은 내용을 추가해둡니다. 우리는 `label`이 `placeholder`의 역할도 같이 수행하도록 하기 위해서 `html`에서 `input`을 추가할때 `placeholder`를 추가하지 않았습니다. `label`을 추가할 때 이것을 고려하여 스타일링 합니다.

- `.card-form label`의 포지션 속성은 `absolute`입니다.
- `z-index`속성은  `-1`입니다.
- 글씨 크기는 `16px`입니다.
- 글씨 색상은 `#757575` 입니다.
- `transition` 속성은 `.4s` 입니다.
- `transform` 속성은 `translateY(-26px)` 입니다.

**Instructions**

1. `.card-form label`의 스타일 적용하기.

   ```css
   .card-form label {
     position: absolute;
     z-index: -1;
     font-size: 16px;
     color: #757575;
     transition: .4s;
     transform: translateY(-26px);
   }
   ```



## .card-form input:focus

어떤 태그나 클래스위에 붙는 `:?????` 는 특정 상태를 의미하는 선택자 입니다. `input:focus` 는 `input`에 마우스 커서가 선택되어있는 입력 중인 상태를 의미합니다. `.card-form` 안에 위치한 `input:focus`의 스타일을 지정합니다. 

- `.card-form input:focus`의 그림자의 내부/x축/y축/퍼짐(blur)/크기/색상은 `inset 0 2px 0 inset 0 -2px #1a73e8`입니다.

**Instructions**

1. `.card-form label`의 스타일 적용하기.

   ```css
   .card-form input:focus {
     box-shadow: inset 0 -2px #1a73e8;
   }
   ```



## .card-form input:focus + label, .card-form input:valid + label

`:valid` 선택자는 이 요소의 값이 있는 경우에 선택됩니다. input이 `:focus`이거나 `:valid` 일 경우, 그 다음에 오는 `label`의 스타일을 지정합니다. 

- `.card-form input:focus + label, .card-form input:valid + labels`의 글씨 색상은 `#1a73e8` 입니다. 
- 글씨 두개는 `bold`입니다.
- 글씨 크기는 `12px`입니다.
- `transform` 속성은 `translateY(-52px)`입니다.

**Instructions**

1. `.card-form input:focus + label, .card-form input:valid + labels`의 스타일 적용하기.

   ```css
   .card-form input:focus + label,
   .card-form input:valid + label {
     color: #1a73e8;
     font-weight: bold;
     font-size: 12px;
     transform: translateY(-52px);
   }
   ```





**NEXT STEP** 버튼을 클릭하세요.

