'''
Created on 2016. 10. 1.

@author: Administrator
'''

# 오버라이딩 => 교재 281 page

# 추상함수 : 구현부가 없는 함수
# 추상클래스 : 추상함수가 있는 클래스
# 인터페이스클래스 : 추상함수로만 구성된 클래스
# 파이선에서는 상속받은 클래스에서 추상함수를 구현 안해도 에러나지 않음. 그냥 아무 짓도 하지 않음. 
# 파이선을 통해서는 디자인 패턴을 구현하기가 어렵다.

class Pet:
    def sleep(self):
        print('?? sleeping')
        
    def eat(self): # 추상함수 : 구현부가 없는 함수, 추상함수가 있는 클래스는 추상클래이스임.
        pass
#         print('?? eating')
        
    def speak(self):
        print('?? speaking')
        
class Dog(Pet): # Pet을 상속받음
    def speak(self): # 오버라이딩
        print('Dog speaking ...')
    def eat(self): 
        print('Dog eating...')

class Cat(Pet):
    def speak(self):
        print("Cat speaking...")
    def eat(self):
        print('Cat eating...')
        
if __name__ == '__main__':
    dog = Dog()
    dog.eat()
    dog.sleep()
    dog.speak()
    
