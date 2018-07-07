# 시작하기
`div`태그를 사용하여 컨테이너를 만들는 것으로 시작합니다.  

**Instructions**
1. `body`태그 안에 `div`태그를 추가하고, class 이름을 `container`로 적용하기. 
    ```html
    <body>
      <div class="container"></div> 
    </body>
    ```



# 테이블 추가하기
`<div class="container">`안에 영수증의 뼈대가 될 `table`태그*를 추가합니다. 영수증에 들어가는 내용은 아래와 같습니다.
> * PAYMENT RECEIPT
> * Product: Awesome Editor
> * Date: Apr. 22 2018
> * Order ID: UDVD12548
> * Price: $109.00
> * Thank you for purchasing form us.


**Instructions**
1. `<div class="container">` 안에 `table`태그를 추가하고, `table-receipt`클래스 적용하기. 
    ```html
    <div class="container">
      <table class="table-receipt"></table>
    </div>
    ```
1. `table`태그 안에 `thead`태그와 `tbody`태그 추가하기.  
    ```html
    <table class="table-receipt">
      <thead></thead>
      <tbody></tbody>
    </table> 
    ```
1. `thead`태그 부분 코드 작성하기.
    * `thead`태그에 `tr`태그를 사용해서 1개의 행을 만들기.
    * `tr`태그안에 `th`태그를 사용해서 1개의 열을 추가하고, 클래스를 `t-header`, colspan을 `2`*로 적용하기
    * 내용 채우기.
    ```html
    <thead>
      <tr>
        <th class="t-header" colspan="2">PAYMENT RECEIPT</th>
      </tr>
    </thead> 
    ```
1. `tbody`태그 부분 코드 작성하기.
    * `tbody`태그에 `tr`태그를 사용해서 5개의 행을 추가하기. 
    * 1~4번째 행에는 `td`태그를 사용해서 2개의 열을 만들고, 클레스를 각각 `t-label`, `t-content`으로 적용하기. 
    * 5번째 행에는 1개의 열을 만들고, 클래스를 `t-footer`, colspan을 `2`로 적용하기. 
    * 각 항목에 내용 채우기. 
    ```html
    <tbody>
      <tr>
        <td class="t-label">Product</td>
        <td class="t-content">Awesome Editor</td>
      </tr>
      <tr>
        <td class="t-label">Date</td>
        <td class="t-content">Apr. 22 2018</td>
      </tr>
      <tr>
        <td class="t-label">Order ID</td>
       <td class="t-content">UDVD12548</td>
      </tr>
      <tr>
        <td class="t-label">Price</td>
        <td class="t-content">$109.00</td>
      </tr>
      <tr>
        <td class="t-footer" colspan="2">
          Thank you for purchasing form us.
        </td>
      </tr>
    </tbody> 
    ```

이렇게 HTML로 뼈대를 구성했습니다. 다음 페이지에서 CSS를 사용해서 스타일링을 해봅시다.



**NEXT STEP** 버튼을 클릭하세요.



## TIPS! 
* 태이블 태그를 작성하는 것이 번거로워요.  
    > 맞아요. 저는 그래서 Google에 [html table generator][1]라고 검색을 합니다.     
* `colspan`이 무엇인가요? 
    > `td`, `th`태그의 attribute중 하나인 `colspan`은 각 셀을 가로로 병합합니다. 예를들어 `colspan="2"`는 2칸을 병합하라는 의미입니다. 만약 세로로 병합하고 싶다면 `rowspan="2"`을 사용할 수 있습니다.

[1]: https://www.google.co.kr/search?ei=ECs-W6KxK8fh-AbF-5HIBQ&amp;amp;amp;q=html+table+generator&amp;amp;amp;oq=html+table+generator&amp;amp;amp;gs_l=psy-ab.3...290762.293424.0.295063.0.0.0.0.0.0.0.0..0.0....0...1c.1.64.psy-ab..0.0.0....0.v4501Hu84LM

