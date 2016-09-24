
김일한
(주)소프트캠퍼스
ilhank@naver.com




월요일 오후 1시반 


파이선 개발
1. eclipse
  - eclipse pydev 플러그인설치 (www.eclipse.org)
  - pythone 3.4.4 다운로드 및 설치 (www.python.org)
2. pycharm (자동완성)
3. atom : 가벼움, c, c++ 도 가능

<< 파이선 라이브러리 종류 >>
1. built in => import사용안함.
  (파이선 내장클래스, 함수, 변수)
   내장클래스 => 주로 예외처리, 대문자로 시작
   함수 : 형변환 등..
   변수 : __로 시작

2. 표준라이브러리 => import를 사용
   (os, sys,glob,time,random)

3. 파이선 제공 라이브러리 => import 사용
   설치디렉토리\Lib
   수만가지... 못하는게 없을 정도...

4. 써드파티라이브러리 => 설치 후 import 사용
   => 라이브러리 설치(pip install 라이브러리)



<< 유지, 보수를 용이하게 하는 설계기법>> 
1. Open : 기능 확장
2. Close : 기존 소스는 가능하면 소스는 수정

C언어에서는 함수포인터를 활용
객체지향에서는 오버라이딩(상속)을 활용, Goff 패턴
파이선에서는 ???? => 람다를 활용


<< 라이브러리 작성 및 활용 >>
compile python => pyc
python dll => pyd

python -m py_compile xxx.py 
  ==> xxx.pyc가 생성됨
  ==> 컴파일된 모듈을 사용하면 속도가 빠름.

라이브러리 활용 : import xxx
  - workspace에 xxx.


<< python path에 추가하는 방법>>

1. 소스상에서 python path를 업데이트 ==> sys.path.append(..)를 활용
2. 글로벌 path에 추가 
     유닉스 : export PYTHONPATH=$PYTHONPATH:/home/my/mylib
     윈도우 : 환경변수를 업데이트
              setx PYTHONPATH %PYTHONPATH%;C:\DevPy\workspace\git\pyTest\mylib

3. 개발환경 상에서 환경 변수 업데이트 
   이클립스 >> 
       window->preference->PyDev->Interpreters->Python Interpreter
       라이브러리 탭에서 New Folder를 클릭해서 라이브러리 폴더 추가

