'''
Created on 2016. 9. 24.

@author: Administrator
'''
import sys

# 매개변수 테스트
# 명령창에서 python fun_sysTest2 aa bb cc dd 를 실행하면
# ['C:\\DevPy\\workspace\\git\\pyTest\\fun_sysTest2.py', 'aa', 'bb', 'cc', 'dd']

# 혹은 이클립스 에서는 run as ... => 
print(sys.argv)

# print 대신 아래 sys함수를 사용할 수 있다.
# sys.stdout.write("korea")
# sys.stdout.write("hello")

import time

tm = time.localtime()
print(tm)
print(tm.tm_year, tm.tm_mon, tm.tm_mday)

# 3초 후에 아래 hello가 출력된다. 
time.sleep(3)
print('hello')
