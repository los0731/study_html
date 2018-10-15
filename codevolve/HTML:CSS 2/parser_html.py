index_html = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Business-card</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
<div class="business-card">
  <img class="image" src="https://cdn3.iconfinder.com/data/icons/fantasy-and-role-play-game-adventure-quest/512/Orc-512.png" alt="Profile image">
  <h2 class="name">Jonathan Harris</h2>
  <ul class="information">
    <li class="job">Orc</li>
    <li class="phone">+1.23.456.7890</li>
    <li class="mail">jonathan@blackrockclan.com</li>
  </ul>
</div>
</body>
</html>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(index_html, 'html.parser')

base_tag = soup.body.select('body *')

print(base_tag)  

# print(base_tag.parent.attrs['class']) 부모요소 찾기.


# 향후 고려사항
#
# 위치
# A요소 다음에 B요소가 있다.
# A요소 안에 B요소가 있다.
#
# 순서
# A, B, C요소가 순서대로 있다.
# 3번째 A 요소의 클래스는 B다.
#
# 요소가 포함된 리스트의 값에서 '\n'을 찾아 삭제후 비교한다. -> 줄바꿈이 되어도 체크가 된다.