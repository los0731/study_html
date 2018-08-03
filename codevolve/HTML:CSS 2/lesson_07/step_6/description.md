### 제목과 부제목

이제부터 가장 디테일한 부분을 다듬어 봅시다. 우선 제목과 부제목에 공통으로 적용되는 스타일이 있습니다. 바로 마진이죠.

- `.headline-text, .sub-headline-text`의 마진은 `0`입니다.

**Instructions**

1. `.headline-text, .sub-headline-text`의 스타일 적용하기.

   ```css
   .headline-text,
   .sub-headline-text {
     margin: 0;
   }
   ```



### 제목

제목의 스타일을 적용해 봅시다.

- `.headline-text`의 아래 마진은 `8px`입니다.
- 글씨 크기는 `30px`입니다.
- 글씨 두깨는 `700`입니다.
- 행간은 `1`입니다.

**Instructions**

1. `.headline-text`의 스타일 적용하기.

   ```css
   .headline-text {
     margin-bottom: 8px;
     font-size: 30px;
     font-weight: 700;
     line-height: 1;
   }
   ```



### 부제목

제목을 보조하는 부제목은 제목보다 크기와 컬러, 두깨가 조금 약하게 표현됩니다.

- `.sub-headline-text`의 글씨 크기는 24px입니다.
- 글씨 두깨는 `300`입니다.
- 행간은 `1.4`입니다.
- 글씨 색상은 `#8f8f8f`입니다.

**Instructions**

1. `.sub-headline-text`의 스타일 적용하기.

   ```css
   .sub-headline-text {
     font-size: 24px;
     font-weight: 300;
     line-height: 1.4;
     color: #8f8f8f;
   }
   ```



컨텐트 텍스트

사실 body태그에서 지정한 스타일을 그대로 적용받는 이 컨텐트 텍스트 (`p`태그)는 마진을 통해서 간격만 조정할 뿐 별도의 스타일을 지정할 필요가 없습니다. body에서 이미 적용 되었기 때문이죠.

- `.content-text`의 마진은 상/하/좌/우 `0 0 80px 0`입니다.

**Instructions**

1. `.content-text `의 스타일 적용하기.

   ```css
   .content-text {
     margin: 0 0 40px 0;
   }
   ```



**NEXT STEP** 버튼을 클릭하세요.