class Student:
    datas =[]
    def inputData(self):
        while True:
            name = input("이름:")
            age = int( input("나이:"))
            self.datas.append( {'name':name, 'age':age} )
            yn =input("계속입력(y/n):")
            if yn =='n':
                break
    def outputData(self):
        print('-'*30)
        print( "%10s%10s"%('이름','나이') )
        print('-'*30)
        for data in self.datas:
            print( '%(name)10s%(age)10d'%data )

if __name__ == '__main__':
    std = Student()
    std.inputData()
    std.outputData()
    

# datas =[]
# def inputData():
#     while True:
#         name = input("이름:")
#         age = int( input("나이:"))
#         datas.append( {'name':name, 'age':age} )
#         yn =input("계속입력(y/n):")
#         if yn =='n':
#             break
# def outputData():
#     print('-'*30)
#     print( "%10s%10s"%('이름','나이') )
#     print('-'*30)
#     for data in datas:
#         print( '%(name)10s%(age)10d'%data )
# 
# if __name__ == '__main__':
#     inputData()
#     outputData()


    
    
# datas =[]
# while True:
#     name = input("이름:")
#     age = int( input("나이:"))
#     datas.append( {'name':name, 'age':age} )
#     yn =input("계속입력(y/n):")
#     if yn =='n':
#         break
# 
# print('-'*30)
# print( "%10s%10s"%('이름','나이') )
# print('-'*30)
# for data in datas:
#     print( '%(name)10s%(age)10d'%data )    