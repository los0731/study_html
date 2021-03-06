# 코스와 레슨의 구조

`www.codevolve.com`의 `Creator`페이지에서 레슨을 추가할 때, 아래와 같은 구조로 레슨과 스탭을 추가합니다.

- **HTML/CSS Projects** (코스이름)
  - **Reading**: Project Intro
  - **Project:** Google Play Terms of Service
    - Step 1: HTML
    - Step 2: CSS 1
    - Step 3: CSS 2
    - Step 4: Completion
  - **Reading**: Project Intro
  - **Project:** Birthday Card
  - **Reading**: Project Intro
  - **Project:** Business Card
  - ...





# Tasks의 작성 가이드

하나의 Task는 하나의 지시(Instruction)와 같습니다. Codevolve에서는 하나의 Task에 여러개의 Checks를 추가하여 코드를 검증합니다. Task를 먼저 추가하고, 별도로 Checks를 추가한다음 Task에서 Checks를 선택하는 방식입니다. 레슨에서 Tasks를 추가할 때에는 다음의 규칙으로 추가합니다.

- **Description**은 아래와 이 `레슨 〉 스탭 〉 지시` 순으로 작성합니다. 이 사이드의 가이드와는 다르게 항목은 유저들이 보지 않는것같습니다.

  ```
  lesson1_step2_instruction1
  ```

- **Instructions**에는 마크다운으로 작성된 가이드를 작성합니다. 유저들인 이 항목을 보게 됩니다.

  ```
  Add `<div>` within `<body>` and apply `class="container"`
  ```

- **Failed Feedback**은 유저가 체크를 했으나 실패했을 때 노출됩니다. 이 항목에는 정답코드를 작성하여, 유저가 실패했을때 정답을 보고 따라 입력할 수 있도록 합니다. 상단에 `이 코드와 비교해보세요.` 라는 문구와 `코딩 컨벤션` 을 똑같이 맞춰달라는 안내 문구도 같이 추가합니다.

  **css의 경우:**

  ```
  <h3 id="title_feedback_failed">Let's compare it to this code.</h3>
  ​```css
  
  ​```
  <h6>If your code is correct but not a 'Well Done.', please match the coding style and coding convention to 'solution code'. and Please enter a correct value code.</h6>
  
  <style>
  	.custom-markdown.failure p:first-child {display:none;}
  	.custom-markdown.failure #title_feedback_failed {
          margin-top : 8px !important;
          font-weight : 700 !important;
          font-size : 16px !important;
  	}
  	.custom-markdown.failure .cmh-pre {
          margin : 8px -10px !important;
          border : none !important;
          padding : 4px !important;
  	}
      .custom-markdown.failure .cmh-pre+h6{
          margin : 2px 0 0 0 !important;
          font-weight : 400 !important;
          font-size : 12px !important;
          line-height : 18px !important;
          color : #607D8B !important;
  	}
  </style>
  ```

  ```
  
  <h3 id="title_feedback_failed">아래의 코드와 비교하세요.</h3>
  
  ​```css
  h1 {
  	margin: 40px 0 8px 0;
  	font-size: 20px;
  }
  ​```
  
  <h6>만약 올바르게 코드를 작성했는데도 불구하고 'Well Done.' 이라는 피드백이 보여지지 않는다면 정답코드와 비교 후, 정확한 코드를 입력하세요.</h6>
  ```



- **html의 경우:**

	```
	Please Check for position or typos in tags & properties. Some text contents require you to enter case-sensitive. Compare with solution code.
	```
	```
	태그와 프로퍼티에 오타는 없는지, 위치가 올바른지 확인하세요. 일부 컨텐트 글씨는 대소문자를 정확하게 입력해야 합니다. 위의 해답 코드와 비교해보세요.
  ```

- **Passed Feedback**은 모두 `Well Done.` 으로 통일합니다.

  ```
  Well Done.
  ```

