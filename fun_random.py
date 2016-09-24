'''
Created on 2016. 9. 24.

@author: Administrator
'''
# ==================================================
import random

# 1부터 10중에 랜덤하게 5개의 값을 생성
# 중복된 값이 나오기도 함
for n in range(5):
    rn = random.randint(1,10)
    print(rn)


# 중복되지 않은 데이타를 얻어오기 위해 shuffle을 사용한다.
my = [n for n in range(1,11)]
print(my)
random.shuffle(my)
print(my)

# ======================================================
import glob 
print(glob.glob('*.py'))
print(glob.glob('[abc]*.py')) #a 또는 b 또는 c로 시작하는 .py 확장자 파일을 가져옴