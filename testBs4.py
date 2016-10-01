'''
Created on 2016. 10. 1.

@author: Administrator
'''


# BeautifulSop 설치 ( => https://www.crummy.com/software/BeautifulSoup/)
# html 및 xml 파싱에 유용한 3rd party library
# > pip install beautifulsoup4
# > C:\DevPy\Python34\Lib\site-packages\bs4

# 중앙일보 rss api => http://rss.joins.com/
# 중앙일보 rss => http://rss.joins.com/joins_news_list.xml

from bs4 import BeautifulSoup
import urllib.request as REQ

# fp = open('songs.xml')
# soup = BeautifulSoup(fp, 'html.parser')
# # print(soup)
# 
# for songElm in soup.findAll('song'):
#     print( songElm['album'])
#     print( songElm.title.string)
#     print( songElm.singer.string)
#     

jURL = "http://rss.joins.com/joins_news_list.xml"
response = REQ.urlopen(jURL)
soup = BeautifulSoup(response, 'html.parser')
# print(soup)

for itemElm in soup.findAll('item'):
    print("기사제목:", itemElm.title.string)
    print("기사내용:", itemElm.description.string)
