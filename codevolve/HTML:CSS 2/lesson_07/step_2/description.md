# 여러개의 세션 만들기

앞서 Medium의 정책 페이지의 본문은 여러 개의 세션으로 구성되어 있고, 하나의 세션은 3가지 요소(제목, 부제목, 문단)로 구성되어 있다고 했습니다.

4개의 세션을 더 추가해보겠습니다.


1. `container`class 안에 앞서 만들었던 `section`class를 추가하기.
    ```html
    <body>
      <div class="navbar">Medium</div>
      <div class="hero"></div>
      <div class="container">
        <div class="section">
            <div class="headline-group">
                <div class="headline-text">Intellectual property and privacy</div>
                <div class="sub-headline-text">Your ownership and rights</div>
            </div>
            <p class="body-text">You own everything that you write on Medium. Medium won’t sell it to anyone else. If you decide to delete a post or your entire account, we won’t keep it. You can use Medium to make or remix creative works, and on every post, you can specify the appropriate license (including Creative Commons). If someone is using Medium to unlawfully copy or distribute your creative work without permission, or confuse people about your identity, company, or product, we’ll investigate and where appropriate, take it down. Medium doesn’t sell your personal information, and we respect Do Not Track.</p>
        </div>
      </div>
    </body>
    ```

1. `container`class 안에 앞서 만들었던 `section`class를 추가하기.
    ```html
    <body>
      <div class="navbar">Medium</div>
      <div class="hero"></div>
      <div class="container">
        <div class="section">
            <div class="headline-group">
                <div class="headline-text">Trust and Safety</div>
                <div class="sub-headline-text">Core to a thoughtful conversation</div>
            </div>
            <p class="body-text">On Medium, your trust and safety is not an afterthought. The way you feel when you interact with others on Medium is a core product feature. We think every day about how to make Medium a place for thoughtful, vigorous, civil conversation while also ensuring that Medium is free from harassment or intimidation.</p>
        </div>
      </div>
    </body>
    ```

1. `container`class 안에 앞서 만들었던 `section`class를 추가하기.
    ```html
    <body>
      <div class="navbar">Medium</div>
      <div class="hero"></div>
      <div class="container">
        <div class="section">
            <div class="headline-group">
                <div class="headline-text">Transparency</div>
                <div class="sub-headline-text">Direct windows in</div>
            </div>
            <p class="body-text">Medium depends on our community’s trust. A key aspect of this is transparency – from writing our terms of service and other legal documents in plain, clear language to publishing an annual transparency report detailing takedowns and information requests, and sharing the rationale behind our decisions and processes.</p>
        </div>
      </div>
    </body>
    ```
1. `container`class 안에 앞서 만들었던 `section`class를 추가하기.
    ```html
    <body>
      <div class="navbar">Medium</div>
      <div class="hero"></div>
      <div class="container">
        <div class="section">
            <div class="headline-group">
                <div class="headline-text">Advocacy</div>
                <div class="sub-headline-text">Taking a stand for better internet</div>
            </div>
            <p class="body-text">Medium advocates for our users in a range of forums around the world, including amicus briefs filed in U.S. courts and statements to Congress and various agencies in the U.S., as well as bodies outside the U.S., like the European Union Commission. We influence discussions on issues that we think are critical to a better internet, such as transparency about government data requests, copyright reform, and strong security.</p>
        </div>
      </div>
    </body>
    ```


**NEXT STEP** 버튼을 클릭하세요.

