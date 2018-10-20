from bs4 import BeautifulSoup

with open('index.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    tag = soup.find('div', class_="nav-right").find_all('a')

    assert(
        tag
        and len(tag) == 4
        and tag[0].text.strip() == 'Gmail'
        and tag[1].text.strip() == 'Images'
        and tag[2].find('i', class_="material-icons").text.strip() == 'apps'
        and tag[2].find('i', class_="md-24").text.strip() == 'apps'
        and tag[3].text.strip() == 'Sign in'
    )

    print("===========")
    print(tag)
    print(len(tag))
    print(tag[0].text.strip())
    print(tag[1].text.strip())
    print(tag[2].text.strip())
    print(tag[3].text.strip())
    print("===========")
    