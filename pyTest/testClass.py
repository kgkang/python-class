'''
Created on 2016. 10. 1.

@author: Administrator
'''


# 교제 239 Page

class Test:
    a = 0
    b = 0
    def setData(self, x, y):
        self.a = x
        self.b = y
    def show(self):
        print("self=>", id(self))
        print(self.a, self.b)
        
if __name__ == '__main__':
    obj = Test()
    print("obj=>",id(obj))
    obj.setData(10, 20) # 첫번째 인수 self는 컴파일러가 자동으로 넘겨준다.
    obj.show()
    
    obj1 = Test()
    print("obj1=>",id(obj1))
    obj1.setData(100, 200) # 첫번째 인수 self는 컴파일러가 자동으로 넘겨준다.
    obj1.show()