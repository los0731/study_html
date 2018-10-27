from bs4 import BeautifulSoup

with open('index.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    tag = soup.body.find('table', class_="table-receipt").thead.find_next_sibling('tbody').find_all('tr')
    t_footer = tag[4].find('td', class_="t-footer", colspan="2")
    i = 0
    while i < 4:
        tag1 = tag[i].find('td', class_="t-label")
        tag2 = tag1.find_next_sibling('td', class_="t-content")
        
        i = i+1

        assert (
        len(tag) == 5
        and tag1
        and tag2
        and t_footer
        )

        print("===========")
        print(">>", i, ": ", tag1)
        print(">>", i, ": ", tag2)
        print("===========")
