# HTML
Start by using `<div>` to make the frame of the card.

**Instructions**
1. Add `<div>` within `<body>` and apply `class="birthday-card`.
    ```html
    <div class="birthday-card"></div>
    ```



### 내용 채우기
Add elements of card in `<div class="birthday-card">`.

**Instructions**
1. Add `<img>`, and apply `src="https://image.freepik.com/free-vector/birthday-background-with-hand-drawn-gift_23-2147645419.jpg"` and `alt="Birthday image"`. 
    ```html
    <img src="https://image.freepik.com/free-vector/birthday-background-with-hand-drawn-gift_23-2147645419.jpg" alt="Birthday Image">
    ```
1. 이미지 다음에 `<h1>`를 사용해서 카드 내용을 추가하기.  
    ```html
    <h1>Happy Birthday. Hope you are having a great day Michelle.</h1> 
    ```
1. 카드 내용 다음에 `<h3>`를 사용해서 카드의 작성자를 추가하기. 
    ```html
    <h3>from Frank</h3>
    ```



### 이미지 출처 남기기
디자이너가 아니라면 직접 그래픽 소스를 만들어서 사용하기 어렵습니다. 이미지가 필요한 경우에 무료 소스 사이트를 이용할 수 있습니다. 대표적으로 아래와 같은 사이트들이 있습니다.
* https://www.freepik.com/ (그래픽이미지/일러스트레이션, 개인/상업적 사용가능, 출처를 남겨야 함.)
* https://www.pexels.com/ (전문 포토그래퍼들이 찍은 사진, 개인/상업적 사용가능, 출처를 남길 필요 없음.)
* https://www.iconfinder.com/free_icons (무료 아이콘, 개인/상업적 사용가능, 출처를 남겨야 함.)

이 곳에서 이미지 소스의 파일을 다운로드 받거나, 마우스 우클릭 후 `이미지 주소 복사`를 통해서 이미지를 사용할 수 있습니다. 중요한 점은 저작권에 어긋나지 않게 사용하는 것입니다. 

**Instructions**
1. `<div class="birthday-card">`아래에 `<h6>`를 추가하고, `class="sources-link"` 적용하기.
    ```html
    <h6 class="sources-link"></h6>
    ```
1. `<h6>` 안에 `<a>`를 추가하고, `href="https://www.freepik.com/free-photos-vectors/background"` 적용 후 아래 내용 추가하기.  
    ```html
    <h6 class="sources-link">
      <a href="https://www.freepik.com/free-photos-vectors/background">Background vector created by Freepik</a>
    </h6> 
    ```



Click the **NEXT STEP** button.



# TIPS
* 이미지에 `alt` 속성을 추가하는 이유
    > `alt` 속성은 Alternate의 줄임말입니다. 이미지가 정상적으로 보이지 않는 상황에서 보이는 대체 글씨입니다. 예를 들어 화면을 볼 수 없는 상황의 사용자는 스크린리더로 이미지를 듣습니다. 이때 `alt` 속성에 포함된 내용을 듣게 됩니다. 또는 네트워크가 좋지 않아서 이미지 로드를 실패했을 경우에도 `alt` 의 내용이 표시됩니다.