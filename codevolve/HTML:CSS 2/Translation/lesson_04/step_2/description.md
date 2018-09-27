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
1. Add `<thead>` and `<tbody>`in the `<table>`

    ```html
    <table class="table-receipt">
      <thead></thead>
      <tbody></tbody>
    </table> 
    ```
1. Write code for the `<thead>` part
    * Use `<tr>`in `<thead>` to create 1 row.
    * Use `<th>` in `<tr>` to add 1 column and apply `class="t-header"`, `colspan="2"`
    * Fill in content
    ```html
    <thead>
      <tr>
        <th class="t-header" colspan="2">PAYMENT RECEIPT</th>
      </tr>
    </thead> 
    ```
1. Write code for the `<tbody>` part
    * Use `<tr>`in `<tbody>` to create 5 rows.
    * For rows 1~4 use `<tr>` to create 2 columns and apply `class="t-label"`, `class="t-content"` to each.
    * For the 5th row create 1 column and apply `class="t-footer"`, `colspan="2"`.
    * Fill each item with content
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
