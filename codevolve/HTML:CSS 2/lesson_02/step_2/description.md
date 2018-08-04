# HTML
`<div>`를 사용하여 카드의 틀을 만드는 것으로 시작합니다.

**Instructions**
1. `<body>`안에 `<div>`를 추가하고, `class="birthday-card`적용하기. 
    ```html
    <div class="birthday-card"></div>
    ```



### 내용 채우기
`<div class="birthday-card">`안에 카드의 요소들을 추가합니다. 

**Instructions**
1. `<img>`를 추가하고,  `src="https://image.freepik.com/free-vector/birthday-background-with-hand-drawn-gift_23-2147645419.jpg"`와  `alt="Birthday image"`적용합니다. 
    ```html
    <img src="https://image.freepik.com/free-vector/birthday-background-with-hand-drawn-gift_23-2147645419.jpg" alt="Birthday Image">
    ```
1. 이미지 다음 라인에 `<h1>`를 사용해서 카드 내용을 추가하기.  
    ```html
    <h1>Happy Birthday. Hope you are having a great day Michelle.</h1> 
    ```
1. 카드 내용 다음 라인에 `<h3>`를 사용해서 카드의 작성자를 추가하기. 
    ```html
    <h3>from Frank</h3>
    ```



### 이미지 출처 남기기
사실, 위에서 사용한 이미지는 제가 그린것이 아닙니다. 디자이너가 아닌 이상 직접 그래픽 소스를 만들어서 사용하기는 어렵기 때문에, 어떤 이미지가 필요하면 지금 처럼 무료 소스 사이트를 이용합니다. 대표적으로 아래와 같은 사이트들이 있습니다.
* https://www.freepik.com/ (그래픽이미지/일러스트레이션, 개인/상업적 사용가능, 출처를 남겨야 함.)
* https://www.pexels.com/ (전문 포토그래퍼들이 찍은 사진, 개인/상업적 사용가능, 출처를 남길 필요 없음.)
* https://www.iconfinder.com/free_icons (무료 아이콘, 개인/상업적 사용가능, 출처를 남겨야 함.)

이곳에서 이미지 소스의 파일을 다운로드 받거나, 마우스 우클릭 후 `이미지 주소 복사`를 통해서 이미지를 사용할 수 있습니다. 중요한 점은, 무료로 사용해도 되지만 반드시 저작권에 어긋나지 않게 사용하는 것입니다. 

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



**NEXT STEP** 버튼을 클릭하세요.



# TIPS
* 이미지에 대체 글씨(Alternate/alt)를 추가하는 이유
    > alt는 이미지가 정상적으로 보이지 않는 상황에서 보이는 대체 글씨입니다. 예를 들어 화면을 볼 수 없는 상황의 사용자는 스크린리더로 이미지를 듣습니다. 이때 대체 글씨를 듣게 됩니다. 또는 네트워크가 좋지 않아서 이미지 로드를 실패했을 경우에도 텍스트를 표시하여 메시지를 전달하게 됩니다.