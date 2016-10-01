'''
Created on 2016. 9. 24.

@author: Administrator
'''

# 모듈 이름을 쓰기 귀찮은 경우

# from mymodule import hap, gop
from mymodule1 import hap, gop
# 해당 모듈의 모든 함수를 import할 경우
# from mymodule1 import *


def main():
    ret = hap(10,20)
    print(ret)


    ret = gop(30,40)
    print(ret)

    # __name__에는 
    print("useTest...", __name__)
    print(type(__name__))


# m 을 쓰고 엔터 치면 아래 라인이 자동 완성됨
if __name__ == '__main__':
    main()
    