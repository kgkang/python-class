'''
Created on 2016. 10. 1.

@author: Administrator
'''

# 생성자 함수 : 객체생성이 완료되면 자동으로 호출되는 함수
# 클래스 초기화 : 생성자함수에서 수행

# 파이선에는 오버로딩이라는 개념이 없음

class Test:
#     a = 0
#     b = 0
    def __init__(self,x=0,y=0): # 생성자함수, 기본은 self만 받지만,인자를 받을수도 있다.
        print("init called ...")
        self.a = x
        self.b = y

    def __del__(self): #소멸자 함수
        print("del ... called" type(self))
        
    def setData(self, x, y):
        self.a = x # a가 self에 없으면 자동으로 만들어준다.
        self.b = y
        
    def show(self):
        print(self.a, self.b)

def fn():
    obj = Test(300,400)
    obj.show()
    return obj
        
if __name__ == '__main__':
    obj = Test(100,200) # 생성자 함수를 호출해준다.
    obj1 = Test() # 인자를 안주고 호출할수 있다. 하지만 함수 선언부의 인자에 default 값이 선언되야 한다.
#     obj.setData(30, 40)

    obj.show()
    obj1.show()
    
    obj2 = fn()
    
    obj3 = fn()
    obj3.show()
    del(obj3) # 명시적으로 소멸자를 호출할 수 있다.
    print("end of main")
    
    # main 함수가 종료되면 남은 객체를 모두 소멸시킨다.
    
