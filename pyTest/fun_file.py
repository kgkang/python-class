'''
Created on 2016. 9. 24.

@author: Administrator
'''

# 파일 테스트 , 교제 p333
# 시리얼, 페러렐 통신등 모두 파일을 사용하기 때문에.. 중요함..

def fileWrite():
    print('file write ....')
    fp = open('test.log', 'w')
    print("fp.tell:", fp.tell())
    fp.write('hello')
    fp.seek(3) # file pointer의 값을 이동시킨다.
    print("fp.tell:", fp.tell())
    fp.write('hello')
    print("fp.tell:", fp.tell())
    fp.close()

def fileRead():
    print('file read ....')
    fp = open('test.log','r')
    print("fp.tell:", fp.tell())
    rd = fp.read()
    print("fp.tell:", fp.tell())
    fp.close()
    print(rd)
    
if __name__ == '__main__':
    fileWrite()
    fileRead()
        