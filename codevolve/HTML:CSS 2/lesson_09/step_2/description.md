# HTML
### Container

`container`를 추가하고 그 안에 `card-login-wrap`을 추가합니다. 2중으로 감싸져 있는 구조가 되겠네요. `card-login-wrap`안에 이후에 `card-login`과  `footer`를 배치하여 전체적인 구조를 만듭니다. 

**Instructions**

1. `<body>` 안에 `<div>`를 추가하고, `class="container"`적용하기.

   ```html
   <div class="container"></div>
   ```

2. `<div class="container">`  안에 `<div>` 를 추가하고 `class="card-login-wrap"` 적용하기.

   ```html
   <div class="card-login-wrap"></div>
   ```

### 

### Card-login-wrap

`card-login-wrap`은 `card-login`과 `footer`를 포함합니다. 로그인 폼 요소들은 `card-login`에 추가하고, 이외의 정보는 `footer`에 추가하겠습니다.

**Instructions**

1. `<div class="card-login-wrap">`  안에  `<div>` 를 추가하고 `class="card-login"` 적용하기.

   ```html
   <div class="card-login"></div>
   ```

2. `<div class="card-login">`  다음에  `<footer>`  추가하기.

   ```html
   <footer></footer>
   ```

### 

### Card-header

`card-header` 는 이 페이지를 설명하는 로고이미지, 헤드라인 요소들을 포함합니다.

**Instructions**

1. `<div class="card-login">`  안에 `<header>`를 추가하고, `class="card-header"`적용하기.

   ```html
   <header class="card-header"></header>
   ```

2. `<header class="card-herder">`  안에 `<img>`를 추가하고 `class="logo"`, `src="https://www.edigitalagency.com.au/wp-content/uploads/small-google-logo-png-transparent-background-210x70.png"`, `alt="Google Logo"`로 적용하기.

   ```html
   <img class="logo" src="https://www.edigitalagency.com.au/wp-content/uploads/small-google-logo-png-transparent-background-210x70.png" alt="Google Logo">
   ```

3. `<img>`다음에 `<h1>`를 추가하고 `class="headline"` 적용 및 내용 채우기.

   ```html
   <h1 class="headline">Sign in</h1>
   ```

4. `<h1 class="headline">` 다음에 `<h2>`를 추가하고 `class="sub-headline"` 적용 및 내용 채우기.

   ```html
   <h2 class="sub-headline">with your Google Account</h2>
   ```



### Card-form

`card-form`에는 검색어를 입력하는 인풋 요소가 들어갑니다. `autofocus` 속성을 사용하여 페이지가 로딩되면 자동으로 `input`에 `focus` 되도록 할 수 있습니다.

**Instructions**

1. `<header class="card-header">`  다음에 `<div>`를 추가하고, `class="card-form"`적용하기.

   ```html
   <div class="card-form"></div>
   ```

2. `<div class="card-form">`  안에 `<input>`을 추가하고 `type="text"`, `id="input-account-id`, `required="required"`,  `autofocus` 적용하기.

   ```html
   <input type="text" id="input-account-id" required="required" autofocus>
   ```

3. `<input>`다음에 `<label>`을 추가하고, `for="input-account-id"` 적용 및 내용채우기.

   ```html
   <label for="input-account-id">Email or phone</label>
   ```





**NEXT STEP** 버튼을 클릭하세요.