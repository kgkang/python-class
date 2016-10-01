'''
Created on 2016. 9. 24.

@author: Administrator
'''

# 정의되지 않은 인자
def fn1_1(**arg):
    print(arg)
    print(type(arg))
    
fn1_1( name='홍길동',age=30, addr='서울시')

myD = {'name':'임꺽정', 'age':40}
fn1_1(**myD) # dictionary를 2정의되지않은 인자로 넘겨줄때 **를 앞에 붙인다
# def fn1_2(**arg):
#     print(arg)
#     print(type(arg))


a=10
b=3.14
c='abc'
s1='a=%d b=%fun_memory_reference_count c=%s' %(a,b,c)
# s2= '이름:%(name)s 나이:%(age)d' %myD
s2= '이름:%(name)10s 나이:%(age)10d' %myD
# s3= 'a={0}, b={1}, c={2}'.format(a,b,c)
# s3= 'a={0:10}, b={1:10}, c={2:10}'.format(a,b,c)
s3= 'a={0:10}, b={1:10}, c={2:>10}'.format(a,b,c)
s4= '이름:{name} 나이:{age}'.format(name='aaa', age=30)
s5= '이름:{name} 나이:{age}'.format(**myD)

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)