# 시작하기 전에 - 구글 아이콘
아이콘 이미지를 브라우저에 표시하는 방법은 여러가지가 있습니다. jpg, png 이미지를 첨부 할 수도 있고, svg icon을 사용할 수도 있고, icon font를 활용할 수도 있습니다. 여기서 icon font를 활용할 수 있는 대표적인 방법은 구글 머테리얼 아이콘을 활용하는 것 입니다. 우리가 만들게 될 구글 검색 페이지에는 마이크 모양의 음성 검색 아이콘과 Apps 아이콘이 사용됩니다.

아이콘 폰트를 더 잘 사용하는 정식 가이드라인 [Material Design - Icon][2] 를 확인할 수 있습니다. 이번 레슨에서는 아이콘 폰트를 사용하기 위해 이미 세팅이 되어 있습니다. 구글 머테리얼 아이콘을 사용하기 위한 최소한의 규칙을 살펴봅시다.

`<head>`에 머테리얼 아이콘을 사용하기 위한 한줄의 코드가 첨부 되어있습니다. `<head>`에 이 코드를 추가하게되면 머테리얼 아이콘을 사용할 수 있습니다. 

```html
<body>
  <i class="material-icons">mic</i>
  <i class="material-icons">accessibility</i>
  <i class="material-icons">assessment</i>
  <i class="material-icons">alarm</i>    
</body>
```

또 이 태그에 특정 클래스를 추가하여 아이콘의 [크기를 조절][3]할 수 있습니다. 
```html
<body>
  <i class="material-icons md-18">mic</i>
  <i class="material-icons md-24">accessibility</i>
  <i class="material-icons md-36">assessment</i>
  <i class="material-icons md-48">alarm</i>
</body>
```




**NEXT STEP** 버튼을 클릭하세요.
