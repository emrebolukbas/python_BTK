Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> (int) (9.6)
9
>>> (int) (4.5)
4
>>> float (4)
4.0
>>> int (5.43)
5
>>> str(4)
'4'
>>> str(4)+str(4)
'44'
>>> 4+4
8
>>> int(10.45) #10.45 kesirli sayısını int veri tipine dönüştür
10
>>> float(59) #59 int veri tipini float'a dönüştür
59.0
>>> B=40
>>> C=str(B)+'5'
>>> print(C)
405
>>> A=5
>>> B=A+'5'
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    B=A+'5'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(B)
40
>>> C=A+'10'
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    C=A+'10'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> C=str(A)+'10'
>>> print(C)
510
