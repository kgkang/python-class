'''
Created on 2016. 10. 1.

@author: Administrator
'''

import xml.etree.ElementTree as ET
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
xmlData = response.read()
xmlData = xmlData.decode('utf-8') # byte를 string으로 변환 

# print(xmlData)

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

root = ET.fromstring(xmlData)
for loc in root.findall('.//location'):
    print("="*30)
    print( loc.findtext('city'))
    for datas in loc.findall('./data'):
        print("-"*30)
        print("날짜 :", datas.findtext('tmEf'))
        print("날씨 :", datas.findtext('wf'))
        print("최저 :", datas.findtext('tmn'))
        print("최고 :", datas.findtext('tmx'))

    