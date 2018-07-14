## 타입과 태그
카드의 최 하단에 위치한 타입과 테그 텍스트를 스타일링 해봅시다. `.card-type`와 `.card-tag`를 동시에 지정해 주어야 합니다.

* `.card-type, .card-tag`의 마진은 위 `16px`, 나머지는 `0`입니다.*
* 글씨 크기는 `12px`입니다.
* 글씨 두깨는 `400`입니다.
* 글씨 컬러는 `#90949C`입니다.


**Instructions**
1. `.card-type, .card-tag`의 스타일 적용하기. 

    ```css
    .card-type, 
    .card-tag {
      margin: 16px 0 0 0;
      font-size: 12px;
      font-weight: 400;
      color: #90949C;
    }
    ```



## Hover
이제 가장 다이네믹한 파트가 기다리고 있습니다. 평소에는 `VIEW MORE` 가 보이지 않고 있다가, 마우스를 올리면 `VIDEO`가 사라지고, `VIEW MORE`가 나타나야 합니다. 어떻게 할까요? 아래와 같이 한단계씩 알아봅시다.

0.  `VIDEO`와 `VIEW MORE`가 있습니다.
1. `VIEW MORE`는 보이지 않습니다.
2. 카드에 마우스를 올리면 `VIDEO`를 사라집니다.
3. 카드에 마우스를 올리면 `VIEW MORE`는 나타납니다.

1, 2, 3번을 CSS로 표현해 봅시다.


**Instructions**
1. `.card-tag`를 보이지 않도록 `display`를 `none`으로 적용하기.
    ```css
    .card-tag {display: none;}
    ```

2. `.card`가 `hover`상태일때, `.card` 안에 있는 `.card-type`이 사라지도록 `display`를 `none`으로 적용하기.

    ```css
    .card:hover .card-type {display: none;}
    ```

3. `.card`가 `hover`상태일때, `.card` 안에 있는 `.card-tag`가 나타나도록 `display`를 `block`으로 적용하기.

    ```css
    .card:hover .card-tag {display: block;}
    ```

    

**NEXT STEP** 버튼을 클릭해서 완성된 모습을 봅시다!



## TIPS!

- 선택자는 좀 가물 가물 하네요. 두개의 클래스에 동시에 스타일을 적용하려고하면 어떻게 해야했죠?

  > 몇가지 많이 쓰는 선택자를 알려줄게요.
  >
  > * A와 B에 동시에 적용. 
  >
  >   ```css
  >   .classA, .classB {...} /* 클래스 사이에 ,로 구분합니다. */
  >   
  >   .classC, 
  >   .classD {...} /* 가독성을 위해 클래스간에 줄바꿈을 사용하기도 합니다.. */
  >   
  >   ```
  >
  > * A안에 있는 모든 B
  >
  >   ```css
  >   .classA .classB {...} /* 단지 한 칸 띄어씁니다.. */
  >   ```
  >
  > * A의 바로 1단계 안에 있는 B
  >
  >   ```css
  >   .classA > .classB {...} /* 클래스 사이에 > 마크가 있습니다. */
  >   ```
