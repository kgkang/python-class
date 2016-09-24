'''
Created on 2016. 9. 24.

@author: Administrator
'''
# 표준 라이브러리 테스트

import os

print(os.name) # os name
print(os.getcwd()) # current word directory 

# 폴더를 이동한다.
# os.chdir("C:\\DevPy") # change directory
# print(os.getcwd()) # current word directory 

# 지정 경로 아래에 있는 폴더들을 리스트로 리턴해준다.
# print(os.listdir("C:\\DevPy")) 
# print(os.listdir(os.getcwd()))

# 현재 경로에 디렉토리를 생성한다.
# os.mkdir('my') 

# 파일을 삭제한다.
# os.remove('a.py') 

# 디렉토리를 삭제한다.
# os.rmdir('my')

print(os.path.isfile('a.py'))
print(os.path.isdir('sk'))

# OS의 명령어를 실행한다. ==> 실행결과값을 리턴 받지 못한다.
os.system('dir')
# os.system('notepad')

# 실행결과를 받아오기 위한 방법이 몇가지 있는데, 
# popen을 이용하는 경우
s = os.popen('dir').read()
print("실행결과 : ", s)


