## 공통 스타일
이제, 제목 부분은 정리가 되었으니, 내용 부분을 정리해 봅시다. 영수증의 내용 부분에서 공통적으로 사용하는 `td`태그의 스타일을 정리해야 할 필요가 있습니다.
* `.table-receipt td`의 패딩은 세로축 `24px`, 가로축 `16px`입니다.
* 하단의 보더라인이 있습니다. 두깨는 `2px`, 스타일은 `solid`, 색상은 `#ECEFF1`입니다.

**Instructions**
1. `.table-receipt td`의 스타일 적용하기. 
    ```css
    .table-receipt td {
    	padding: 24px 16px;
    	border-bottom: 2px solid #ECEFF1;
    }
    ```
    
    

## 라벨
이제 라벨의 스타일을 정의해봅시다.
* `.table-receipt .t-label`의 글씨 크기는 `16px`입니다.
* 글씨의 두깨는 `700`입니다.
* 글씨의 컬러는 `#78909C`입니다. ([Google color][999]의 blue grey 400)

**Instructions**
1. `.table-receipt .t-label`의 스타일 적용하기. 
    ```css
    .table-receipt .t-label {
    	font-size: 16px;
    	font-weight: 700;
    	color: #78909C;
    }
    ```



## 값
값은 영수증에서 가장 중요한 부분입니다. 이 부분의 스타일을 정의해 봅시다.
* `.table-receipt .t-value`의 글씨 크기는 `24px`입니다.
* 글은 오른쪽 정렬입니다.

**Instructions**
1. `.table-receipt .t-label`의 스타일 적용하기. 
    ```css
    .table-receipt .t-value {
    	font-size: 24px;
    	text-align: right;
    }
    ```


    
## 푸터
마지막으로 푸터의 스타일입니다.
* `.table-receipt .t-footer`의 패딩은 `24px`입니다.
* 아랫면의 보더라인이 `0`입니다.
* 글씨 크기는 `16px`입니다.
* 글씨 컬러는 제목의 배경과 같은 `#2196F3`입니다.
* 글씨의 두깨는 `700`입니다.
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

[999]: https://material.io/design/color/#color-usage-palettes