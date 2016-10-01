'''
Created on 2016. 10. 1.

@author: Administrator
'''



aa = b'abcd'
aa = aa.decode('utf-8') # byte를 string으로 디코딩
print(aa)


bb = 'abc'
bb = bb.encode(encoding='utf_8')
print(bb)