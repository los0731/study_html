# HTML
Start by creating container using `<div>`.


**Instructions**
1. Add `<div>` within `<body>` and apply `class="container"`.

    ```html
    <body>
      <div class="container"></div> 
    </body>
    ```



### Add table
`<div class="container">`안에 영수증의 뼈대가 될 `<table>`를 추가합니다. 영수증에 들어가는 내용은 아래와 같습니다.
> * PAYMENT RECEIPT
> * Product: Awesome Editor
> * Date: Apr. 22 2018
> * Order ID: UDVD12548
> * Price: $109.00
> * Thank you for purchasing form us.


**Instructions**
1. Add `<table>` within `<div class="container">` and apply `class="table-receipt"`.

    ```html
    <div class="container">
      <table class="table-receipt"></table>
    </div>
    ```
1. `<table>` 안에 `<thead>`와 `<tbody>` 추가하기. 

    ```html
    <table class="table-receipt">
      <thead></thead>
      <tbody></tbody>
    </table> 
    ```
1. `<thead>` 부분 코드 작성하기.
    * `<thead>`에 `<tr>`를 사용해서 1개의 행을 만들기.
    * `<tr>`안에 `<th>`를 사용해서 1개의 열을 추가하고, `class="t-header"`, `colspan="2"` 적용하기
    * 내용 채우기.
    ```html
    <thead>
      <tr>
        <th class="t-header" colspan="2">PAYMENT RECEIPT</th>
      </tr>
    </thead> 
    ```
1. `<tbody>` 부분 코드 작성하기.
    * `<tbody>`에 `<tr>`를 사용해서 5개의 행을 추가하기. 
    * 1~4번째 행에는 `<td>`를 사용해서 2개의 열을 만들고, 각각 `class="t-label"`, `class="t-content"` 적용하기. 
    * 5번째 행에는 1개의 열을 만들고, `class="t-footer"`, `colspan="2"`로 적용하기. 
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



Click the **NEXT STEP** button.



# TIPS! 
* 태이블 태그를 작성하는 것이 번거로워요.  
    > 맞아요. 그래서 저는 [Table Generator][https://www.tablesgenerator.com/html_tables] 를 이용합니다.
* `colspan`이 무엇인가요? 
    > `<td>`, `<th>`의 속성 중 하나인 `colspan`은 각 셀을 가로로 병합합니다. 예를 들어 `colspan="2"`는 2칸을 병합하라는 의미입니다. 만약 세로로 병합하고 싶다면 `rowspan="2"`을 사용할 수 있습니다.
