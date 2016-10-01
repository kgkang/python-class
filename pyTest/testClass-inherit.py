'''
Created on 2016. 10. 1.

@author: Administrator
'''

# 상속 => 교재 296 page
# 생성자 함수는 상속되지 않는다.

class People:
    name = ""
    age = 0
    def __init__(self,name,age):
        self.name = "아무개"
        self.age = 0
        
    def setName(self,n):
        self.name = n
        
    def getName(self):
        return self.name

class Student(People):
    stdNum = 0
    def __init__(self,name,age, stdNum):
        super().__init__(name, age) # 부모 클래스(super)의 생성자를 호출
#         self.name = name 
#         self.age = age
        self.stdNum = stdNum
    
if __name__ == '__main__':
#     std1 = Student()
#     std.name = "홍길동"
    std = Student('홍길동',30,20160101)
    std.setName("홍길동")
    std.age = 30
    std.stdNum = 20160101
    
    
    
    
    