Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
L=[1,2,3,4,5,6,7,8,9]
L[4:]
[5, 6, 7, 8, 9]
L[0]
1
L[]
SyntaxError: incomplete input
L[:]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
L[2:4]
[3, 4]
L[0:4]
[1, 2, 3, 4]
L[::-1]
[9, 8, 7, 6, 5, 4, 3, 2, 1]
L[::2]
[1, 3, 5, 7, 9]
L[::3]
[1, 4, 7]
L[::-2]
[9, 7, 5, 3, 1]
listeIlkDort=L[0:4]
listeIlkDort
[1, 2, 3, 4]
listeSonDort=L[4:]
listeSonDort
[5, 6, 7, 8, 9]
>>> listeSonDort=LSD
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    listeSonDort=LSD
NameError: name 'LSD' is not defined
>>> listeSonDort==LSD
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    listeSonDort==LSD
NameError: name 'LSD' is not defined
>>> LSD=0
>>> listeSonDort=LSD
>>> LSD
0
>>> listeSonDort==LSD
True
>>> L[:]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> L[4:1]
[]
>>> L[5:]
[6, 7, 8, 9]
>>> LSD=L[5:]
>>> L[4:0]
[]
>>> L[0:4]
[1, 2, 3, 4]
>>> LID=L[0:4]
>>> L[4]
5
>>> LO=L[4]
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> LID
[1, 2, 3, 4]
>>> LSD
[6, 7, 8, 9]
>>> LO
5
