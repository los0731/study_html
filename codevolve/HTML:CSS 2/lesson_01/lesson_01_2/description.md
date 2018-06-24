## HTML로 시작하기
`div`태그에 대해서 아시나요? `div`태그는 분할 또는 섹션을 정의할때 사용하는 비어있는 태그 입니다. 기본속성으로 `display: block;`만 가지고 있습니다. 
우리는 이렇게 비어있는 태그에 클레스를 적용하여 CSS로 스타일을 지정하는 컨테이너로 사용하는 경우가 많습니다.

순서대로 따라해 보면서 페이지를 완성해 봅시다.

**Instructions**
1. `<body>`태그 안에 `<div>`태그를 추가하고, `container`라는 클래스를 적용하세요.
1. 추가한 `<div>`태그 안에 `img_google_play.png` 이미지를 추가하고, `img-logo`라는 클레스를 적용하세요. 그리고 alt-text:`Google Play`를 추가하세요
1. 이미지 다음에 `h1`태그를 사용해서 헤드라인:`Google Play Terms of Service`을 추가하세요. 
1. 헤드라인 다음에 `h6`태그를 사용해서 게시일:`February 5, 2018`을 추가하세요.
1. 게시일 다음에 `h2`태그를 사용해서 첫번째 소제목을 추가하세요.
    ```
    1. Introduction
    ```
1. 그 다음줄에, `p`태그를 활용해서 첫번째 소재목에 대한 내용을 추가하세요.
    ```
    "Applicable Terms. Thanks for using Google Play. Google Play is a service provided by Google LLC ("Google", "we" or "us"), located at 1600 Amphitheatre Parkway, Mountain View, California 94043, USA. Your use of Google Play and the apps (including Android Instant Apps), games, music, movies, books, magazines, or other digital content or services (referred to as "Content") available through it is subject to these Google Play Terms of Service and the Google Terms of Service ("Google ToS") ( together referred to as the "Terms"). Google Play is a "Service" as described in the Google ToS. If there is any conflict between the Google Play Terms of Service and the Google ToS, the Google Play Terms of Service shall prevail."
    ```
1. 그 다음줄에, `h2`태그를 사용해서 두번째 소제목을 추가하세요.
    ```
    2. Your Use of Google Play
    ```
1. `p`태그를 활용해서 두번째 내용을 추가하세요.
    ```
    Access to and Use of Content. You may use Google Play to browse, locate, view, stream, or download Content for your mobile, computer, tv, watch, or other supported device ("Device"). To use Google Play, you will need a Device that meets the system and compatibility requirements for the relevant Content, working Internet access, and compatible software. The availability of Content and features will vary between countries and not all Content or features may be available in your country. Some Content may be available to share with family members. Content may be offered by Google or made available by third-parties not affiliated with Google. Google is not responsible for and does not endorse any Content made available through Google Play that originates from a source other than Google.
    ```
1. 마지막으로 `h2`태그를 사용해서 세번째 소제목을 추가하세요.
    ```
    3. Purchases and Payments
    ```
1. `p`태그를 활용해서 세번째 내용을 추가하세요.
    ```
    Content on Google Play is offered by Google Commerce Limited, and when you download, view, use or purchase Content on or using Google Play, you will enter into a separate contract based on these Terms (as applicable) with Google Commerce Limited.
    ```
    
모두 완료했나요? `CSS` 없이 `HTML`만 작성하니 모습이 어색할 거예요. 하지만 괜찮습니다. 
이렇게 `HTML`만으로 구조를 먼저 작성하는 것은 아주 좋은 습관이거든요.
이제 `CSS`를 이용해서, 조금 더 스타일링을 해봅시다.

**NEXT STEP** 버튼을 클릭하세요.


## HELP
만약 잘 모르겠다면 아래에 있는 완성된 코드를 보고 따라 해 보는 것도 좋습니다. 다른 사람의 코드를 카피하는 것도 좋은 경험이거든요. 코딩은 외워서 하는 게 아닙니다. 반복적으로 코딩을 하다 보면 어쩔 수 없이 외워지는 거죠.

**Code**
```html
<div class="container">
  <img src="img_google_play.png" class="img-logo">
  <h1 class="headline">Google Play Terms of Service</h1>
  <h6 class="publication-date">February 5, 2018</h6>
  <h2>1. Introduction</h2>
  <p>Applicable Terms. Thanks for using Google Play. Google Play is a service provided by Google LLC ("Google", "we" or "us"), located at 1600 Amphitheatre Parkway, Mountain View, California 94043, USA. Your use of Google Play and the apps (including Android Instant Apps), games, music, movies, books, magazines, or other digital content or services (referred to as "Content") available through it is subject to these Google Play Terms of Service and the Google Terms of Service ("Google ToS") ( together referred to as the "Terms"). Google Play is a "Service" as described in the Google ToS. If there is any conflict between the Google Play Terms of Service and the Google ToS, the Google Play Terms of Service shall prevail.</p>
  <h2>2. Your Use of Google Play</h2>
  <p>Access to and Use of Content. You may use Google Play to browse, locate, view, stream, or download Content for your mobile, computer, tv, watch, or other supported device ("Device"). To use Google Play, you will need a Device that meets the system and compatibility requirements for the relevant Content, working Internet access, and compatible software. The availability of Content and features will vary between countries and not all Content or features may be available in your country. Some Content may be available to share with family members. Content may be offered by Google or made available by third-parties not affiliated with Google. Google is not responsible for and does not endorse any Content made available through Google Play that originates from a source other than Google.</p>
  <h2>3. Purchases and Payments</h2>
  <p>Content on Google Play is offered by Google Commerce Limited, and when you download, view, use or purchase Content on or using Google Play, you will enter into a separate contract based on these Terms (as applicable) with Google Commerce Limited.</p>
</div>
``` 
