## HTML로 시작하기


이전 시간에 배웠던 `div`태그를 사용하여 카드의 틀을 만들어보겠습니다. 

순서대로 따라해 보면서 카드를 완성해 봅시다.

**Instructions**
1. `<body>`태그 안에 `<div>`태그를 추가하고, `birthday-card`라는 클래스를 적용하세요. 
1. 추가한 `<div>`태그 안에 카드를 꾸밀 이미지를 추가하세요.
이미지는 아래의 주소를 복사하고, `src`속성을 이용해 가져옵니다. 
```
    https://image.freepik.com/free-vector/birthday-background-with-hand-drawn-gift_23-2147645419.jpg
```

1. 이미지 다음에 `h1`태그를 사용해서 카드 내용을 추가하세요. 두 문장 사이는 `br`태그를 이용해 개행합니다.  
```
    Hope you are having a great day Mechelle. Happy Birthday.
```
1. 카드 내용 다음에 `h3`태그를 사용해서 카드의 작성자를 추가하세요. 
```
    from Frank
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
<div class="birthday-card">
      <img src="https://image.freepik.com/free-vector/birthday-background-with-hand-drawn-gift_23-2147645419.jpg" width="400" alt="Birthday Image">
      <h1>Hope you are having a great day Mechelle.<br>Happy Birthday. </h1>
      <h3>from Frank</h3>
    </div>
``` 