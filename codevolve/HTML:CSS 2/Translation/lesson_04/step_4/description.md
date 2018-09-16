### 공통 스타일
영수증의 내용 부분에서 공통적으로 사용하는 `td`의 스타일을 정리합시다.
* `.table-receipt td`의 패딩은 상/하 `24px`, 좌/우 `16px`입니다.
* 하단에 경계선이 있습니다. 보더의 넓이/스타일/색상은 `2px solid #ECEFF1`입니다.

**Instructions**
1. Apply style to `.table-receipt td`.
    ```css
    .table-receipt td {
    	padding: 24px 16px;
    	border-bottom: 2px solid #ECEFF1;
    }
    ```


### label
이제 라벨의 스타일을 정의합시다.
* The font size of `.table-receipt .t-label` is `16px`.
* 글씨 두께는 `700`입니다.
* The font color is `#78909C`. [Google color][999]의 blue grey 400과 같습니다.

**Instructions**
1. Apply style to `.table-receipt .t-label`.
    ```css
    .table-receipt .t-label {
    	font-size: 16px;
    	font-weight: 700;
    	color: #78909C;
    }
    ```



### Price
값은 영수증에서 가장 중요한 부분입니다. 이 부분의 스타일을 정의합시다.
* `.table-receipt .t-value`의 글씨 크기는 `24px`입니다.
* The letters are centered.

**Instructions**
1. Apply style to `.table-receipt .t-label`.
    ```css
    .table-receipt .t-value {
    	font-size: 24px;
    	text-align: right;
    }
    ```


​    
### footer
마지막으로 푸터의 스타일입니다.
* `.table-receipt .t-footer`의 패딩은 `24px`입니다.
* 하단의 경계선은 `0`입니다.
* The font size is `16px`.
* The font color is `#2196F3`. (same as background color.)
* 글씨 두께는 `700`입니다.
* The letters are centered.

**Instructions**
1. Apply style to `.table-receipt .t-footer`.
    ```css
    .table-receipt .t-footer {
    	padding: 24px;
    	border-bottom: 0;
    	font-size: 16px;
    	color: #2196F3;
    	font-weight: 700;
    	text-align: center;
    }
    ```


Click the **NEXT STEP** button. 

[999]: https://material.io/design/color/#color-usage-palettes