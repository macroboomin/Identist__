"""https://www.google.com/search?q=trump&tbm=nws&sxsrf=ALeKk02EYFr4jXK-tcA7dvfYGeg0fzSJog:1604852647529&ei=pxuoX4LiH5nN-Qb-tJGwBg&start=10&sa=N&ved=0ahUKEwjC0eP_rfPsAhWZZt4KHX5aBGYQ8tMDCI0B&biw=1920&bih=937&dpr=1"""
import requests
import bs4
import pandas as pd

title = []
link = []
keyword = input("Searching for? ")


def scrap_page(num):
    url = f"https://www.google.com/search?q={keyword}&tbm=nws&sxsrf=ALeKk02EYFr4jXK-tcA7dvfYGeg0fzSJog:1604852647529&ei=pxuoX4LiH5nN-Qb-tJGwBg&start=10&sa=N&ved=0ahUKEwjC0eP_rfPsAhWZZt4KHX5aBGYQ8tMDCI0B&biw=1920&bih=937&dpr=1"
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.text, 'lxml')
    items = soup.find_all("div", class_="BNeawe vvjwJb AP7Wnd")
    for item in items:
        tit = item.text
        title.append(tit)
    link_items = soup.find_all('a')
    li2 = ''
    c = 0
    for item in link_items:
        li = item.get('href')
        if li[0:12] == "/url?q=https":
            c += 1
            li2 = li[7:]
            if c % 2 == 0:
                link.append(li2)


pages = list(range(0, 60, 10))
for i in pages:
    scrap_page(i)

for i in range(60):
    print(i+1, title[i], link[i], sep='||')
"""
def scrap_page(num):
    url = f"https://www.google.com/search?q={keyword}&tbm=nws&sxsrf=ALeKk02EYFr4jXK-tcA7dvfYGeg0fzSJog:1604852647529&ei=pxuoX4LiH5nN-Qb-tJGwBg&start={num}&sa=N&ved=0ahUKEwjC0eP_rfPsAhWZZt4KHX5aBGYQ8tMDCI0B&biw=1920&bih=937&dpr=1"
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.text, 'lxml')
    items = soup.find_all("div", class_="JheGif nDgy9d")
    print(items)

    for item in items:
        tit = item.text
        title.append(tit)
    link_items = soup.find_all(
        "a", style_="text-decoration:none;display:block")
    for item in link_items:
        li = item.get('href')
        link.append(li)


scrap_page(0)
for i in title:
    print(title)

pages = list(range(0, 60, 10))
for i in pages:
    scrap_page(i)

for i in range(60):
    print(i+1, end='/ ')
    print("제목 : ", title[i], "링크 : ", link[i])"""
