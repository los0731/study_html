# HTML

우리는 아주 옅은 회색의 배경에 명함 한 장이 떠 있는 모습을 연출할 겁니다. `<div>`를 사용하여 명함의 틀을 만들는 것으로 시작합니다. 

**Instructions**
1. `<body>`안에 `<div>`를 추가하고, `class="business-card"` 적용하기. 
    ```html
    <div class="business-card"></div>
    ```



### 명함 내용 채우기
`<div class="business-card">`안에 카드의 요소들을 추가합니다. 이 명함에는 컨셉을 잘 나타내주는 이미지와, 이름, 정보(직업, 전화번호, 이메일)가 있습니다. 이미지는 `iconfinder.com`에서 가져오고, 순서가 없는 리스트 태그를 사용해서 정보(직업, 전화번호, 이메일)를 나열할 겁니다.

**Instructions**
1. `<img>`를 추가하고, `class="image"`와 `alt="Profile image"` 적용하기. 
    ```html
    <img class="image" src="https://cdn3.iconfinder.com/data/icons/fantasy-and-role-play-game-adventure-quest/512/Orc-512.png" alt="Profile image">
    ```
1. `<h2>`를 추가하고, `class="name"`으로 적용하기.  
    ```html
    <h2 class="name">Jonathan Harris</h2> 
    ```
1. `<ul>`를 추가하고, `class="information"` 적용하기. 
    ```html
    <ul class="information"></ul>
    ```
1. `<ul>` 안에 `<li>`를 추가하고, 아래와 같이 각각 직업/전화번호/이메일에 맞는 클래스 적용하기.  
    ```html
    <ul class="information">
      <li class="job">Orc</li>
      <li class="phone">+1.23.456.7890</li>
      <li class="mail">jonathan@blackrockclan.com</li>
    </ul>
    ```



**NEXT STEP** 버튼을 클릭하세요.



# TIPS! 
* 무료 이미지 사용하기
    > 디자이너가 아닌 이상 직접 그래픽 소스를 만들어서 사용하기는 어렵기 때문에, 어떤 이미지가 필요하면 지금 처럼 무료 소스 사이트를 이용합니다. 대표적으로 아래와 같은 사이트들이 있습니다. 
    >
    > - https://www.freepik.com/ (그래픽이미지/일러스트레이션, 개인/상업적 사용가능, 출처를 남겨야 함.) 
    > - https://www.pexels.com/ (전문 포토그래퍼들이 찍은 사진, 개인/상업적 사용가능, 출처를 남길 필요 없음.) 
    > - https://www.iconfinder.com/free_icons (무료 아이콘, 개인/상업적 사용가능, 일부 컨텐츠는 출처를 남겨야 함.) 
    >
    > 이곳에서 이미지 소스의 파일을 다운로드 받거나, 마우스 우클릭 후 `이미지 주소 복사`를 통해서 이미지를 사용할 수 있습니다. 중요한 점은, 무료로 사용해도 되지만 반드시 저작권에 어긋나지 않게 사용하는 것입니다.   
