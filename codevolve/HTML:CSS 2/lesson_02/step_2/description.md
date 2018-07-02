# 시작하기
`div`태그를 사용하여 카드의 틀을 만드는 것으로 시작합니다.

**Instructions**
1. `body`태그 안에 `div`태그를 추가하고, class 이름을 `birthday-card`로 적용하기. 
    ```html
    <div class="birthday-card"></div>
    ```



## 내용 채우기
`<div class="birthday-card">` 안에 카드의 요소들을 추가합니다. 

**Instructions**
1. 이미지를 추가하고, src attribute를 `https://image.freepik.com/free-vector/birthday-background-with-hand-drawn-gift_23-2147645419.jpg`, alt attribute를 `Birthday image`로 적용합니다. 
    ```html
    <img src="https://image.freepik.com/free-vector/birthday-background-with-hand-drawn-gift_23-2147645419.jpg" alt="Birthday Image">
    ```
1. 이미지 다음 라인에 `h1`태그를 사용해서 카드 내용을 추가하기.  
    ```html
    <h1>Happy Birthday. Hope you are having a great day Mechelle.</h1> 
    ```
1. 카드 내용 다음 라인에 `h3`태그를 사용해서 카드의 작성자를 추가하기. 
    ```html
    <h3>from Frank</h3>
    ```



## 이미지 출처 남기기
사실, 위에서 사용한 이미지는 제가 그린것이 아닙니다. 저는 어떤 이미지가 필요하면 지금 처럼 무료 소스 사이트를 이용합니다. 아래와 같은 사이트들이 있어요.
* https://www.freepik.com/
* https://www.pexels.com/

이런 사이트들은 일러스트레이션 또는 사진들을 무료로 사용할 수 있도록 소스를 공개해두고 있습니다. 파일을 다운로드 받거나, 마우스 우클릭 후 `이미지 주소 복사`를 통해서 이미지를 사용할 수 있습니다. 중요한 점은, 무료로 사용해도 되지만 반드시 출처를 남겨야 한다는 것입니다.

**Instructions**
1. `<div class="birthday-card">` 아래에 `h6`태그를 추가하고, class를 `sources-link`로 적용하기.
    ```html
    <h6 class="sources-link"></h6>
    ```
1. `h6`태그 안에 `a`태그를 추가하고, 출처 내용과 링크를 적용하기.  
    ```html
    <h6 class="sources-link">
      <a href="https://www.freepik.com/free-photos-vectors/background">Background vector created by Freepik</a>
    </h6> 
    ```



**NEXT STEP** 버튼을 클릭하세요.