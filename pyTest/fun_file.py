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
 
def fileWrite1():
    print('file write ....')
    fp = open('test.log', 'w')
    fp.write('abcdefghijklmnop')
    fp.close()
    
def fileWrite2():
    fp = open('test.log', 'w')
    fp.write('abc\def\ghi\jkl\mno')
    fp.close()

def fileRead1():
    print('file read ....')
    fp = open('test.log','r')
    print("fp.tell:", fp.tell())
    rd = fp.read(3)
    print(rd)
    print("fp.tell:", fp.tell())
    rd = fp.read(3)
    print(rd)
    print("fp.tell:", fp.tell())
    fp.close()

# def fileRead2():
#     fp = open('test.log','r')
#     while True:
#         rd = fp.read(3)
#         if not rd:
#             break
#         print(rd)
#     fp.close()
    
def fileRead2():
    fp = open('test.log','r')
    while True:
        rd = fp.read(3)
        if not rd:
            break
        print(rd)
    fp.close()

def fileRead3():
    fp = open('test.log','r')
    for rd in fp: # readline으로 동작
        print(rd)
    fp.close()

def fileRead4():
    fp = open('test.log','r')
    rd = fp.readlines()
    print(rd)
    fp.close()

    
if __name__ == '__main__':
#     fileWrite()
#     fileRead()
#     fileWrite1()
#     fileRead1()
#     fileWrite1()
#     fileRead2()
    fileWrite2()
    fileRead4()
        