'''
Created on 2016. 9. 24.

@author: Administrator
'''

import sys
print('sys.path =',sys.path)

# sys.path.append(".\\mylib")
# sys.path.append("C:\\DevPy\\workspace\\git\\pyTest\\mylib")
# print('sys.path =',sys.path)

import fun_module
# 아래 라인을 추가하면 모듈을 컴파일 하고 그것을 사용하게 됨.
# py_compile.compile("fun_module.py")

ret = fun_module.hap(10,20)
print(ret)


ret = fun_module.gop(30,40)
print(ret)



