### Find account & Help

입력 폼 아래에는 자신의 이메일을 분실했을 경우에 대비하는 이메일 찾기 버튼이 있어야 합니다. 그리고 그다음에는 게스트 모드를 통해서 사용하는 방법에 대한 안내 문구가 표시됩니다. 여기서부터 사용하는 `<a>`는 실제로 기능하는 것은 아니기 때문에 하이퍼링크 속성은 공란으로 비워둡니다.

**Instructions**

1. `<div class="card-form">` 다음에 `<a>`를 추가하고, `class="btn-account-find"`, `href=""` 적용 및 내용 채우기. 

   ```html
   <a class="btn-account-find" href="">이메일을 잊으셨나요?</a>
   ```

2. `<a class="btn-account-find" href=""> `다음에 `<p>`를 추가하고, `class="help"` 적용 및 내용 채우고, 마지막 `자세히 알아보기` 문구에 하이퍼링크 적용하기.

1. ```html
   <p class="help">내 컴퓨터가 아닌가요? 게스트 모드를 사용하여 비공개로 로그인하세요. <a href="">자세히 알아보기</a></p>
   ```



### Card buttons

카드의 마지막 부분에는 `계정 만들기`와 `다음`버튼이 위치합니다. 이 두 버튼들을 하나로 묶어 `card-buttons`라고 합시다. 버튼까지 추가하면 `<div class="card-login">`에 들어가야 하는 요소는 모두 포함시키게 됩니다.

**Instructions**

1. `<p class="help">` 다음에 `<div>`를 추가하고, `class="card-buttons"`적용하기. 

   ```html
   <div class="card-buttons"></div>
   ```

2. `<div class="card-buttons"> `다음에 `<a>`를 추가하고, `class="btn btn-account-create"`, `href=""` 적용 및 내용 채우기.

   ```html
   <a class="btn btn-account-create" href="">계정 만들기</a>
   ```

3. `<a href="" class="btn btn-account-create"> `다음에 `<a>`를 추가하고, `class="btn btn-next"`, `href=""` 적용 및 내용 채우기.

   ```html
   <a class="btn btn-next" href="">다음</a>
   ```






**NEXT STEP** 버튼을 클릭하세요.