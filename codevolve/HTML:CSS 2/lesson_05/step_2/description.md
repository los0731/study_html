# 시작하기
`div`태그를 사용하여 메뉴판의 틀을 만드는 것으로 시작합니다.
메뉴판은 메뉴판의 바탕인 `menu-wrap`, 메뉴판의 내용을 채울 `menu`,
가게의 이름을 적을 `header`, 메뉴를 적을 `table-menu`로 이루어집니다. 

**Instructions**
1. `body`태그 안에 `div`태그를 추가하고, class 이름을 `menu-wrap`로 적용하기. 
    ```html
    <div class="menu-wrap"></div>
    ```
1. `menu-wrap`클래스 안에 `div`태그를 추가하고, class 이름을 `menu`로 적용하기. 
    ```html
    <div class="menu-wrap">
        <div class="menu">
        </div>
    </div>
    ```
1. `menu`클래스 안에 `div`태그를 추가하고, class 이름을 `header`로 적용하기. 
    ```html
    <div class="menu-wrap">
        <div class="menu">
            <div class="header">
            </div>
        </div>
    </div>
    ```
1. `menu`클래스 안에 `table`태그를 추가하고, class 이름을 `table-menu`로 적용하기. 
    ```html
    <div class="menu-wrap">
        <div class="menu">
            <div class="header">
            </div>
            <table class="table-menu">
            </table>
        </div>
    </div>
    ```

## header 내용 채우기
`<div class="header">` 안에 카페의 이름과 로고들을 추가합니다. 
** 배웠던 것 처럼 이미지의 출처를 남겨주세요.**

**Instructions**

1. 이미지 다음 라인에 `h4`태그를 사용해서 카페의 이름 추가하기.  
    ```html
    <h4>·P·L·A·S·T·I·C·P·I·N·K·</h4> 
    ```

1. `h4`태그의 다음 라인에 로고 이미지를 추가하고, src attribute를 `https://cdn2.iconfinder.com/data/icons/flat-line-valentine-1/1010/coffee-heart-256.png`, alt attribute를 `logo`, width attribute를 `128px`로 적용하기.
    ```html
    <img src="https://cdn2.iconfinder.com/data/icons/flat-line-valentine-1/1010/coffee-heart-256.png" alt="logo" width="128">
    ```
1. 두 번째 로고 이미지를 추가하고, src attribute를 `https://cdn2.iconfinder.com/data/icons/flat-line-valentine-1/1010/pot-love-pills-256.png`, alt attribute를 `logo`, width attribute를 `128px`로 적용하기.
    ```html
    <img src="https://cdn2.iconfinder.com/data/icons/flat-line-valentine-1/1010/pot-love-pills-256.png" alt="logo" width="128">
    ```
1. 세 번째 로고 이미지를 추가하고, src attribute를 `https://cdn2.iconfinder.com/data/icons/flat-line-valentine-1/1010/cup-coffee-hearts-256.png`, alt attribute를 `logo`, width attribute를 `128px`로 적용하기.
    ```html
    <img src="https://cdn2.iconfinder.com/data/icons/flat-line-valentine-1/1010/cup-coffee-hearts-256.png" alt="logo" width="128">
    ```
1. 네 번째 로고 이미지를 추가하고, src attribute를 `https://cdn2.iconfinder.com/data/icons/flat-line-valentine-1/1010/heart-bulb-256.png`, alt attribute를 `logo`, width attribute를 `128px`로 적용하기.
    ```html
    <img src="https://cdn2.iconfinder.com/data/icons/flat-line-valentine-1/1010/heart-bulb-256.png" alt="logo" width="128">
    ```

## table 내용 채우기
`<div class="table-menu">` 안에 커피의 종류와 가격을 추가하여 메뉴판의 내용을 채웁니다. 


**Instructions**

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