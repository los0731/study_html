# Google Login
Google material design의 특징중 하나는 [스타일리시한 입력 폼](https://material-components.github.io/material-components-web-catalog/#/component/text-field)입니다. 폼을 클릭하면 Placeholder 글씨가 멋지게 움직이면서 라벨이 되죠. 구글의 이 다이나믹한 폼을 사용하려면 JavaScript를 이용해야 합니다. 하지만 이 레슨에서는 JavaScript 없이 순수한 CSS만 이용하여 이 멋진 폼을 만들어 봅니다.



### 이 페이지의 구조
![image-1](https://res.cloudinary.com/dyiqg9qhi/image/upload/v1532609841/wire/img-wire-01.jpg)



코드를 작성하는것 만큼 중요한 것은, 그 구조를 이해하는 것입니다. 이 페이지는 하나의 묶음(Container)에 로고 이미지와 글들이 순서대로 나열되어있습니다. 우리는 먼저 HTML을 이용해서 이 페이지의 뼈대를 잡아야합니다.

```
|- Body
    |- 컨테이너
    |   |- 로고 이미지
    |   |- 제목
    |   |- 게시일
    |   |- 소제목 1
    |   |- 본문
    |   |- 소제목 2
    |   |- 본문
    |   |- 소제목 3
    |   |- 본문
    |   |- ...
```



**NEXT STEP** 버튼을 클릭하세요.