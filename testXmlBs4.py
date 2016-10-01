'''
Created on 2016. 10. 1.

@author: Administrator
'''

from bs4 import BeautifulSoup
import urllib.request as REQ

# tree = ET.parse('songs.xml')
# root = tree.getroot()
# 
# # for songElm in rss.findall('./channel/song'):
# for songElm in root.findall('.//song'):
#     print( songElm.attrib['album'])
#     print( songElm.findtext('title'))
#     print( songElm.findtext('singer'))

# 기상청 rss api ==> http://web.kma.go.kr/weather/lifenindustry/sevice_rss.jsp
# 서울 경기도 => http://web.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109
kURL = "http://web.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109"
response = REQ.urlopen(kURL)
soup = BeautifulSoup(response, 'html.parser')

# print(soup)

# ==================== 
# 서울 
# -------------
# 날짜:
# 날씨:
# 최저:
# 최고:
# -------------
# 날짜:
# 날씨:
# 최저:
# 최고:
# ==================
# 수원
# 

for loc in soup.findAll('location'):
    print("="*30)
    print( loc.city.string)
    for datas in loc.findAll('data'):
        print("-"*30)
        print("날짜 :", datas.tmef.string) # 대문자를 모두 소문자로 바꾼다.
        print("날씨 :", datas.wf.string)
        print("최저 :", datas.tmn.string)
        print("최고 :", datas.tmx.string)
 
