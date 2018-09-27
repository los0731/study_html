### .headline-text, .sub-headline-text

Now let's trim the most detailed parts. First of all, the title and subheadings share a common style. it's the margin, of course. 

- The margin of `.headline-text` and `.sub-headline-text` is `0`.

**Instructions**

1. Apply style to `.headline-text,` and `.sub-headline-text`.

   ```css
   .headline-text,
   .sub-headline-text {
     margin: 0;
   }
   ```



### .headline-text

let's apply the title style. 

- `.headline-text`의 아래 마진은 `8px`입니다.
- The font size is `30px`.
- 글씨 두께는 `700`입니다.
- 행간은 `1`입니다.

**Instructions**

1. Apply style to `.headline-text`

   ```css
   .headline-text {
     margin-bottom: 8px;
     font-size: 30px;
     font-weight: 700;
     line-height: 1;
   }
   ```



### .sub-headlind-text

The subheadings, which assist the main title part, are expressed in smaller font, lighter color, less boldness.  

- The font size of `.sub-headline-text` is `24px`. 
- 글씨 두께는 `300`입니다.
- 행간은 `1.4`입니다.
- The font color is `#8f8f8f`.

**Instructions**

1. Apply style to `.sub-headline-text`.

   ```css
   .sub-headline-text {
     font-size: 24px;
     font-weight: 300;
     line-height: 1.4;
     color: #8f8f8f;
   }
   ```



### .content-text

Actually, the `<body>`'s style is applied to the the content text (`<p>`) as is, and other than adjusting the margin, there's no need to specify the style. it's because it is all already defined within the body. 

- `.content-text`의 마진은 상/우/하/좌 `0 0 80px 0`입니다.

**Instructions**

1. Apply style to `.content-text`.

   ```css
   .content-text {
     margin: 0 0 40px 0;
   }
   ```



Click the **NEXT STEP** button.