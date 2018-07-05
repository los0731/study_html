## 스타일 적용하기

**Instructions**
1. `body`배경색은 `#ECEFF1`입니다.
1. `.container`의 스타일
    * 최대 넓이는 `400px`입니다.
    * 배경색은 `white`입니다.
    * 위/아래 margin은 `80px`이고, 좌/우 margin은 `auto`입니다.
1. `.table-receipt`의 스타일
    * 넓이는 `100%`입니다. 
    * `border-collapse`속성의 값은 `collapse`입니다. 
        > `border-collapse: collapse;`는 테이블 또는 셀의 경계선을 겹쳐줌으로서 깔끔하게 선이 표시되도록 합니다. 
    * `box-shadow`속성의 값은 `40px 40px 80px -8px #B0BEC5`입니다.
        > 저는 그림자의 컬러에 black을 사용하지 않습니다. [Google Colors](https://material.io/design/color/#tools-for-picking-colors)에서 제공하는 `Blue grey 200`은 흰 배경일 때의 그림자 컬러로 적당합니다.
1. `.t-header`의 스타일
    * `padding`은 `24px`입니다.
    * 글씨 컬러는 흰색입니다.
    * 글씨 크기는 `24px`입니다.
    * 배경 컬러는 `#2196F3`입니다.
1. `td`의 스타일
    * 위/아래 `padding`은 `24px`이고, 좌/우는 `16px`입니다.
    * `border-bottom`속성의 값은 `2px solid #ECEFF1;`입니다.
1. `.t-label`의 스타일
    * 글씨의 크기는 `16px`입니다.
    * 글씨의 두깨는 `700`입니다.
    * 글씨의 컬러는 `#78909C`입니다.
1. `.t-content`의 스타일
    * 글씨의 크기는 `24px`입니다.
    * `text-align`속성의 값은 `right`입니다.
1. `.td-footer`의 스타일
    * `padding`은 `24px`입니다.
    * `border-bottom`속성의 값은 `0`입니다. 
    * 글씨의 크기는 `16px`입니다.
    * 글씨의 컬러는 `#2196F3`입니다.
    * 글씨의 두깨는 `700`입니다.
    * `text-align`속성의 값은 `center`입니다.

모두 완료했다면 **NEXT STEP** 버튼을 클릭하세요.
 

## HELP 
만약 잘 모르겠다면 아래에 있는 완성된 코드를 보고 따라해보세요. 

**Code**
```css
body {
  margin: 0;
	background-color: #ECEFF1;
}

.container {
	max-width: 400px;
	background-color: white;
	margin: 80px auto;
}

.table-receipt {
	width: 100%;
	border-collapse: collapse;
	box-shadow: 40px 40px 80px -8px #B0BEC5;
}

.t-header {
	padding: 24px;
	width: 100%;
	color: white;
	font-size: 24px;
	background-color: #2196F3;
}

td {
	padding: 24px 16px 24px 16px;
	border-bottom: 2px solid #ECEFF1;
}

.t-label {
	font-size: 16px;
	font-weight: 700;
	color: #78909C;
}

.t-content {
	font-size: 24px;
	text-align: right;
}

.td-footer {
	font-size: 16px;
	color: #2196F3;
	font-weight: 700;
	text-align: center;
	padding: 24px;
	border-bottom: 0;
}
``` 