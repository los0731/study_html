# 시작하기

우리는 아주 옅은 회색의 배경에 명함 한 장이 떠 있는 모습을 연출할 겁니다. `div`태그를 사용하여 명함의 틀을 만들는 것으로 시작합니다. 

**Instructions**
1. `body`태그 안에 `div`태그를 추가하고, 클래스 이름을 `business-card`로 적용하기. 
    ```html
    <div class="business-card"></div>
    ```



# 명함 내용 채우기
`<div class="business-card">` 안에 카드의 요소들을 추가합니다. 이 명함에는 컨셉을 잘 나타내주는 이미지와, 이름, 정보(직업, 전화번호, 이메일)가 있습니다. 이미지는 `iconfinder.com`에서 가져오고, 순서가 없는 리스트 태그를 사용해서 정보(직업, 전화번호, 이메일)를 나열할 겁니다.

**Instructions**
1. `img`태그를 추가하고, 클래스를 `image`로, alt attribute를 `Profile image`로 적용하기. 
    ```html
    <img class="image" src="https://cdn3.iconfinder.com/data/icons/fantasy-and-role-play-game-adventure-quest/512/Orc-512.png" alt="Profile image">
    ```
1. `h1`태그를 사용해서 이름을 추가하고, 클래스를 `name`으로 적용하기.  
    ```html
    <h1 class="name">Jonathan Harris</h1> 
    ```
1. `ul`태그를 추가하고, 클래스를 `information`으로 적용하기. 
    ```html
    <ul class="information"></ul>
    ```
1. `ul`태그 안에 `li`태그를 사용해서 직업, 전화번호, 이메일과 각 클래스 
    ```html
    <ul class="information">
      <li class="job">Orc</li>
      <li class="phone">+1.23.456.7890</li>
      <li class="mail">jonathan@blackrockclan.com</li>
    </ul>
    ```



이제 `CSS`를 이용해서, 조금 더 스타일링을 해봅시다.



**NEXT STEP** 버튼을 클릭하세요.



## TIPS! 
* [iconfinder.com][1]은 어떤 곳이죠? 
    > 아이콘 이미지를 무료로 공유하는 사이트입니다. 유료로 구매할 수도 있고요. 이곳에서는 별도의 출처를 기재하지 않도고 양질의 아이콘들을 사용할 수 있도록 자료를 공개하고 있습니다.     

[1]: https://www.iconfinder.com/