- 나머지 옵션은 다음과 같이 선택합니다.

  - Live → on
  - Share Checks → off
  - Same Directory → on





# Checks 작성가이드

## CSS 검증 → Code Pattern

#### `Checks` 추가하기

Code Pattern은 일반적인 정규표현식을 통하여 코드를 검증합니다. CSS를 체크할 때 사용할 수 있습니다. 아래의 샘플 코드를 통해서 설명하겠습니다.

```css
.container {
    margin: 0 auto;
    padding: 0 16px;
    max-width: 630px;
}
```

 `.container` 라는 클레스를 사용하고, `margin`, `padding`, `max-width`를 사용해야하는 css 실습이 있다고 가정합시다. 위와 같이 3개의 프로퍼티를 측정해야하는 경우 총 3개의 `Checks`를 추가해야합니다.



#### `Checks` 작성

check는 1개의 css 프로퍼티만 검증할 수 있습니다. 따라서 3개의 프로퍼티를 검증하길 원할 경우, 3개의 check를 추가해야합니다.

- **Description**은 유저들에게 보이지 않습니다. 강사만 알아볼 수 있도록 ``클레스/태그 〉 프로퍼티 〉 값`의 형식으로 이름을 정합니다.

  ```
  .container {    margin: 0 auto;
  ```

- **Code Pattern**에 정규표현식을 사용하여 코드를 검증합니다. 아래와 같은 방식입니다.

  ```
  \.container\s*{[\s|\S]*?margin\s*:\s*0\s*auto\s*;[\s|\S]*?}
  ```

- **Filename**에는 검증할 파일명을 추가합니다.

  ```
  style.css
  ```

- **Test Code**는 해도되고 안해도 됩니다. 한 눈에 어떤 Check인지 알기 쉽게 하기위하여 솔루션 코드를 넣어두면 좋습니다.

  ```
  .container {
      margin: 0 auto;
  }
  ```

- 나머지 옵션들은 다음과 같습니다.

  - Case Sensitive → on
  - Present → on



#### CSS 검증을 위한 정규표현식 작성 템플릿

검증하고자 하는 코드가 아래와 같다면

```css
.form-search:hover,
.form-search:focus {
  padding: 10px auto;
}
```

위 css 코드에 대한 정규표현식은 다음과 같다.

```python
\.form-search:hover,\s*\.form-search:focus\s*{[\s|\S]*?padding\s*:\s*10\s*px\s*\s*auto\s*;[\s|\S]*?}
```

아래의 코드를 보고 값만 수정한다음 줄바꿈을 제거하고 복붙하면 편리합니다.

```python
\.form-search:hover,\s*
\.form-search:focus\s*{
    [\s|\S]*?
    	padding\s*:
    		\s*10\s*px\s*
    		\s*auto\s*;
    [\s|\S]*?
}
```



#### 설명

- `\s` : Matches any space, tab or newline character. 공백 문자를 찾음. 띄어쓰기, 줄바꿈, 탭 모두.
- `\S` : Matches anything other than a space, tab or newline.
- `*` : Matches as many characters as possible. 없구나 무한대로 있거나 모두 찾음
- `[\s|\S]` : 모든 문자
- `\s*` : 줄바꿈과 띄어쓰기가 있건 없건 모두 찾습니다. 코드상 띄어쓰기를 많이 해도 되고, 안해도 될때 사용합니다.
- `\s+` : 줄바꿈과 띄어쓰기가 최소 1개 이상 있어야하는 경우.
- `[\s|\S]*?내용[\s|\S]*?` : 내용 앞뒤고 어떤 문자가 오더라도 찾습니다. 



#### Online Test

- 이곳 (https://regexr.com/40oqm) 에서 작성중인 정규표현식을 테스트해볼 수 있습니다.





## HTML 검증 → HTML Parser

#### `Check` 작성

- Description은 유저들에게 보이지 않습니다. 따라서 추가해야하는 html 코드를 작성합니다. 이 항목에는 마크다운이 적용되어, 태그를 작성하면 보이지 않습니다. 

  ```html
  `<nav class="navigation"></nav>`
  ```

- Test Contents에 beautiful soup 코드를 작성합니다. [Beautiful soup 4.0.0의 한글 문서](http://pydockr.16mb.com/blog/beautifulsoup4.html)를 참고하세요.

  ```python
  from bs4 import BeautifulSoup
  
  with open('index.html', 'r') as file:
      soup = BeautifulSoup(file.read(), 'html.parser')
  
      base_tag = soup.find('nav', class_="navigation").find_next()
      assert(
          base_tag.name == 'div'
          and base_tag['class'][0] == 'content'
          and base_tag.parent.name == 'body'
      )
  ```

html parser를 이용한 체크는 아직 간단한 패턴을 찾지 못했습니다. 따라서 가장 많이 보이는 패턴위주로 작성할태니, 필요에 따라 활용하시면 됩니다.



#### 자주 사용되는 패턴

- **패턴1** :  `<body></body>` 안에 `<tag attr="">` 가 있는지 찾기.

  ```py
  from bs4 import BeautifulSoup
  
  with open('index.html', 'r') as file:
      soup = BeautifulSoup(file.read(), 'html.parser')
      tag = soup.body.find('nav', class_="navigation") #찾는 태그 
  
      assert(
          tag
      )
  ```

- **패턴2** :  `<tag attr="">` 안에 `<tag attr="">` 가 순서대로 0개 있는지 찾기.

  ```python
  from bs4 import BeautifulSoup
  
  with open('index.html', 'r') as file:
      soup = BeautifulSoup(file.read(), 'html.parser')
      tag = soup.find('div', class_="footer-right").find_all('a')
  
      assert(
          tag
          and len(tag) == 3
          and tag[0].text.strip() == 'Privacy'
          and tag[1].text.strip() == 'Terms'
          and tag[2].text.strip() == 'Settings'
      )
  ```

- 패턴3 :  `<tag attr="">` 다음에 `<tag attr="">` 가 있는지 찾기

  ```python
  from bs4 import BeautifulSoup
  
  with open('index.html', 'r') as file:
      soup = BeautifulSoup(file.read(), 'html.parser')
      tag = soup.find('div', class_="content").find_next('footer', class_="footer")
  
      assert(
          tag
          and tag.parent.name == 'body' 
          #find_next()는 <body> 밖에 있는 요소까지 찾기 때문에 별도로 부모 요소를 비교해야합니다.
      )
  ```


#### 유용한 문법

- **문법1** : 하위에 있는 요소 찾기

  ```python
  #find
  tag = soup.find('div', class_="footer-right")
  
  # boolean
  assert(tag)
  ```

- **문법2** : 부모요소 찾기

  ```python
  # find
  tag = soup.find_parent('div', class_="footer-right")
  
  # boolean
  assert(tag.parent.name == 'body')
  ```

- **문법3** : 다음에 오는 요소 찾기

  ```python
  # find
  tag = soup.find('div', class_="content").find_next('footer', class_="footer")
  
  # boolean
  assert(tag)
  ```

- **문법4** : 갯수찾기

  ```python
  # find
  tag = soup.find_all('div', class_="btn")
  
  # boolean
  assert(
      tag
      and len(tag) == 2
  )
  ```

- **문법5** : 텍스트 내용 비교하기

  ```python
  # find
  tag = soup.find_all('a', class_="btn")
  
  # boolean
  assert(
      tag
      and tag[0].text.strip() == 'New'
      and tag[1].text.strip() == 'Edit'
  )
  ```

- **문법6** : 이 요소가 특정 속성을 가지고 있으면 참 (속성이름을 비교하지 않고, 있는지 아닌지 만 비교)

  ```python
  # find
  tag = soup.body.find('a').has_attr('href')
  
  # boolean
  assert(
      tag
  )
  ```
