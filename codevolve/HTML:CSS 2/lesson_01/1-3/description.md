순서대로 따라 해 봅시다. 가장 먼저, 글과 이미지들을 담아 두는 빈 공간, 
즉 `div`태그를 추가합니다.

> `div`태그(division tag)는 HTML 문서에서 `분할` 또는 `섹션`을 의미합니다. 
이 태그는 CSS로 스타일을 지정하거나, 여기서는 배우지 않지만 JavsScript로 특정 작업을 하기 위하여 
다른 HTML 요소들의 컨테이너로 많이 사용됩니다. 

`div`태그에 `container`라고 클래스를 추가합니다. 
그리고, `Materials`을 복사/붙여넣기하여 
로고 이미지, 제목, 게시일, 소제목, 문단들을 이 `div`태그 안에 추가합니다.

**Materials**
```html0    
<!-- 제목 -->
Google Play Terms of Service

<!-- 게시일 -->
February 5, 2018

<!-- 소제목 1 + 설명 문단 -->
1. Introduction
Applicable Terms. Thanks for using Google Play. Google Play is a service provided by Google LLC ("Google", "we" or "us"), located at 1600 Amphitheatre Parkway, Mountain View, California 94043, USA. Your use of Google Play and the apps (including Android Instant Apps), games, music, movies, books, magazines, or other digital content or services (referred to as "Content") available through it is subject to these Google Play Terms of Service and the Google Terms of Service ("Google ToS") ( together referred to as the "Terms"). Google Play is a "Service" as described in the Google ToS. If there is any conflict between the Google Play Terms of Service and the Google ToS, the Google Play Terms of Service shall prevail.

<!-- 소제목 2 + 설명 문단 -->
2. Your Use of Google Play
Access to and Use of Content. You may use Google Play to browse, locate, view, stream, or download Content for your mobile, computer, tv, watch, or other supported device ("Device"). To use Google Play, you will need a Device that meets the system and compatibility requirements for the relevant Content, working Internet access, and compatible software. The availability of Content and features will vary between countries and not all Content or features may be available in your country. Some Content may be available to share with family members. Content may be offered by Google or made available by third-parties not affiliated with Google. Google is not responsible for and does not endorse any Content made available through Google Play that originates from a source other than Google.

<!-- 소제목 3 + 설명 문단 -->
3. Purchases and Payments
Content on Google Play is offered by Google Commerce Limited, and when you download, view, use or purchase Content on or using Google Play, you will enter into a separate contract based on these Terms (as applicable) with Google Commerce Limited.
```
 
**Instructions**
* `body`태그 안에 `div`태그를 추가하세요.
* `div`태그에 `container`라는 클래스를 추가하세요.
* img_google_play.png 이미지를 추가하세요.
* `h1`태그를 사용해서 제목을 추가하세요. 
* `h6`태그를 사용해서 게시일을 추가하세요.
* `h2`태그와 `p`태그를 사용하여 섹션 1, 2, 3을 추가하세요.


**Hint**
```html
<div class="container">
  <img src="img_google_play.png">
  <h1>Google Play Terms of Service</h1>
  <h6>February 5, 2018</h6>
  <h2>2. Your Use of Google Play</h2>
  <p>Access to and Use of Content. You may use Google Play to browse, locate, view, stream, or download Content for your mobile, computer, tv, watch, or other supported device ("Device"). To use Google Play, you will need a Device that meets the system and compatibility requirements for the relevant Content, working Internet access, and compatible software. The availability of Content and features will vary between countries and not all Content or features may be available in your country. Some Content may be available to share with family members. Content may be offered by Google or made available by third-parties not affiliated with Google. Google is not responsible for and does not endorse any Content made available through Google Play that originates from a source other than Google.</p>
  <h2>3. Purchases and Payments</h2>
  <p>Content on Google Play is offered by Google Commerce Limited, and when you download, view, use or purchase Content on or using Google Play, you will enter into a separate contract based on these Terms (as applicable) with Google Commerce Limited.</p>
</div>
``` 
 
