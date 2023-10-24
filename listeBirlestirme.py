Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> L1=[1,2,3,4]
>>> L2=[5,6,7,8]
>>> L3=L1+L2
>>> print(L3)
[1, 2, 3, 4, 5, 6, 7, 8]
>>> print(L1+L2)
[1, 2, 3, 4, 5, 6, 7, 8]
>>> L1.expend(L2)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    L1.expend(L2)
AttributeError: 'list' object has no attribute 'expend'. Did you mean: 'extend'?
>>> L1.extend(L2)
>>> print(L1)
[1, 2, 3, 4, 5, 6, 7, 8]
>>> print(L2)
[5, 6, 7, 8]
>>> L2.extend(L1)
>>> print(L2)
[5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
>>> L2.extend(L2)
>>> print(L2)
[5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
