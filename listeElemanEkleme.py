Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> L=[1,2,3]
>>> L
[1, 2, 3]
>>> L.append(4)
>>> L
[1, 2, 3, 4]
>>> L.append(5,6)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    L.append(5,6)
TypeError: list.append() takes exactly one argument (2 given)
>>> L
[1, 2, 3, 4]
>>> L.append(5)
>>> L
[1, 2, 3, 4, 5]
>>> L.insert(3,0)
>>> L
[1, 2, 3, 0, 4, 5]
>>> L.insert(-1,0)
>>> L
[1, 2, 3, 0, 4, 0, 5]
