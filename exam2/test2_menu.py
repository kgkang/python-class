'''
Created on 2016. 9. 24.

@author: Administrator
'''
import os
import pickle
from bs4 import BeautifulSoup

class Module:
    products = []
    def print_header(self):
        print('============================')
        print('제품명    갯수    날짜')
        print('============================')
    
    def mod_input(self):
        while True:
            product={}
            product['name']= input("제품명 : ")
            product['count'] = input("갯수 :")
            product['date'] = input("날짜 :")
            self.products.append(product)
            if ('n' == input("계속 입력하시겠습니까?(y/n)")):
                break
    
    def mod_output(self):
        self.print_header()
        for product in self.products:
            print(product['name'],product['count'],product['date'])
        input("아무 키나 입력하세요")
        
    def mod_find(self):
        name = input("검색할 이름을 입력하세요: ")
        self.print_header()
        for product in self.products:
            if (name == product['name']):
                print(product['name'],product['count'],product['date'])
        input("아무 키나 입력하세요")
    
    def mod_save(self):
        sel = input("저장하시겠습니까? (번호선택)(1.xml 2.pickle 3.취소)")
        if sel == '1':
            self.mod_save_xml()
        elif sel == '2':
            self.mod_save_pickle()

    def mod_read(self):
        self.products = []
        if (os.path.isfile('products.xml')):
            fp = open('products.xml','rt',encoding='utf-8')
            soup = BeautifulSoup(fp, 'html.parser')
            for item in soup.findAll('product'):
                self.products.append({'name': item.sname.string,
                                      'count':item.scount.string, 
                                      'date':item.sdate.string})
            fp.close()
        elif (os.path.isfile('products.dat')):
            fp = open('products.dat','rb')
            self.products = pickle.load(fp)
            fp.close()

        
    def mod_save_xml(self):
        xmlData=[]
        xmlData.append('<?xml version="1.0" encoding="UTF-8"?>')
        xmlData.append('<products>')
        for data in self.products:
            xmlData.append('\t<product>')
            xmlData.append('\t\t<sname>'+data['name']+'</sname>')
            xmlData.append('\t\t<scount>'+data['count']+'</scount>')
            xmlData.append('\t\t<sdate>'+data['date']+'</sdate>')
            xmlData.append('\t</product>')
        xmlData.append('</products>')
        xmlS = '\n'.join(xmlData)
        
        fp = open('products.xml', 'wt', encoding='utf-8')
        fp.write(xmlS)
        fp.close()

    def mod_save_pickle(self):
        fp = open('products.dat','wb')
        pickle.dump(self.products, fp)
        fp.close()

if __name__ == '__main__':
    
    choice = None
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    module = Module()
    module.mod_read()
    
    while True:
        clear()
        print("제품 관리 프로그램")
        print("===================")
        print("1. 입력")
        print("2. 출력")
        print("3. 검색")
        print("4. 저장")
        print("5. 종료")
        
        choice = input("메뉴를 선택하시오:")
        
        if choice == "1":
            clear()
            module.mod_input()
        elif choice == "2":
            clear()
            module.mod_output()
        elif choice == "3":
            clear()
            module.mod_find()
        elif choice == "4":
            clear()
            module.mod_save()
        elif choice == "5":
            print("종료합니다.")
            break
        else:
            print("잘못된 입력입니다.")
            