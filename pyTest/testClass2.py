'''
Created on 2016. 10. 1.

@author: Administrator
'''

# 캡슐화 : 멤버데이터에 직접 접근해 값을 R/W하지 않고 함수를 통해 RW, 데이터의 무결성을 위해...
# property : 캡슐화의 원칙도 지켜주고 사용도 편리하도록 해준다.


class Calendar:
    month=0
    def setMonth(self,m):
        if m>1 or m>12:
            print('wrong month')
        else:
            self.month = m 
    
    def getMonth(self):
        return self.month
    
    
if __name__ == '__main__':
    cal = Calendar()
    cal.month = 13
    cal.setMonth(13)
    print(cal.getMonth())
    
    #파이선에서는 접근 권한자(private 등의)가 없다