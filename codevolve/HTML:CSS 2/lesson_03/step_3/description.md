## 스타일
#### body 

명함의 색은 짙은 남색으로 만들고, 배경은 하늘색으로 설정합니다. 

**Instructions**
1. `body`의 `background-color`를 `#5FC9F1`로 설정하세요.
1. `business-card`클래스의 `background-color`를 `#2D3A67`로 설정하세요. 

#### 명함 디자인

`birthday-card`클래스를 가지고 있는 `div`태그는 명함의 틀을 만듭니다.

생일 축하 카드를 만들면서 배웠던 `margin`과 `padding`을 다시 연습해볼게요.
`margin`속성은 해당 클래스를 상위의 `body` 태그와 여백을 만들기 위해 사용합니다. 
`padding`속성은 해당 클래스 안에 있는 콘텐츠와 해당 클래스의 border 사이에 여백을 만들기 위해 사용합니다.
`box-shadow`속성은 해당 클래스에 그림자를 넣기 위해 사용합니다. 
예를 들어, `box-shadow: 80px 80px 100px -30px rgba(0,0,0,0.3)`는 순서대로 첫 번째 값은 수평, 두 번째 값은 수직, 세 번째 값은 블러 효과, 네 번째 값은 그림자의 반지름, 마지막 다섯 번째 값은 색을 설정합니다.
다섯 번째 값 `rgba`는 색에 투명도를 넣고 싶을 때 사용합니다.

마지막으로 `img`의 `filter`속성은 이미지의 명암을 반전 시키고 싶을 때 사용합니다. 

**Instructions**
1. `business-card`클래스의 `width`는 `400px`입니다.  
1. `img`의 넓이는 `100%`입니다. 넓이를 `100%`로 설정하면 이미지의 상단에 있는 태그인 business-class의 넓이에 맞게 설정됩니다.  
1. `img`의 `margin-top`은 `20px`입니다. 
1. `img`의 `filter`를 `brightness(0) invert(1);"`로 설정하세요.
1. `business-card`클래스의 `margin`은 상-하 `40px`이고, 좌-우 `auto`입니다. 
1. `birthday-card`클래스의 `padding`은 상-하-좌-우 모두 `40px`입니다. 
1. `birthday-card`클래스의 `box-shadow`의 수평은 `80px`, 수직은 `80px`, 블러 효과는 `100px`입니다.
1. `birthday-card`클래스의 `box-shadow`의 반지름은 `-30px`, 색은 `rgba(0, 0, 0, 0.3)`입니다. 


#### 폰트 디자인

가장 중요한 명함 소유자의 이름이 잘 보이게 만들어보겠습니다. 
`font-family`속성은 해당 클래스의 글씨체를 변경하기 위해 사용합니다. 
`font-weight`속성은 해당 클래스의 글씨를 두껍게 만들기 위해 사용합니다.

추가로 `h`태그는 기본적으로 `margin`값을 가지고 있기 때문에, 여백을 만들고 싶지 않으면 `0`으로 설정해주는 것이 좋습니다.  

**Instructions**
1. `name`클래스의 `font-family`는 `Arial`입니다.
1. `name`클래스의 `font-weight`는 `900`입니다.  
1. `name`클래스의 `color`는 `#5FC9F1`입니다.
1. `name`클래스의 `margin`는 `0`입니다.
1. `job`, `phone-number`, `e-mail`, `personal-website`클래스의 `color`는 `white`이고, `margin`는 `4px 0 0 0`입니다.
1. `phone-number`클래스의 `margin`을 `20px 0 0 0`으로 변경하세요. 

모두 완료했다면 **NEXT STEP** 버튼을 클릭하세요.
 

## HELP 
만약 잘 모르겠다면 아래에 있는 완성된 코드를 보고 따라해보세요. 

**Code**
```css
body {
  background-color: #5FC9F1;
}

.business-card {
  background-color: #2D3A67;
  width: 240px;
  margin: 40px auto; 
  padding: 40px;
  box-shadow: 80px 80px 100px -30px rgba(0,0,0,0.3); 
}

.representive-img {
  width: 100%;
  margin-top: 20px;
  filter: brightness(0) invert(1); margin-top: 20px;
}

.name {
  font-family: Arial;
  font-weight: 900;
  color: #5FC9F1;
  margin: 0;  
}

.job {
  color: white;
  margin: 4px 0 0 0;
}

.phone-number {
  color: white;
  margin: 20px 0 0 0;
}

.e-mail {
  color: white;
  margin: 4px 0 0 0;
}

.personal-website {
  color: white;
  margin: 4px 0 0 0;
}
``` 
