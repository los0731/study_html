### headline and sub-headline

이제부터 가장 디테일한 부분을 다듬어 봅시다. 우선 제목과 부제목에 공통으로 적용되는 스타일이 있습니다. 바로 마진이죠.

- The margin of `.headline-text` and `.sub-headline-text` is `0`.

**Instructions**

1. Apply style to `.headline-text,` and `.sub-headline-text`.

   ```css
   .headline-text,
   .sub-headline-text {
     margin: 0;
   }
   ```



### headline

제목의 스타일을 적용해 봅시다.

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



### sub-headlind

제목을 보조하는 부제목은 제목보다 크기와 컬러, 두께가 조금 약하게 표현됩니다.

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



### content-text

사실 body태그에서 지정한 스타일을 그대로 적용받는 이 컨텐트 텍스트 (`<p>`)는 마진을 통해서 간격만 조정할 뿐 별도의 스타일을 지정할 필요가 없습니다. body에서 이미 적용 되었기 때문이죠.

- `.content-text`의 마진은 상/우/하/좌 `0 0 80px 0`입니다.

**Instructions**

1. Apply style to `.content-text`.

   ```css
   .content-text {
     margin: 0 0 40px 0;
   }
   ```



Click the **NEXT STEP** button.