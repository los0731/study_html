# Google Login
Google material design의 특징중 하나는 [스타일리시한 입력 폼](https://material-components.github.io/material-components-web-catalog/#/component/text-field)입니다. 클릭하면 Placeholder 글씨가 멋지게 움직이면서 라벨이 되죠. 구글의 이 다이나믹한 폼을 사용하려면 JavaScript를 이용해야 하지만 이 레슨에서는 JavaScript 없이 순수한 CSS만 이용하여 이 멋진 폼을 만들어 봅니다.



### 이 페이지의 구조
![image-1](https://res.cloudinary.com/dyiqg9qhi/image/upload/v1536398894/img-wire-09_didnd2.jpg)



`card`와 `footer`가 있습니다. 이 두 요소를 묶어 `card wrap`으로 만듭니다. 그리고 이것을 `container`로 감싼 후 `flexbox`를 이용하여 `card wrap`이 컨테이너 영역의 가운데 위치하도록 합니다. 이때 컨테이너의 최소 높이는 뷰의 전체 높이여야 합니다.

```
|- Body
    |- 컨테이너
	|	|- 카드 랩(Wrap)
	|   |   |- 카드(card)
	|	|	|	|- 헤더
	|	|	|	|- 입력 폼
	|	|	|	|- 이메일 찾기 버튼
	|	|	|	|- 안내 메시지
	|	|	|	|- 버튼 그룹
	|	|	|	|	|- 계정 만들기 버튼
	|	|	|	|	|- 로그인 버튼
	|   |   |- 푸터(footer)
	|	|	|	|- 언어 버튼
	|	|	|	|- 푸터 버튼 그룹
	|	|	|	|	|- 도움말 버튼
	|	|	|	|	|- 개인정보 보호 버튼
	|	|	|	|	|- 약관 버튼
```



**NEXT STEP** 버튼을 클릭하세요.