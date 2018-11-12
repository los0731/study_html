## <td>
영수증의 내용 부분에서 공통적으로 사용하는 `td`의 스타일을 정리합시다.
* `.table-receipt td`의 패딩은 상/하 `24px`, 좌/우 `16px`입니다.
* 하단에 경계선이 있습니다. 보더의 넓이/스타일/색상은 `2px solid #ECEFF1`입니다.

**Instructions**
1. `.table-receipt td`의 스타일 적용하기. 
    ```css
    .table-receipt td {
    	padding: 24px 16px;
    	border-bottom: 2px solid #ECEFF1;
    }
    ```
    
    

## t-label
이제 라벨의 스타일을 정의합시다.
* `.table-receipt .t-label`의 글씨 크기는 `16px`입니다.
* 글씨 두께는 `700`입니다.
* 글씨의 색상은 `#78909C`입니다. [Google color](https://material.io/design/color/#color-usage-palettes)의 blue grey 400과 같습니다.

**Instructions**
1. `.table-receipt .t-label`의 스타일 적용하기. 
    ```css
    .table-receipt .t-label {
    	font-size: 16px;
    	font-weight: 700;
    	color: #78909C;
    }
    ```



## .t-price
값은 영수증에서 가장 중요한 부분입니다. 이 부분의 스타일을 정의합시다.
* `.table-receipt .t-price`의 글씨 크기는 `24px`입니다.
* 글은 오른쪽 정렬입니다.

**Instructions**
1. `.table-receipt .t-price`의 스타일 적용하기. 
    ```css
    .table-receipt .t-price {
    	font-size: 24px;
    	text-align: right;
    }
    ```


​    
## .t-footer
마지막으로 푸터의 스타일입니다.
* `.table-receipt .t-footer`의 패딩은 `24px`입니다.
* 하단의 경계선은 `0`입니다.
* 글씨 크기는 `16px`입니다.
* 글씨 색상은 제목의 배경과 같은 `#2196F3`입니다.
* 글씨 두께는 `700`입니다.
* 글은 가운데 정렬입니다.

**Instructions**
1. `.table-receipt .t-footer`의 스타일 적용하기. 
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
    
    

모두 완료했다면 **NEXT STEP** 버튼을 클릭하세요.  