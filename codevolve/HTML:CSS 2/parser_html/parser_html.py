from bs4 import BeautifulSoup

with open('index.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    tag = soup.find_all('div', class_="content")[4]
    tag1 = tag.find('div', class_="headline-group")
    tag2 = tag1.find('h2', class_="headline-text")
    tag3 = tag2.find_next('h3', class_="sub-headline-text")
    tag4 = tag1.find_next_sibling("p", class_="content-text")

    assert(
        tag4
    )

    print("===========")
    print(tag4)
    print("===========")
    