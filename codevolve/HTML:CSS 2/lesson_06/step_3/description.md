## 메뉴 목록
헤더 아래에 커피 메뉴 정보를 추가합니다. 메뉴 정보는 상품 이름과, 가격으로 이루어져있습니다. `table`태그를 활용합니다. 

**Instructions**
1. `header`태그 안에 `table`태그를 추가하고, 클래스를 `table-menu`로 적용하기. 
    ```html
    <header>...</header>
    <table class="table-menu"></table>
    ```
1. `table-menu`클래스 안에 `thead`태그를 추가하기
    ```html
    <table class="table-menu">
        <thead>
        </thead>
    </table>
    ```

1. `thead`태그 안에 `tr`태그를 추가하기
    ```html
    <table class="table-menu">
        <thead>
            <tr>
            </tr>
        </thead>
    </table>
    ```

1. `tr`태그 안에 4개의 `th`태그를 추가하고, 각 클래스의 이름 정하기
    ```html
    <table class="table-menu">
        <thead>
            <tr>
                <th class="t-title">Coffee & Espresso</th>
                <th class="t-size">Tall</th>
                <th class="t-size">Grande</th>
                <th class="t-size">Venti</th>
            </tr>
        </thead>
    </table>
    ```

1. `table-menu`클래스 안에 `tbody`태그를 추가하기
    ```html
    <table class="table-menu">
        <thead>
            <tr>
                <th class="t-title">Coffee & Espresso</th>
                <th class="t-size">Tall</th>
                <th class="t-size">Grande</th>
                <th class="t-size">Venti</th>
            </tr>
        </thead>
        <tbody>
        </tbody>
    </table>
    ```

1. `tbody`태그 안에 `tr`태그를 추가하기
    ```html
    <table class="table-menu">
        <thead>
            <tr>
                <th class="t-title">Coffee & Espresso</th>
                <th class="t-size">Tall</th>
                <th class="t-size">Grande</th>
                <th class="t-size">Venti</th>
            </tr>
        </thead>
        <tbody>
            <tr>
            </tr>
        </tbody>
    </table>
    ```

1. `tr`태그 안에 4개의 `td`태그를 추가하고, 각 클래스의 이름 정하기
    ```html
    <table class="table-menu">
        <thead>
            <tr>
                <th class="t-title">Coffee & Espresso</th>
                <th class="t-size">Tall</th>
                <th class="t-size">Grande</th>
                <th class="t-size">Venti</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="t-title">Cold Brew</td>
                <td class="t-size">4.5</td>
                <td class="t-size">5.0</td>
                <td class="t-size">5.5</td>
            </tr>
        </tbody>
    </table>
    ```

**NEXT STEP** 버튼을 클릭하세요.