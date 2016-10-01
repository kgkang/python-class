'''
Created on 2016. 10. 1.

@author: Administrator
'''

# property : 캡슐화의 원칙도 지켜주고 사용도 편리하도록 해준다.
#          : 함수명을 같게해주고
#          : getter에는 @property를 주고 
#          : setter에는 @함수명.setter를 준다.

class Shop:
    _price = 0
    
    @property  #decorator...
    def price(self):
        print("get price...")
        return self._price
    
    @price.setter
    def price(self, value):
        print("set call...")
        self._price = value
        
        
if __name__ == '__main__':
    shop = Shop()
    shop.price = 1000
    print(shop.price)
            