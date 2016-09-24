'''
Created on 2016. 9. 24.

@author: Administrator
'''

def print_header():
    print('============================')
    print('제품명    갯수    날짜')
    print('============================')

def mod_input(products):
    while True:
        product={}
        product['name']= input("제품명 : ")
        product['count'] = input("갯수 :")
        product['date'] = input("날짜 :")
        products.append(product)
        if ('n' == input("계속 입력하시겠습니까?(y/n)")):
            break

def mod_output(products):
    print_header()
    for product in products:
        print(product['name'],product['count'],product['date'])
    input("아무 키나 입력하세요")
    
def mod_find(products):
    name = input("검색할 이름을 입력하세요: ")
    print_header()
    for product in products:
        if (name == product['name']):
            print(product['name'],product['count'],product['date'])
    input("아무 키나 입력하세요")