Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> S='PYTHON'
>>> S[:]
'PYTHON'
>>> S[3:]
'HON'
>>> S[:3]
'PYT'
>>> S[1:5]
'YTHO'
>>> S[1:-1]
'YTHO'
>>> S[1::2]
'YHN'
>>> S[1:6:3]
'YO'
>>> S[::-1] #TERSTEN YAZDIRIR
'NOHTYP'
>>> S[::-1]
'NOHTYP'
>>> S[1::]
'YTHON'
>>> S[:]
'PYTHON'
>>> S2=S[:3]+'T'+S[4:]
>>> print(S2)
PYTTON
