### 메뉴 목록
헤더 아래에 커피 메뉴 정보를 추가합니다. 메뉴 정보는 상품 이름과, 가격으로 이루어져있습니다. `<table>`를 활용합니다. 

**Instructions**
1. `<header>` 안에 `<table>`를 추가하고, `class="table-menu"`로 적용하기. 
    ```html
    <header>...</header>
    <table class="table-menu"></table>
    ```

1. `<thead>` 아래에 `<tbody>`를 추가하기
    ```html
    <table class="table-menu">
        <tbody>
        </tbody>
    </table>
    ```

1. 메뉴가 7가지이므로, `<tbody>` 안에 7개의 `<tr>` 추가하기
    ```html
    <table class="table-menu">
        <tbody>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
            <tr></tr>
        </tbody>
    </table>
    ```

1. `<tr>` 안에 각각 2개의 `<td>`를 추가하고, 각 클래스와 내용 추가하기.
    ```html
    <table class="table-menu">
        <tbody>
            <tr>
              <td class="t-title">Espresso</td>
              <td class="t-price">2.75</td>
            </tr>
            <tr>
              <td class="t-title">Macchiato</td>
              <td class="t-price">3.25</td>
            </tr>
            <tr>
              <td class="t-title">Cappuccino</td>
              <td class="t-price">3.5</td>
            </tr>
            <tr>
              <td class="t-title">Caffé Latte</td>
              <td class="t-price">4</td>
            </tr>
            <tr>
              <td class="t-title">Caffé Mocha</td>
              <td class="t-price">5</td>
            </tr>
            <tr>
              <td class="t-title">Drip Blend</td>
              <td class="t-price">2.75</td>
            </tr>
            <tr>
              <td class="t-title">Cold Brewed Iced</td>
              <td class="t-price">4</td>
            </tr>
        </tbody>
    </table>
    ```

**NEXT STEP** 버튼을 클릭하세요.