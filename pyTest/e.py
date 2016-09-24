'''
Created on 2016. 9. 24.

@author: Administrator
'''

g = 100

def fn1():
    g = 10
    print(g)
    
fn1()
print('global g = ',g)

def fn2():
    global g
    g = 10
    print(g)

fn2()
print('global g = ',g)


#파이선 내장 함수 확인
print( dir(__builtins__))

# 변수나 함수명에 빌트인 심벌을 사용하면 안됨, (명명규칙)
# 그 경우 local이 우선되기 때문에 해당 빌트인 기능을 사용못함.
# str = "abc"
# def fn3():
#     str = 'def'
#     print(str)
#     
# fn3()
# print(str)
# a = str(100)


