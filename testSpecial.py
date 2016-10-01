'''
Created on 2016. 10. 1.

@author: Administrator
'''


class Test:
    def __init__(self,x,y):
        self.a = x
        self.b = y 
    
#     def __add__(self, y):
#         print('calling __add__')
#         return self.a + y 
    
    def __add__(self, y):
        print('calling __add__')
        return Test(self.a + y.a, self.b + y.b)
    
    def __sub__(self, y):
        print('calling __sub__')
        return self.a - y 
    
    def __eq__(self, y):
        return self.a == y.a and self.b == y.b
    
    def show(self):
        print(self.a, self.b)
    
    # 교재 301
    def __str__(self): 
        return "a=%d b=%d"%(self.a, self.b)
    
if __name__ == '__main__':
    obj = Test(100,200)
#     ret = obj + 10 # ret = obj.__add__(10)
#     ret = obj - 10 
#     print('returns =>',ret)
    
    obj1 = Test(100,200)
    
    # 등가연산자은 두 객체의 id를 비교한다. (address 비교) => 교재 309
    if obj == obj1: 
        print("같다")
    else:
        print("틀리다")
        
    
    
    t1 = Test(100,200)
    t2 = Test(10,20)
    t3 = t1 + t2
    
    t1.show()
    t2.show()
    t3.show()
    
    print( str(t3) )
    print( repr(t3) )
