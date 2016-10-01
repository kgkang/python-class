'''
Created on 2016. 10. 1.

@author: Administrator
'''

# 교제 341 page => 직렬화 , 역직렬화
# 교제 343 page => with 구문 (fp.close를 자동으로 호출해준다)

import pickle


def obWrite():
    # myList = [10,20,30]
    datas=[{'name':'홍길동','age':30},
           {'name':'임걱정', 'age':40}]
    fp = open("ob.txt","wb")
    pickle.dump(datas,fp)
    print('before', fp.closed)
    fp.close()
    print('after', fp.closed)
    
    
def obWriteWith():
    # myList = [10,20,30]
    datas=[{'name':'홍길동','age':30},
           {'name':'임걱정', 'age':40}]
    with open("ob.txt","wb") as fp:
        pickle.dump(datas,fp)
        print('before', fp.closed)

    print('after', fp.closed)    
    
def obRead():
    fp = open("ob.txt","rb")
    my = pickle.load(fp)
    fp.close()
    print(my)
    for data in my:
        print("이름:%(name)s 나이:%(age)d" %data)
    
if __name__ == '__main__':
    obWriteWith()
    obRead()