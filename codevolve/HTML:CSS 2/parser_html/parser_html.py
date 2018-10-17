# 레슨 8 스텝 2 HTML

from bs4 import BeautifulSoup

with open('index.html', 'r') as file:
  soup = BeautifulSoup(file.read(), 'html.parser')

  # base_tag = nav.navigation의 다음에 오는 요소. 단 </body> 이후에 있는 요소도 찾음.
  base_tag = soup.find('nav', class_="navigation").find_next()
  

  # 조건 1,2,3을 모두 만족하면 통과.
  print(
    '찾는 태그 : ' + base_tag.name + '\n'
    '찾는 태그의 클래스 : ' + base_tag['class'][0] + '\n'
    '찾는 태그의 부모 : ' + base_tag.parent.name
    )

  # assert(
  #     base_tag.name == 'div'
  #     and base_tag['class'][0] == 'content'
  #     and base_tag.parent.name == 'body'
  #   )