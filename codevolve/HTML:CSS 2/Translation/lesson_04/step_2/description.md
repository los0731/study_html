# HTML
Start by creating container using `<div>`.


**Instructions**
1. Add `<div>` within `<body>` and apply `class="container"`.

    ```html
    <body>
      <div class="container"></div> 
    </body>
    ```



### .table-receipt
In the `<div class="container">` we add `<table>`, which will be the framework for the receipt. The following items will be part of the receipt. 
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

So this is how we have constructed the page framework using `HTML`. On the next page let's use `CSS` to do some styling. 



Click the **NEXT STEP** button.



## TIPS! 
* It's really tedious to write a table tag.

    > That's true. That's why I use  [Table Generator][https://www.tablesgenerator.com/html_tables]. 
* What's `colspan`?

    > Among the properties of `<td>`, `<th>`, there is one called `colspan`, which merges each cell horizontally. For example, `colspan="2"` means two cells will be merged. When you want to merge two cells vertically, you can use `rowspan="2"`. 
