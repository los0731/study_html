### .name
`<h2>`태그를 사용하는 이름은 위에있는 이미지와 조금 떨어져 있어야하고, 가장 중요한 정보이기 때문에 글씨를 두껍게 해야합니다. 그리고 이 태그의 색상은 [Google colors][1]의 Green 500을 선택합니다.

* `h2`의 위 마진은 `8px`입니다.
* 글씨 두께는 `900`입니다.  
* The font color is `#4CAF50`.

**Instructions**
1. Apply style to `.name`.
    ```css
    .name {
    	margin-top: 8px;
    	font-weight: 900;
    	color: #4CAF50;
    }
    ```



### .information

직업, 전화번호, 이메일의 정보는 순서가 없는 리스트 태그를 사용해서 작성했습니다. 여기서 더 자연스럽게 보이기 위해서 불릿 포인트를 제거해야합니다. 그리고 리스트 태그는 기본 옵션으로 마진과 패딩이 들어가 있습니다. 따라서 별도의 마진과 패딩 값을 지정해서 리스트 태그의 간격을 원하는 상태로 조정해 주어야 합니다.  

* 리스트의 불렛 마크가 없습니다.
* 마진은 상/우/하/좌 `16px 0 0 0` 입니다.  
* Padding is `0`.
* 글씨 크기는 `16px`입니다.
* 행간은 `24px`입니다.
* 글씨 색상은 `#455A64`입니다.


**Instructions**
1. Apply style to `.information`. 
    ```css
    .information {
        list-style: none;
        margin: 16px 0 0 0;
        padding: 0;
        font-size: 16px;
        line-height: 24px;
        color: #455A64;
    }
    ```



Click the **NEXT STEP** button.



## TIPS! 
* `font-weight`의 수치들은 어떤게 있나요?

    > font-weight은 normal, bold를 사용할 수도 있지만, 숫자를 활용할 수도 있습니다. 100부터 900의 값을 선택할 수 있고, 900은 어떤 경우든 가장 두껍게 표현합니다.   


[1]: https://material.io/design/color/#color-usage-palettes

