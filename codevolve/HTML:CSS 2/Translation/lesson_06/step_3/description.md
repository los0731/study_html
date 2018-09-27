### .container

Here are the content elements of the policy page, excluding the logo and hero image. 

```
    |- Container
    |   |- Content
    |   |   |- Headline-group
    |   |   |   |- Headline
    |   |   |   |- Sub-headline
    |   |   |- Body text
    |   |- Content
    |   |   |- Headline-group
    |   |   |   |- Headline
    |   |   |   |- Sub-headline
    |   |   |- Body text
```

Looking just at the elements there are: headline, sub-headline and body text. The headline and subheadline are grouped into the headline group and together with the body, they form the content. Starting at the very top, let's write the tags for them, one by one. 

**Instructions**


1. Add `<div>` below `<div class="hero">` and apply `class="container"`.

    ```html
    <div class="container"></div>
    ```

1. Add 4 `<div>` in `<div class="container">` and apply `class="content"`

    ```html
    <div class="container">
        <div class="content"></div>
        <div class="content"></div>
        <div class="content"></div>
        <div class="content"></div>
    </div>
    ```

1. Add `<div>`  within first `<div class="content">`and apply `class="headline-group"`.

    ```html
    <div class="content">
        <div class="headline-group"></div>
    </div>
    ```

1. Add `<h1>` inside `<div class="headline-group">` and fill contents after applying `class="headline-text"`.

    ```html
    <div class="headline-group">
        <h2 class="headline-text">Legal @ Medium</h2>
    </div>
    ```

1. Add `<h3>` below `<h1 class="headline-text">` and fill contents after applying `class="sub-headline-text"`.

    ```html
    <div class="headline-group">
        <h1 class="headline-text">...</h1>
        <h3 class="sub-headline-text">Making Medium fair and safe</h3>
    </div>
    ```

1. Add `<p>` below `<div class="headline-group">` and fill contents after applying `class="content-text"`.

    ```html
    <div class="headline-group">
        <h1 class="headline-text">...</h1>
        <h3 class="sub-headline-text">...</h3>
        <p class="content-text">Ideas can only thrive in an environment governed by transparency, trust, and fairness – values that have shaped every aspect of Medium. Above all, Medium is a place that’s safe for anyone to participate. Below, we’ve broken down what you can expect when reading and writing on Medium.</p>
    </div>
    ```

1. Same as above, write code for the second `<div class="content">`

    ```html
    <div class="content">
        <div class="headline-group">
          <h2 class="headline-text">Intellectual property and privacy</h2>
          <h3 class="sub-headline-text">Your ownership and rights</h3>
        </div>
        <p class="content-text">You own everything that you write on Medium. Medium won’t sell it to anyone else. If you decide to delete a post or your entire account, we won’t keep it. You can use Medium to make or remix creative works, and on every post, you can specify the appropriate license (including Creative Commons). If someone is using Medium to unlawfully copy or distribute your creative work without permission, or confuse people about your identity, company, or product, we’ll investigate and where appropriate, take it down. Medium doesn’t sell your personal information, and we respect Do Not Track.</p>
      </div>
    ```

1. Same as above, write code for the third `<div class="content">`

    ```html
    <div class="content">
        <div class="headline-group">
          <h2 class="headline-text">Trust and Safety</h2>
          <h3 class="sub-headline-text">Core to a thoughtful conversation</h3>
        </div>
        <p class="content-text">On Medium, your trust and safety is not an afterthought. The way you feel when you interact with others on Medium is a core product feature. We think every day about how to make Medium a place for thoughtful, vigorous, civil conversation while also ensuring that Medium is free from harassment or intimidation.</p>
      </div>
    ```

1. Same as above, write code for the fourth `<div class="content">`

    ```html
    <div class="content">
        <div class="headline-group">
          <h2 class="headline-text">Transparency</h2>
          <h3 class="sub-headline-text">Direct windows in</h3>
        </div>
        <p class="content-text">Medium depends on our community’s trust. A key aspect of this is transparency – from writing our terms of service and other legal documents in plain, clear language to publishing an annual transparency report detailing takedowns and information requests, and sharing the rationale behind our decisions and processes.</p>
      </div>
    ```

1. Same as above, write code for the last `<div class="content">`

    ```html
    <div class="content">
        <div class="headline-group">
          <h2 class="headline-text">Advocacy</h2>
          <h3 class="sub-headline-text">Taking a stand for better internet</h3>
        </div>
        <p class="content-text">Medium advocates for our users in a range of forums around the world, including amicus briefs filed in U.S. courts and statements to Congress and various agencies in the U.S., as well as bodies outside the U.S., like the European Union Commission. We influence discussions on issues that we think are critical to a better internet, such as transparency about government data requests, copyright reform, and strong security.</p>
      </div>
    ```




Click the **NEXT STEP** button.

