'''
Created on 2016. 10. 1.

@author: Administrator
'''

# BeautifulSop 설치 ( => https://www.crummy.com/software/BeautifulSoup/)
# html 및 xml 파싱에 유용한 3rd party library
# > pip install beautifulsoup4
# > C:\DevPy\Python34\Lib\site-packages\bs4

datas=[{'name':'홍길동','age':30},
       {'name':'이순신','age':40}]



xmlData=[]
xmlData.append('<rss>')
for data in datas:
    xmlData.append('\t<address>')
    xmlData.append('\t\t<name>'+data['name']+'</name>')
    xmlData.append('\t\t<age>'+str(data['age'])+'</age>')
    xmlData.append('\t</address>')
xmlData.append('</rss>')

#print(xmldata)
xmlS = '\n'.join(xmlData)
print(xmlS)