'''
Created on 2016. 9. 24.

@author: Administrator
'''
def hap1(a,b):
    return a+b

# 람다함수, 임시함수 => 함수이름이 없음
hap2 = lambda a,b : a+b

ret = hap1(10,20)
print('hap1 =',ret)

ret = hap2(10,20)
print('hap2 =',ret)

# 그럼 람다함수는 왜 쓰나????
def show1(arg):
    for n in arg:
        print(n)

def show2(arg):
    for n in arg:
        print(n, end='=')

def fn(a, myfn):
    myfn(a)

myList = [10,20,30]
fn( myList, show1)
fn( myList, show2)

fn( myList, lambda x: print(x, sep="-"))
