# HTML
### 컨테이너

우리는 컨테이너를 생성하는 것으로 시작할 수 있습니다. 컨테이너는 무언가를 담아두고 있는 의미를 가지고 있습니다. 여기서는 이미지와 글들을 담아두겠죠. 이런 컨테이너 역할을 하는 태그는 여러가지가 있지만, 지금과 같이 특정한 의미가 없는 묶음일 경우 주로 `<div> `를 사용합니다.


**Instructions**
1. `body` 태그 안에 `<div>` 를 추가하고, `class="container"` 적용하기.
    ```html
    <div class="container"></div>
    ```



### 컨테이너의 구성 요소
이제부터 `<div class="container">` 안에 나머지 요소들을 추가합니다. 위에서부터 순서대로 이미지, 제목, 게시일, 소제목, 본문을 추가합니다. 

**Instructions**
1. `<div class="container">` 안에 `<img>`를 추가하고, `src="img_google_play.png"` 와 `alt="Google Play"` 속성 적용하기.

    ```html
    <img src="img_google_play.png" alt="Google Play">
    ```

1. `<img>` 다음 줄에 `<h1>` (제목)을 추가하고, 아래 내용 채우기.
    ```html
    <!-- <img src="img_google_play.png" alt="Google Play"> -->
    <h1>Google Play Terms of Service</h1>
    ```

1. `<h1>` 다음 줄에 `<h6>` (게시일)를 추가하고, 아래 내용 추가하기.
    ```html
    <!-- <h1>Google Play Terms of Service</h1> -->
    <h6>February 5, 2018</h6>
    ```

1. `<h6>` 다음 줄에 `<h2>` (소제목)를 추가하고, 아래 내용 추가하기.
    ```html
    <!-- <h6>February 5, 2018</h6> -->
    <h2>1. Introduction</h2>
    ```

1. `<h2>` 다음 줄에 `<p>` (본문)를 추가하고, 아래 내용 추가하기.
    ```html
    <!-- <h2>1. Introduction</h2> -->
    <p>
        Applicable Terms. Thanks for using Google Play. Google Play is a service provided by Google LLC ("Google", "we" or "us"), located at 1600 Amphitheatre Parkway, Mountain View, California 94043, USA. Your use of Google Play and the apps (including Android Instant Apps), games, music, movies, books, magazines, or other digital content or services (referred to as "Content") available through it is subject to these Google Play Terms of Service and the Google Terms of Service ("Google ToS") ( together referred to as the "Terms"). Google Play is a "Service" as described in the Google ToS. If there is any conflict between the Google Play Terms of Service and the Google ToS, the Google Play Terms of Service shall prevail.
    </p>
    ```

1. 다음 줄에, 위와 같은 방식으로 두번째 `<h2>` (소제목), `<p>` (본문)을 추가하고, 아래와 내용 추가하기 두번째/세번째 소제목과 본문을 추가하기.

    ```html
    <!-- <h2>1. Introduction</h2> -->
    <!-- <P>...</p> -->
    <h2>2. Your Use of Google Play</h2>
    <p>
        Access to and Use of Content. You may use Google Play to browse, locate, view, stream, or download Content for your mobile, computer, tv, watch, or other supported device ("Device"). To use Google Play, you will need a Device that meets the system and compatibility requirements for the relevant Content, working Internet access, and compatible software. The availability of Content and features will vary between countries and not all Content or features may be available in your country. Some Content may be available to share with family members. Content may be offered by Google or made available by third-parties not affiliated with Google. Google is not responsible for and does not endorse any Content made available through Google Play that originates from a source other than Google.
    </p>
    ```

1. 다음 줄에, 위와 같은 방식으로 세번째  `<h2>` (소제목), `<p>` (본문)을 추가하고, 아래와 내용 추가하기 두번째/세번째 소제목과 본문을 추가하기.

    ```html
    <!-- <h2>2. Your Use of Google Play</h2> -->
    <!-- <P>...</p> -->
    <h2>3. Purchases and Payments</h2>
    <p>
        Content on Google Play is offered by Google Commerce Limited, and when you download, view, use or purchase Content on or using Google Play, you will enter into a separate contract based on these Terms (as applicable) with Google Commerce Limited.
    </p> 
    ```

    



모두 완료했나요? `CSS` 없이 `HTML`만 작성하니 모습이 어색하지만, 괜찮습니다. 이렇게 `HTML`만으로 구조를 먼저 작성하는 것은 아주 좋은 습관입니다. 이제 `CSS`를 이용해서, 스타일링을 해봅시다.



**NEXT STEP** 버튼을 클릭하세요.