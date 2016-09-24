'''
Created on 2016. 9. 24.

@author: Administrator
'''

#파이선에서는 오버로딩이란 개념이 불가능하다.

#파이선에서는 디폴트 인자를 지원한다.
def fn(a=10,b=20,c=30):
    print(a,b,c)
    
# fn()
# fn(100)
# fn(100,200)
# fn(100,200,300)


def fn1(a,b=20,c=30):
    print(a,b,c)

# fn1() # 에러발생
# fn1(400)


#키워드 인자
def fn2(a,b):
    print(a,b)
    
fn2(10,20)
fn2(b=100,a=200)

#키워드 인자를 활용한 print , 기본은 sep는 ' '임
print(10,20)
print(10,20,sep='-')
print('hello',end=' ')
print('hi')

#가변인자 (variable argument)
def fn3_1(a):
    print(a)
    print(type(a))

fn3_1( (10,20,30))
fn3_1( [10,20,30])
fn3_1( 100 )
    
def fn3_2( *arg):
    print(arg)
    print(type(arg))

fn3_2(10,20)
fn3_2(10,20,30,40)

# def fn4(*arg, a): # 에러발생, 가번인자는 반드시 뒤에 와야 함.
def fn4(a, *arg):
    print(arg)
    
fn4(10,20,30,40)
