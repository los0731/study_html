## 스타일
#### body 

카드의 색을 하얀색으로 만들 것이기 때문에, 카드가 잘 보이도록 배경은 보라색으로 설정합니다. 

**Instructions**
1. `body`의 `background-color`를 `#512DA8`로 설정하세요. 

#### 카드 디자인

`birthday-card`class를 가지고 있는 `div`태그는 카드의 틀을 만듭니다. 
지금은 카드가 페이지의 상단에 딱 붙어있습니다. 하지만 카드가 페이지의 상단에서 조금 떨어져있다면 읽는 사람이 카드를 잘 볼 수 있을거에요. `margin`속성은 해당 class를 상위의 `body` 태그와 여백을 만들기 위해 사용합니다. 
`margin: 40px auto`과 같이 사용하면 상하 여백을 40px으로 설정하고 좌우는 자동으로 중앙에 설정합니다. 

`padding`속성은 해당 class 안에 있는 콘텐츠와 해당 class의 border 사이에 여백을 만들기 위해 사용합니다.
`padding: 16px`과 같이 사용하면 상-하-좌-우 여백을 모두 16px로 설정합니다.
카드 내부에 여백이 생기기 때문에 읽는 사람이 카드의 내용을 잘 볼 수 있을거에요.

`box-shadow`속성은 해당 class에 그림자를 넣기 위해 사용합니다. class를 더 입체적으로 보이게 만들 수 있어요. 
예를 들어, `box-shadow: 0 24px 40px -8px #311B92`는 순서대로 첫 번째 값은 수평, 두 번째 값은 수직, 세 번째 값은 블러 효과, 네 번째 값은 그림자의 반지름, 마지막 다섯번째 값은 색을 설정합니다. 

**Instructions**
1. `birthday-card`class의 `background-color`는 `white`입니다.  
1. `birthday-card`의 넓이는 `400px`입니다.  
1. `birthday-card`class의 `text-align`은 `center`입니다. 
1. `birthday-card`class의 `margin`은 상-하 `40px`이고, 좌-우 `auto`입니다. 
1. `birthday-card`class의 `padding`은 상-하-좌-우 모두 `16px`입니다. 
1. `birthday-card`class의 `box-shadow`의 수평은 `0`, 수직은 `24px`, 블러 효과는 `40px`입니다.
1. `birthday-card`class의 `box-shadow`의 반지름은 `-8px`, 색은 `#311B92`입니다. 

모두 완료했다면 **NEXT STEP** 버튼을 클릭하세요.
 

## HELP 
만약 잘 모르겠다면 아래에 있는 완성된 코드를 보고 따라해보세요. 

**Code**
```css
body {
  background-color: #512DA8;
}

.birthday-card {
  background-color: white;
  width: 400px;
  text-align: center;
  margin: 40px auto;
  padding: 16px;
  box-shadow: 0 24px 40px -8px #311B92;;
}
``` 
