
������
(��)����Ʈķ�۽�
ilhank@naver.com




������ ���� 1�ù� 


���̼� ����
1. eclipse
  - eclipse pydev �÷����μ�ġ (www.eclipse.org)
  - pythone 3.4.4 �ٿ�ε� �� ��ġ (www.python.org)
2. pycharm (�ڵ��ϼ�)
3. atom : ������, c, c++ �� ����

<< ���̼� ���̺귯�� ���� >>
1. built in => import������.
  (���̼� ����Ŭ����, �Լ�, ����)
   ����Ŭ���� => �ַ� ����ó��, �빮�ڷ� ����
   �Լ� : ����ȯ ��..
   ���� : __�� ����

2. ǥ�ض��̺귯�� => import�� ���
   (os, sys,glob,time,random)

3. ���̼� ���� ���̺귯�� => import ���
   ��ġ���丮\Lib
   ��������... ���ϴ°� ���� ����...

4. �����Ƽ���̺귯�� => ��ġ �� import ���
   => ���̺귯�� ��ġ(pip install ���̺귯��)



<< ����, ������ �����ϰ� �ϴ� ������>> 
1. Open : ��� Ȯ��
2. Close : ���� �ҽ��� �����ϸ� �ҽ��� ����

C������ �Լ������͸� Ȱ��
��ü���⿡���� �������̵�(���)�� Ȱ��, Goff ����
���̼������� ???? => ���ٸ� Ȱ��


<< ���̺귯�� �ۼ� �� Ȱ�� >>
compile python => pyc
python dll => pyd

python -m py_compile xxx.py 
  ==> xxx.pyc�� ������
  ==> �����ϵ� ����� ����ϸ� �ӵ��� ����.

���̺귯�� Ȱ�� : import xxx
  - workspace�� xxx.


<< python path�� �߰��ϴ� ���>>

1. �ҽ��󿡼� python path�� ������Ʈ ==> sys.path.append(..)�� Ȱ��
2. �۷ι� path�� �߰� 
     ���н� : export PYTHONPATH=$PYTHONPATH:/home/my/mylib
     ������ : ȯ�溯���� ������Ʈ
              setx PYTHONPATH %PYTHONPATH%;C:\DevPy\workspace\git\pyTest\mylib

3. ����ȯ�� �󿡼� ȯ�� ���� ������Ʈ 
   ��Ŭ���� >> 
       window->preference->PyDev->Interpreters->Python Interpreter
       ���̺귯�� �ǿ��� New Folder�� Ŭ���ؼ� ���̺귯�� ���� �߰�

