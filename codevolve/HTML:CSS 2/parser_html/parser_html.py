from bs4 import BeautifulSoup

with open('index.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    tag = soup.find_all('div', class_="content")[1].find('div', class_="headline-group")
    tag2 = tag.find('h2', class_="headline-text")
    tag3 = tag2.find_next('h3', class_="")

    assert(
        tag
    )

    print("===========")
    print(tag)
    print("===========")
    