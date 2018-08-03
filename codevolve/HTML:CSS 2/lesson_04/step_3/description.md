# CSS
### 배경 
영수증이 배경에서 조금 떠있는 스타일을 연출하기 위해서는 배경이 흰색보다 약간 회색에 가깝도록 해봅시다. 배경 색상은 [Google colors][999]의 Blue Grey 50를 사용합니다. 
* `body`의 배경 색상은 `#ECEFF1`입니다.

**Instructions**
1. `body`의 스타일 적용하기. 
    ```css
    body {
      background-color: #ECEFF1;
    }
    ```



### 컨테이너
컨테이너는 영수증을 일정 넓이로 고정해주고, 화면의 가운데 있도록 해줍니다.  
* `.container`의 마진은 상/하 `80px`, 좌/우 `auto`입니다.
* 최대 넓이는 `400px`입니다.

**Instructions**
1. `.container`의 스타일 적용하기. 
    ```css
    .container {
      margin: 80px auto;
      max-width: 400px;
    }
    ```



### 영수증 
컨테이너 안에 있는 영수증의 스타일을 정의해봅시다. 
* `.table-receipt`의 보더라인들이 겹쳐서 표시되도록 합니다. 다르게 말하면 `border-collapse: collapse;`입니다.*
* 넓이는 `100%`입니다.
* 배경 색상은 `white`입니다.
* 그림자가 있습니다. 그림자의 x축/y축/퍼짐(blur)/크기/색상은 `40px 40px 80px -8px #B0BEC5`입니다.

**Instructions**
1. `.table-receipt`의 스타일 적용하기. 
    ```css
    .table-receipt {
    	border-collapse: collapse;
    	width: 100%;
    	background-color: white;
    	box-shadow: 40px 40px 80px -8px #B0BEC5;
    }
    ```



### 제목 
영수증의 제목 부분인 `th`의 스타일을 정의합시다. 이 레슨에서 선택자를 입력할 때는 `.table-receipt th`라고 하겠습니다.*
* `.table-receipt th`패딩은 `24px`입니다.
* 넓이는 `100%`입니다.
* 글씨 색상은 `white`입니다.
* 배경 색상은 `#2196F3`입니다. 이 색상은 [Google colors][999]의 Blue 500과 같습니다.

**Instructions**
1. `.table-receipt th`의 스타일 적용하기. 
    ```css
    .table-receipt th {
    	padding: 24px;
    	width: 100%;
    	color: white;
    	font-size: 24px;
    	background-color: #2196F3;
    }
    ```
    
    

모두 완료했다면 **NEXT STEP** 버튼을 클릭하세요. 다음 스텝에서 영수증의 나머지 부분의 스타일을 정의해봅시다. 

 


# TIPS! 
* CSS 선택자를 생략하는 이유.
    > 만약 위의 경우에서 아주 정확하게 선택자를 입력한다면 아래와 같이 작성할 수 있습니다.
    > ```css
    > table.table-receipt thead tr th {...}
    > ```
    > 하지만 클래스를 활용해서 선택 범위가 정확하다고 생각된다면, 생략할 수 있는 코드는 최대한 생략하고 짧게 작성하는 것도 좋은 방법입니다.
    > ```css
    > .table-receipt th {...}
    > ```
    > 간결하게 코드를 작성하면 좋은 이유는 짧은 시간에 코드를 이해하는데 도움이 되기 때문입니다. 특히 다른 사람이 내 코드를 봐야한다면요.
* `border-collapse`는 뭔가요?
    > [border-collapse][2]는 테이블 cell 보더라인의 겹침 속성을 설정하는 CSS 프로퍼티입니다. 값은 collapse, separate가 있습니다. `collapse`: 테이블 cell의 테두리를 통합합니다. 즉 겹쳐서 한줄로 보이도록 합니다. `separate`: 기본설정으로 테이블 cell의 테두리를 분리해서 두줄로 보이게됩니다.

[1]: https://www.w3schools.com/cssref/css_selectors.asp
[2]: https://www.w3schools.com/CSSref/tryit.asp?filename=trycss_border-collapse
[999]: https://material.io/design/color/#color-usage-palettes