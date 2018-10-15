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

# print(soup.prettify())

if soup.find('h3', text = 'from Frank'):
    print("성공")
else:
    print("실패")

