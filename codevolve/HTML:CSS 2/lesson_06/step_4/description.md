## 히어로 이미지
아까 언급한 카드히어로의 스타일을 순서대로 따라 적용해봅시다.
* `.card-hero`넓이는 `100%`입니다.
* 높이는 `296px`입니다.
* 배경 이미지가 있고, 소스는 `https://scontent-hkg3-1.xx.fbcdn.net/v/t15.0-10/12323191_10153628757763553_1398467009_n.jpg?_nc_cat=0&oh=76da236f6fc18effbfec0f9020e4d009&oe=5BDA9FDB`입니다.
* 배경 이미지는 반복되지 않습니다. 
* 배경 이미지의 위치는 x축 `center`, y축 `center`입니다. 
* 배경 이미지 크기는 `cover`입니다.
* 위 왼쪽 모서리의 반지름은 `4px` 입니다.
* 위 오른쪽 모서리의 반지름은 `4px` 입니다.


**Instructions**
1. `.card-hero`의 스타일 적용하기. 

    ```css
    .card-hero {
      width: 100%;
      height: 296px;
      background-image: url('https://scontent-hkg3-1.xx.fbcdn.net/v/t15.0-10/12323191_10153628757763553_1398467009_n.jpg?_nc_cat=0&oh=76da236f6fc18effbfec0f9020e4d009&oe=5BDA9FDB');
      background-repeat: no-repeat;
      background-position: center center;
      background-size: cover;
      border-top-left-radius: 4px;
      border-top-right-radius: 4px;
    }
    ```



## 카드 블록
히어로 이미지가 완성되었으니, 나머지 요소들의 묶음인 카드 블록의 스타일을 합시다. 

* `.card-block`의 패딩은 24px입니다.
* 배경 컬러는 white입니다.


**Instructions**
1. `.card-block`클래스의 스타일 적용하기.
    ```css
    .card-block {
      padding: 24px;
      background-color: white;
    }
    ```



## 제목 
카드의 제목은 h2태그를 사용하고 있습니다. 그리고 h2를 포함한 모든 heading태그에는 기본 적으로 마진이 적용되어있습니다. 따라서 타이틀의 스타일을 정의할 때, 기본 스타일을 고려해야합니다.

* `.card-title`의 마진은 `0`입니다.
* 글씨 크기는 `24px`입니다.
* 글씨의 두께는 `400`입니다.
* 행간은 `32px`입니다.


**Instructions**
1. `.card-title`클래스의 스타일 적용하기.
    ```css
    .card-title {
      margin: 0;
      font-size: 24px;
      font-weight: 400;
      line-height: 32px;
    }
    ```



## 설명 글

설명글은 원본의 본문의 글 중 앞 부분만 불러와서 보여줍니다. 따라서 얼마나 보여주어야하는 기준이 필요하죠. 여기서는 3줄까지만 보여주도록 할 것입니다. 3줄이 지나면 `...`처리가 되도록 해야합니다. 

- `.card-description`이 3줄 까지만 보여주고, 그 이상이면 `...`처리합니다.
- 위 마진은 `12px`이고 나머지 방향은 모두 0입니다.
- 글씨 크기는 `12px`입니다.
- 글씨의 두깨는 `400`입니다.
- 행간은 `20px`입니다.
- 글씨 컬러는 `#4B4F56`입니다.

**Instructions**

1. `.card-description`의 스타일 적용하기.

   ```css
   .card-description {
     display: -webkit-box;
     -webkit-line-clamp: 3;
     -webkit-box-orient: vertical;
     overflow: hidden;
     text-overflow: ellipsis;
     margin: 12px 0 0 0;
     font-size: 14px;
     font-weight: 400;
     line-height: 20px;
     color: #4B4F56;
   }
   ```





## 구분선

구분선으로 사용한 `hr`태그는 기본적으로 `border-width: 1px`이 적용되어 있습니다. 따라서 우리는 이 보더라인의 스타일을 조정하여 구분선으로 만들 수 있습니다.

- `.card-hr` 의 마진은 위 `16px`, 오른쪽 `0`, 아래 `0`, 왼쪽 `0` 입니다.
- 구분선의 스타일을 모두 지웁니다.
- 위-구분선은 `1px solid #ECEFF1` 입니다.

**Instructions**

1. `.card-hr`의 스타일 적용하기.

   ```css
   .card-hr {
     margin: 16px 0 0 0;
     border: 0;
     border-top: 1px solid #ECEFF1;
   }
   ```



**NEXT STEP** 버튼을 클릭하세요.



## TIPS!

- background-image + background-position + background-repeat = background

  > * 다음 두개의 스타일은 같습니다. 경우에 따라 위를 선택하기도, 더 간단한 아래를 선택하기도 합니다.
  >
  >   ```css
  >   background-image: url('...');
  >   background-repeat: no-repeat;
  >   background-position: center center;
  >   ==
  >   background: url('...') no-repeat center center;
  >   ```

- 3줄 까지만 뭐요? 난감하네요. 뭐 어떻게 해야하죠?

  > - 많은 개발자/디자이너들이 자신이 잘 모르는 요구조건을 만나면 가장 먼저 하는 것이 무엇일까요? 
  >
  > - 네. 바로 구글신에게 여쭤보는 것이죠. :-) 위의 케이스에는 보통 `text ellipsis 3 line css`라고 검색합니다. 그럼 대다수의 경우 해결이 되죠. 제가 찾은 코드는 아래와 같습니다.
  >
  >   ```css
  >   display: -webkit-box;
  >   -webkit-line-clamp: 3;
  >   -webkit-box-orient: vertical;
  >   overflow: hidden;
  >   text-overflow: ellipsis;
  >   ```
  >
  >   그럼 그것을 복붙하고, 되는지 체크 해봅니다. 이런식으로 stackoverflow.com, css-tricks.com 등에서 많은 지식을 얻어요.

- 위에 `border`를 `0`으로 하고, `border-top`을 또 주는 이유가 있어요? 

  > hr태그에는 기본적으로 `border-width: 1px`이 적용되어 있어요. 하지만 저는 `hr`태그에 `border-top`만 적용하고 싶습니다. 그래서 `border: 0`을 선언해서 기본 옵션을 초기화 해주는 겁니다. 그리고 거기에 새로운 `border-top` 속성을 부여하는거죠. 