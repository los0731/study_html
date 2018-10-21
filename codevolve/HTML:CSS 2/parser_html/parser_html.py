from bs4 import BeautifulSoup

with open('index.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    tag = soup.find('div', class_="nav-left").find_all('a')

    assert(
        tag
        and len(tag) == 3
        and tag[0].text.strip() == 'Privacy'
        and tag[1].text.strip() == 'Terms'
        and tag[2].text.strip() == 'Settings'
    )

    print("===========")
    print(tag)
    print("===========")
    