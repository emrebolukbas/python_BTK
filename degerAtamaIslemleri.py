Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
Cep=0
Cep=Cep+10
print(Cep)
10

Cep+=10
print(Cep)
20
Cep-=10
print(Cep)
SyntaxError: multiple statements found while compiling a single statement
Cep-=10
print(Cep)
10
Cep/=2
print(Cep)
5.0
Cep=10
Cep//=2
print(Cep)
5
Cep%=2
print(Cep)
1
i=10
i+=j+8
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    i+=j+8
NameError: name 'j' is not defined
>>> i=i+j+8
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    i=i+j+8
NameError: name 'j' is not defined
>>> j=5
>>> 
>>> 
>>> i+=j+8
>>> print(i)
23
>>> A=A+B
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    A=A+B
NameError: name 'A' is not defined
>>> x=x-y/2
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    x=x-y/2
NameError: name 'x' is not defined
>>> A=5
>>> B=3
>>> A+=B
>>> print(A)
8
>>> x=10
>>> y=4
>>> x+=-y/2
>>> print(x)
8.0
>>> x//=1
>>> print(x)
8.0
>>> x//=2
>>> print(x)
4.0
