'''
Created on 2016. 9. 24.

@author: Administrator
'''
def fn():
    print('hello')
    print('hi')

def fn1(a,b):
    print(a,b)

def fn2(a,b):
    return a+b

# ret = fn2(10,20)
# print('ret = ', ret)

def circle(r):
    return r**2*3.14

# ret = circle(3)
# print("원의면적: ", ret)

def fn3():
    return 10,20

# 2개 이상의 값을 하나의 변수로 할당했을 때 tuple로 자동으로 변환(packing)된다.
# ret = fn3() 
# print(ret) 
# 
# ret1, ret2 = fn3()
# print(ret1)
# print(ret2)

def fn4():
    return (10,20)



def fn5():
    return [10,20,30]

# ret = fn5()
# print(ret)

def fn6(a,b,c):
    return min(a,b,c)

def min_val(a,b,c):
    mymin = a if a<b else b 
    mymin = mymin if mymin<c else c 
    return mymin

# print(fn6(4,5,6))

def yaksu1(a):
    y = []
    for div in range(1,a+1):
        if (a%div == 0):
            y.append(div)
            #print(div)
    return y

def yaksu2(a):
    y = [n for n in range(1,a+1) if  a%n==0] 
    return y       

# print( yaksu1(15))
# print( yaksu2(15))

def shape(r,h,w):
    return r**2*3.14, h*w 

ret = shape(3,10,20)
print(ret) #tuple
ret1,ret2 = shape(3,10,20)
print(ret1, ret2)
