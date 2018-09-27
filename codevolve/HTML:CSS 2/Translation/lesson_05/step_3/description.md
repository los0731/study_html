### .table-menu
Below the header we add the menu information. The menu information is composed of the dish/beverage name and a price. We use  `<table>` to do this. 

**Instructions**
1. Add `<table>` within `<header>` and apply `class="table-menu"`.
    ```html
    <header>...</header>
    <table class="table-menu"></table>
    ```

1. Add `<tbody>` below `<thead>`.
    ```html
    <table class="table-menu">
        <tbody>
        </tbody>
    </table>
    ```

1. Since the menu has 7 elements, add 7 `<tr>` inside `<tbody>`.
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

1. Add two '<td>' within `<tr>`, and add each class and its contents.
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

Click the **NEXT STEP** button.