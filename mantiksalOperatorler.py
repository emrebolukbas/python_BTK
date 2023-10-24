Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> (3<5)and(4<7)
True
>>> (3<5)and(4<7)and(2<5)
True
>>> (3<5)and(4<7)and(2>5)
False
>>> (4<5)or(3<6)
True
>>> (4<5)or(7<6)
True
>>> (4<5)or(7<6)or(4<2)
True
>>> (5=<4)or(7<6)or(4<2)
SyntaxError: invalid syntax
>>> (5<=4)or(7<6)or(4<2)
False
>>> not(5<=4)or(7<6)or(4<2)
True
>>> 3>5
False
>>> not(3>5)
True
