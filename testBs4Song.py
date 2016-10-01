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
 
fp = open('songs.xml')
soup = BeautifulSoup(fp, 'html.parser')
channel = soup.find('channel')
song = soup.new_tag('song', album="album4") #{'album':'album4','my':'my4'}
title = soup.new_tag('title')
singer = soup.new_tag('singer')
song.append(title)
song.append(singer)
channel.append(song)
print(soup.prettify())

     
