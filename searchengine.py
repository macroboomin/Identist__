import requests
import bs4
import pandas as pd

title = []
link = []
keyword = input("검색할 단어는? ")


def scrap_page(num):
    url = f"https://search.naver.com/search.naver?&where=news&query={keyword}&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=76&start={num}&refresh_start=0"
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.text, 'lxml')
    items = soup.find_all("a", class_="news_tit")
    for item in items:
        tit = item.text
        title.append(tit)
        li = item.get('href')
        link.append(li)


pages = list(range(1, 61, 10))
for i in pages:
    scrap_page(i)

for i in range(60):
    print(i+1, end='/ ')
    print("제목 : ", title[i], "링크 : ", link[i])
