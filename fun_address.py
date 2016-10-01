'''
Created on 2016. 9. 24.

@author: Administrator
'''

def fn():
    print('fn()...')
    
def fn1():
    print('fn1()...')

myD = {0:fn, 1:fn1}
myD[0]()
myD[1]()

fn1 = fn
print(id(fn))
fn1()