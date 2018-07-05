# 시작하기

`div`태그를 사용하여 컨테이너를 만들는 것으로 시작합니다.  

**Instructions**
1. `body`태그 안에 `div`태그를 추가하고, class 이름을 `container`로 적용하기. 
    ```html
    <div class="container"></div>
    ```



# 테이블 추가하기
`<div class="container">`안에 영수증을 만들기 위해서 `table`태그를 사용하겠습니다. 테이블에 추가해야하는 내용은 아래와 같습니다.
```html
|-------------------------|
|     PAYMENT RECEIPT     |
|-------------------------|
| Product |Awesome Editor |
|-------------------------|
| Date    |  Apr. 22 2018 |
|-------------------------|
| Order ID|     UDVD12548 |
|-------------------------|
| Price   |       $109.00 |
|-------------------------|
| Thank you for purchas...|
|-------------------------|
``` 
순서대로 따라해봅시다.


**Instructions**
1. `<div class="container">` 안에 `table`태그를 추가하고, `table-receipt`클래스 적용하기. 
    ```html
    <table class="table-receipt"></table>
    ```
1. `table`태그 안에 `thead`태그와 `tbody`태그 추가하기.  
    ```html
    <table class="table-receipt">
      <thead></thead>
      <tbody></tbody>
    </table> 
    ```
1. `thead`태그에 `tr`, `th`태그를 추가하고, `t-header` 클래스와 2칸을 모두 채우도록 `colspan="2"` attribute 추가하기.
    ```html
    <table class="table-receipt">
      <thead>
        <tr>
          <th colspan="2">PAYMENT RECEIPT</th>
        </tr>
      </thead>
      <tbody></tbody>
    </table> 
    ```
1. `tbody`태그에 `tr`을 사용해서 아래와 같이 4개의 행을 추가하기. 그리고 그 안에 2개씩의 `td`태그를 추가하고, 각각 `t-label`, `t-content` 클래스를 적용하기.
    ```html
    <table class="table-receipt">
      <thead>
        ...
      </thead>
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
      </tbody>
    </table> 
    ```

1. `tbody`태그에 1개의 행을 더 추가하고, `td-footer` 클래스를 적용한 `td`태그를 추가하기. 마지막 `td`태그는 2칸을 모두 채루도록 `colspan="2"` attribute 추가하기.
    ```html
    <table class="table-receipt">
      <thead>
        ...
      </thead>
      <tbody>
        ...
        <tr>
          <td class="td-footer" colspan="2">
            Thank you for purchasing form us.
          </td>
        </tr>
      </tbody>
    </table> 
    ```

이렇게 HTML로 뼈대를 구성했습니다. 다음 페이지에서 CSS를 사용해서 스타일링을 해봅시다.

**NEXT STEP** 버튼을 클릭하세요.



## TIPS! 
* 태이블 태그를 작성하는 것이 번거로워요.  
    > 맞아요. 저는 그래서 Google에 [html table generator][1]라고 검색을 합니다.     

[1]: https://www.google.co.kr/search?ei=ECs-W6KxK8fh-AbF-5HIBQ&q=html+table+generator&oq=html+table+generator&gs_l=psy-ab.3...290762.293424.0.295063.0.0.0.0.0.0.0.0..0.0....0...1c.1.64.psy-ab..0.0.0....0.v4501Hu84LM

