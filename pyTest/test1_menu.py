'''
Created on 2016. 9. 24.

@author: Administrator
'''
import os
from test1_module import mod_input,mod_output,mod_find

choice = None
products = []

while True:
    os.system('cls')
    print("제품 관리 프로그램")
    print("===================")
    print("1. 입력")
    print("2. 출력")
    print("3. 검색")
    print("4. 종료")
    
    choice = input("메뉴를 선택하시오:")
    
    if choice == "1":
        os.system('cls')
        mod_input(products)
    elif choice == "2":
        os.system('cls')
        mod_output(products)
    elif choice == "3":
        os.system('cls')
        mod_find(products)
    elif choice == "4":
        print("종료합니다.")
        break
    else:
        print("잘못된 입력입니다.")
        