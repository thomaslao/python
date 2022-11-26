from bs4 import BeautifulSoup
import requests

addr="https://zh.wikipedia.org/wiki/%E8%87%BA%E7%81%A3%E8%A1%8C%E6%94%BF%E5%8D%80%E4%BA%BA%E5%8F%A3%E5%88%97%E8%A1%A8"

res=requests.get(addr).text
bs=BeautifulSoup(res,"html.parser")
rows=bs.find_all("tr")

for row in rows:
    if row.find('td'):
        #屬性stripped_strings去餘每欄中字串的空白符號
        cols =[item for item in row.stripped_strings]
        #讀取List物件的元素
        for item in range(0,len(cols)):
            print(cols[item], end = ' ')
        print() #換行
