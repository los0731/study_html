### .card-hero

Like mentioned before, let's style the card's hero with CSS.
* The width of `.card-hero` is `100%`.
* The height is `296px`.
* The url of the background image is `https://scontent-hkg3-1.xx.fbcdn.net/v/t15.0-10/12323191_10153628757763553_1398467009_n.jpg?_nc_cat=0&oh=76da236f6fc18effbfec0f9020e4d009&oe=5BDA9FDB`.
* 배경 이미지는 반복하지 않습니다.
* 배경 이미지의 위치는 x축/y축  `center center`입니다. 
* 배경 이미지가 모든 영역을 덮어 씁니다.
* 위/왼쪽 모서리의 둥글기는 `4px`입니다.
* 위/오른쪽 모서리의 둥글기는 `4px`입니다.


**Instructions**
1. Apply style to `.card-hero`

    ```css
    .card-hero {
      width: 100%;
      height: 296px;
      background-image: url('https://scontent-hkg3-1.xx.fbcdn.net/v/t15.0-10/12323191_10153628757763553_1398467009_n.jpg?_nc_cat=0&oh=76da236f6fc18effbfec0f9020e4d009&oe=5BDA9FDB');
      background-repeat: no-repeat;
      background-position: center center;
      background-size: cover;
      border-top-left-radius: 4px;
      border-top-right-radius: 4px;
    }
    ```



### .card-block
Now that the hero image is complete, let's style the card block, a bundle of the rest of the elements of the card.

* `.card-block`의 패딩은 `24px`입니다.
* Background color is `white`.


**Instructions**
1. Apply style to `.card-block`.
    ```css
    .card-block {
      padding: 24px;
      background-color: white;
    }
    ```



### .card-title
The card's title uses  `<h2>`. A basic margin has been applied to all the title tags from `<h1>`to`<h6>`. Hence, when defining the style of the titles, the default style has to be taken into consideration. 

* `.card-title`의 마진은 `0`입니다. 
* The font size is `24px`.
* 글씨 두께는 `400`입니다.
* 행간은 `32px`입니다.


**Instructions**
1. Apply style to `.card-title`
    ```css
    .card-title {
      margin: 0;
      font-size: 24px;
      font-weight: 400;
      line-height: 32px;
    }
    ```



### .card-description

The description text should only show the beginning part of the text. Therefore we have to choose whether it will show 2 or 3 first lines of the text. Here we will set it to show up to only 3 lines. Whatever exceeds 3 lines will be displayed as `...`.

- `.card-description`이 3줄 까지만 보여주고, 그 이상이면 `...`처리합니다.
- 마진은 상/우/하/좌 `12px 0 0 0 0`입니다.
- The font size is `12px`.
- 글씨 두께는 `400`입니다.
- 행간은 `20px`입니다.
- The font color is `#4B4F56`. 

**Instructions**

1. Apply style to `.card-description`.

   ```css
   .card-description {
     display: -webkit-box;
     -webkit-line-clamp: 3;
     -webkit-box-orient: vertical;
     overflow: hidden;
     text-overflow: ellipsis;
     margin: 12px 0 0 0;
     font-size: 14px;
     font-weight: 400;
     line-height: 20px;
     color: #4B4F56;
   }
   ```





### .card-hr

`<hr>` used as a partition line, has a default setting of  `border-width: 1px`. that's why I usually overwrite it with a new `border` attribute and use a partition line that I actually like. 

- `.card-hr`의 마진은 상/우/하/좌 `16px 0 0 0`입니다.
- There are no borders.
- 상단 경계선은 `1px solid #ECEFF1`입니다.

**Instructions**

1. Apply style to `.card-hr`.

   ```css
   .card-hr {
     margin: 16px 0 0 0;
     border: 0;
     border-top: 1px solid #ECEFF1;
   }
   ```



Click the **NEXT STEP** button.



## TIPS!

- background-image + background-position + background-repeat = background

  > * The next two styles are the same. Depending on the situation you may choose the top one or the simpler, bottom one. 
  >
  >   ```css
  >   background-image: url('...');
  >   background-repeat: no-repeat;
  >   background-position: center center;
  >   ==
  >   background: url('...') no-repeat center center;
  >   ```

- What does it mean `first 3 lines only`? I'm lost. What do I have to do?

  > - What is the first thing that many developers/designers do when they come across a requirement they don't know or understand? 
  >
  >   In the above case, we usually search in Google for `text ellipsis 3 line css`. In most cases, it solves the problem. Here is the code that I found for that: 
  >
  >   ```css
  >   display: -webkit-box;
  >   -webkit-line-clamp: 3;
  >   -webkit-box-orient: vertical;
  >   overflow: hidden;
  >   text-overflow: ellipsis;
  >   ```
  >
  >   let's paste it in and check if it works. Then let's search on Google. Even I, when I don't remember something, look it up on Google. Moreover, you can get a lot of useful knowhow on `stackoverflow.com`, `css-tricks.com` and similar sites. 

- Why is `border` at the top set to `0` and `border-top` is added on?

  > By default the `<hr>` is set as `border-width: 1px`. However, I only want to apply `border-top` to `<hr>`. that's why I declared  `border: 0` and I reset the default option. And there I added a new `border-top` attribute. 