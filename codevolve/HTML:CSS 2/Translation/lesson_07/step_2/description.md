# HTML
`<div>`를 사용하여 카드를 만듭니다. 그 안에  `<a>`를 사용해서 링크도 추가합시다. 본격적인 카드의 요소는 `<a>` 안에 들어갑니다. 카드에 들어갈 요소들은 다음과 같습니다.
> - 히어로 이미지 (카드를 설명하는 이미지)
> - 제목
> - 본문
> - 구분선
> - 컨텐츠 타입
> - hover 했을 때 등장하는 `VIEW MORE`텍스트

**Instructions**
1. Add `<div>` within `<body>` and apply `class="card"`.
    ```html
    <body>
      <div class="card"></div>
    </body>
    ```
1. Add `<a>` within `<div class="card">` and apply `href="https://facebook.design/videos/designing-at-facebook"`.
    ```html
    <div class="card">
      <a href="https://facebook.design/videos/designing-at-facebook"></a>
    </div>
    ```



### card-hero 
히어로 이미지는 보통 영역 상단에 풀 스크린으로 배치된 큰 이미지입니다. 히어로 이미지는 해당 영역의 큰 분위기를 표현하고, 사용자가 글을 읽기 전에 호기심을 자극하거나, 대략적인 의미를 전달하는 기능을 수행합니다. 이 요소는 곧 CSS에서 다룰태니, 지금은 빈 태그와 클래스만 남겨둡니니다.

**Instructions**
1. Add `<div>` within `<a>` and apply `class="card-hero"`.
    ```html
    <a href="https://facebook.design/videos/designing-at-facebook">
      <div class="card-hero"></div>
    </a>
    ```



### card-block
카드 히어로 이미지를 제외하고, 나머지 요소들(타이틀, 설명, 구분선, 태그 등)은 하나로 묶어 줄겁니다. 이 요소들을 `card-block`이라고 합시다.

**Instructions**
1. Add `<div>` below `<div class="card-hero">` and apply `class="card-block"`
    ```html
    <div class="card-hero"></div>
    <div class="card-block"></div> 
    ```

1. `<div class="card-block">`안에 `<h2>`를 추가하고, `class="card-title"` 적용 및 내용 채우기.

    ```html
    <div class="card-block">
      <h2 class="card-title">Designing at Facebook</h2> 
    </div>  
    ```

1. `<h2 class="card-title>`아래에 `<p>`를 추가하고, `class="card-description"`으로 적용 및 내용 채우기. 
    ```html
    <p class="card-description">Get a sneak peek at the design process at Facebook from product designers Cat Audi and George Kedenburg III.</p>       
    ```

1. Add `<hr>` below `<p class="card-description">` and apply `class="card-hrclass="`.
    ```html
    <hr class="card-hr">       
    ```

1. `<hr class="card-hr">`아래에 `<h6>`를 2개 추가하고, 각각 `class="card-type"`, `class="card-tag"` 적용 및 내용 채우기. 
    ```html
    <h6 class="card-type">VIDEO</h6>
    <h6 class="card-tag">VIEW MORE</h6>
    ```


Click the **NEXT STEP** button.



# TIPS!

- `<div class="card-hero">`는 왜 `<img>`가 아니라 `<div>`를 사용하나요?

  > 대다수의 히어로 이미지는 `<img>`가 아닌 `<div>`태그에 `background`를 프로퍼티를 사용해서 표현합니다. 이유는 다음과 같습니다. 
  >
  > - 보통 리스트에서 표현하는 히어로 이미지는 원래 페이지의 이미지 소스를 가져오는 경우가 많기 때문에 이미지의 비율이 다양합니다. `ìmg`태그는 비율이 고정되어, 화면 안에 강제로 표시하면 이미지가 좁아지거나 늘어나게 됩니다.
  > - 다양한 디바이스 (데스크탑, 모바일, 테블릿)의 넓이에 따라 영역의 비율이 계속 바뀔 수 있기 때문에, `<img>`로 표현하는데에는 한계가 있습니다. 

