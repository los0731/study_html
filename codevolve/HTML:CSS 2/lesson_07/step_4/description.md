# 스타일
## 본문
본문의 스타일을 지정해 봅시다. 본문에 있는 내용은 페이지의 가운데에서만 보여집니다.

* `container`의 최대 넓이는 `630px`입니다.
* `container`의 마진은 상-하 `0`, 좌-우 `auto`입니다.


**Instructions**
1. `container`의 스타일 적용하기. 
    ```css
    .cotainer {
        max-width: 630px;
        margin: 0 auto;
    }
    ```

## 헤드라인 그룹
제목과 부제목을 감싸고 있는 헤드라인 그룹의 스타일을 지정해 봅시다. 바디 텍스트와 명확히 구분하기 위해 마진을 이용해서 간격을 설정하고, 글씨체를 변경합니다. 

* `.headline-group`의 마진은 상-하-좌-우 `64px 0 24px 0`입니다.
* `.headline-group`의 폰트는 `sans-serif`입니다.


**Instructions**
1. `.headline-group`클래스의 스타일 적용하기.
    ```css
    .headline-group {
    	margin: 64px 0 24px 0;
        font-family: sans-serif;
    }
    ```


## 제목, 부제목, 바디 텍스트 
제목과 부제목, 바디 텍스트의 스타일을 지정해봅시다. 

* `.headline-text`와 `.sub-headline-text`의 마진은 모두 `0`입니다.
* `.headline-text`의 폰트 굵기는 `900`입니다.
* `.sub-headline-text`의 폰트 굵기는 `400`입니다.
* `.sub-headline-text`의 폰트 컬러는 `rgba(162, 164, 181, .8)`입니다.
* `.body-text`의 마진은 상-하-좌-우 `0 0 80px 0`입니다.


**Instructions**
1. `.headline-text`와 `.sub-headline-text`클래스의 스타일 적용하기.
    ```css
    .headline-text,
    .sub-headline-text {
        margin: 0;
    }
    ```
1. `.headline-text`클래스의 스타일 적용하기.
    ```css
    .headline-text {
        font-weight: 900;
    }
    ```
1. `.sub-headline-text`클래스의 스타일 적용하기.
    ```css
    .sub-headline-text {
        font-weight: 400;
        color: rgba(162,164,181,.8);
    }
    ```
1. `.body-text`클래스의 스타일 적용하기.
    ```css
    .body-text {
        margin: 0 0 80px 0;
    }
    ```


다음 스탭에서는 미디어 쿼리에 대해서 알아봅니다. **NEXT STEP** 버튼을 클릭하세요.