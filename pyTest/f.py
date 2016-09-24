'''
Created on 2016. 9. 24.

@author: Administrator
'''
import sys

myL = [10,20,30,40]

myL1 = myL
print( sys.getrefcount(myL)-1)

myL2 = myL
print( sys.getrefcount(myL)-1)

del(myL1)
print( sys.getrefcount(myL)-1)

# reference count가 없으면 객체를 삭제한다.
del(myL2)
print( sys.getrefcount(myL)-1)


def fn():
    # [10,20,30,40]은 heap에 할당됨
    # myL은 stack에 할당됨
    myL = [10,20,30,40]
    print(myL)
    return(myL)
    
fn()

my = fn()
print(my)

def fn1(a):
    a[0] = 100
    print(a)
    
myL = [10,20,30,40]
fn1(myL)
print(myL)

