from bs4 import BeautifulSoup

with open('index.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    tag = soup.find('hr', class_="card-hr").find_next('h6', class_="card-type")
    tag2 = tag.find_next('h6', class_="card-tag")

    assert(
        tag
        and tag.text.strip() == 'VIDEO'
        and tag2
        and tag2.text.strip() == 'VIEW MORE'
    )

    print("===========")
    print(tag)
    print(tag2)
    print("===========")
    