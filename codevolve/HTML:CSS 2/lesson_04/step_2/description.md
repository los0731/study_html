## HTML로 구조잡기
순서대로 따라해 보면서 페이지를 완성해 봅시다.  

**Instructions**
1. `<body>` 안에 `<div>`를 추가하고, `container`라는 class를 적용하세요.
1. 추가한 `<div>`태그 안에 `<table>`를 추가하고, `table-receipt`라는 class를 적용하세요.
1. `<table>`안에 `<thead>`를 추가하세요.
1. `<thead>`안에 `<tr>`를 추가하세요. `<tr>`안에 `<th>`를 추가하고, 내용:"PAYMENT RECEIPT"을 추가하세요. 그리고 이 `<th>`에 `colspan="2"`속성을 추가하세요.
1. `<thead>`아래 `<tbody>`를 추가하세요.
1. `<thead>`안에 `<tr>`를 추가하세요. `<tr>`안에 `<td>`를 2번 추가하고, 첫번째 `<td>`에는 `td-title`class와 내용:"Product"를, 두번째 `<td>`에는 `td-content`class와 내용:"Awesome Editor"를 추가하세요.
1. 같은 방식으로 `<tr>`다음에 새로운 `<tr>`을 추가하세요. `<tr>`안에 `<td>`를 2번 추가하고, 첫번째 `<td>`에는 `td-title`class와 내용:"Date"를, 두번째 `<td>`에는 `td-content`class와 내용:"Apr. 22 2018"를 추가하세요.
1. 새로운 `<tr>`을 추가하세요. `<tr>`안에 `<td>`를 2번 추가하고, 첫번째 `<td>`에는 `td-title`class와 내용:"Order ID"를, 두번째 `<td>`에는 `td-content`class와 내용:"UDVD12548"를 추가하세요.
1. 새로운 `<tr>`을 추가하세요. `<tr>`안에 `<td>`를 2번 추가하고, 첫번째 `<td>`에는 `td-title`class와 내용:"Price"를, 두번째 `<td>`에는 `td-content`class와 내용:"109.00"를 추가하세요.
1. 마지막입니다. 새로운 `<tr>`을 추가하세요. `<tr>`안에 `<td>`를 1번 추가하고, `td-footer`class를 적용합니다. 그리고 이 `<td>`에 `colspan="2"`속성을 추가하세요.

**NEXT STEP** 버튼을 클릭하세요.



## HELP
`<table>`은 안에 들어가는 태그들이 다양해서 익숙하지 않을 수 있습니다. 만약 뜻대로 되지 않는다면 아래의 완성된 코드를 보는것이 큰 도움이 될거에요.

**Code**
```html
<div class="container">
  <table class="table-receipt">
    <thead>
    <tr>
      <th class="th-header" colspan="2">PAYMENT RECEIPT</th>
    </tr>
    </thead>

    <tbody>
    <tr>
      <td class="td-title">Product</td>
      <td class="td-content">Awesome Editor</td>
    </tr>
    <tr>
      <td class="td-title">Date</td>
      <td class="td-content">Apr. 22 2018</td>
    </tr>
    <tr>
      <td class="td-title">Order ID</td>
      <td class="td-content">UDVD12548</td>
    </tr>
    <tr>
      <td class="td-title">Price</td>
      <td class="td-content">$109.00</td>
    </tr>
    <tr>
      <td class="td-footer" colspan="2">Thank you for purchasing form us.</td>
    </tr>
    </tbody>
  </table>
</div>
``` 
