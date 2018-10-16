# 레슨 8 스텝 2 HTML

from bs4 import BeautifulSoup

with open('index.html', 'r') as file:
  soup = BeautifulSoup(file.read(), 'html.parser')

  list_elem = soup.find('body').contents # body 안에 모든 요소를 리스트로 추출.
  while '\n' in list_elem:list_elem.remove('\n') # base_tag 리스트의 공백만 찾아서 제거.
  

  base_tag = list_elem.find_all('nav')

  
  # assert(
  #   base_tag.name == 'div'
  #   and base_tag['class'][0] == 'content'
  # )
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