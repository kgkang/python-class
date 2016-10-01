'''
Created on 2016. 10. 1.

@author: Administrator
'''

def fileWrite():
    print('file write...')
    fp = open('test.txt', 'w')
    fp.write('kor\nea')
    fp.close()
 
def fileRead():
    print('file read...')
    fp = open('test.txt','r')
    rd = fp.read()
    fp.close()
    print(rd)
    
if __name__ == '__main__':
    fileWrite()
    fileRead()