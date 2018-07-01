## HTML로 시작하기


이전 시간에 배웠던 `div`태그를 사용하여 온라인 명함의 틀을 만들어보겠습니다. 

순서대로 따라해 보면서 온라인 명함을 완성해 봅시다.

**Instructions**
1. `<body>`태그 안에 `<div>`태그를 추가하고, `business-card`라는 class를 적용하세요. 
1. 추가한 `<div>`태그 안에 `h3`태그를 사용해서 명함 소유자의 이름을 추가하세요.
```
    FRANK PART
```
1. 소유자의 이름 다음에 `h6`태그를 사용해서 직업을 추가하고, `name`라는 class를 적용하세요. 
```
    Designer
```
1. 직업 다음에 `img`태그를 사용해서 명함 소유자를 대표하는 이미지를 추가하고, `representive-img`라는 class를 적용하세요. 

이미지는 아래의 주소를 복사하고, `src`속성을 이용해 가져옵니다. 
```
    "https://cdn4.iconfinder.com/data/icons/space-exploration-set/128/iStar_Design_Space_LineIcons_Live-2-512.png"
```

1. 이미지 다음에 `h6`태그를 사용해서 연락처를 추가하고, `phone-number`라는 class를 적용하세요. 
```
    +821012345667
```
1. 연락처 다음에 `h6`태그를 사용해서 이메일을 추가하고, `e-mail`라는 class를 적용하세요. 
```
    los0731@gmail.com
```
1. 이메일 다음에 `h6`태그를 사용해서 개인 홈페이지 주소를 추가하고, `personal-website`라는 class를 적용하세요. 
```
helloworld.com
```
1. `<div>`태그를 종료하세요. 


모두 완료했나요? `CSS` 없이 `HTML`만 작성하니 모습이 어색할 거예요. 하지만 괜찮습니다. 
이렇게 `HTML`만으로 구조를 먼저 작성하는 것은 아주 좋은 습관이거든요.
이제 `CSS`를 이용해서, 조금 더 스타일링을 해봅시다.

**NEXT STEP** 버튼을 클릭하세요.


## HELP
만약 잘 모르겠다면 아래에 있는 완성된 코드를 보고 따라 해 보는 것도 좋습니다. 다른 사람의 코드를 카피하는 것도 좋은 경험이거든요. 코딩은 외워서 하는 게 아닙니다. 반복적으로 코딩을 하다 보면 어쩔 수 없이 외워지는 거죠.

**Code**
```html
<div class="business-card">
      <h3 class="name">FRANK PARK</h3>
      <h6 class="job">Designer</h6>
      <img class="representive-img" src="https://cdn4.iconfinder.com/data/icons/space-exploration-set/128/iStar_Design_Space_LineIcons_Live-2-512.png">
      <h6 class="phone-number">+821012345667</h6>
      <h6 class="e-mail">los0731@gmail.com</h6>
      <h6 class="personal-website">helloworld.com</h6>
</div>
``` 