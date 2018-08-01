# Medium Legal

우리가 레슨 1에서 만들었던 Google의 정책 페이지가 기억 나시나요? 이번에는 조금 더 보기 좋게 디자인 된 [Medium의 정책 페이지][https://legal.medium.com/]를 만들어 봅시다. 이번 레슨은 Medium 정책 페이지가 가로 해상도 768 x 1280일때의 상태를 기준으로 만들어졌습니다. (아직은 @media query를 사용할 때가 아닙니다!)



### **이 페이지의 구조**

![image](https://res.cloudinary.com/dyiqg9qhi/image/upload/v1533078133/img-wire-07_o6ryro.jpg)

이 페이지는 네비게이션 영역 / 히어로 영역 / 컨테이너 영역의 3단계로 구분되어 있습니다. 컨테이너 영역에는 제목과 부제목 그리고 본문으로 구성된 컨텐트 영역들이 배치되어 있습니다.

```
|- Body
    |- Navigation Bar
    |- Hero Image
    |- Container
    |   |- Content
    |   |   |- Headline Group
    |   |   |   |- Headline
    |   |   |   |- Sub-headline
    |   |   |- Content-text
    |   |- Content
    |   |   |- Headline Group
    |   |   |   |- Headline
    |   |   |   |- Sub-headline
    |   |   |- Content-text
    |   |- ...
```



### 기본 서체

Medium에는 별도의 서체를 사용하고 있습니다. 이번 레슨에는 Medium과 동일한 서체를 사용할 수는 없지만* 비슷한 서체를 사용할 수 있도록 CSS 코드가 첨부되어 있습니다. 서체는  [Google Fonts][https://fonts.google.com/] 에서 가져왔습니다.



**NEXT STEP** 버튼을 클릭하세요.
