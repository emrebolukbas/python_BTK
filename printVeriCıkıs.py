Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
print ('x','y','z')
x y z
print ('x','y','z', sep='+')
x+y+z
input('Yaşınız:?')
Yaşınız:?5
'5'
int(input('Yaşınız:?' end='..='))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
int(input("Yaşınız:?" end='..='))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
int(input('Yaşınız:?' end=..=))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
input('Yaşınız:?' end='..=')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
input('Yaşınız:?')
Yaşınız:?5
'5'
input('Yaşınız:' end='..=')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
input('Yaşınız:' end:'..=')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> input('yaşınız:' end='..=')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> yas = input('Yaşınız =')
Yaşınız =10
>>> print(yas, end='...=')
10...=
>>> 10
10
>>> 20
20
>>> print('btk\nAkademi')
btk
Akademi
>>> print('btk\tAkademi')
btk	Akademi
>>> print('\')
...       
SyntaxError: incomplete input
>>> print('\\')
...       
\
>>> A = 5
...       
>>> print('A=',A)
...       
A= 5
>>> print("a={0}".format(A))
...       
a=5
>>> print(f"A={A}")
...       
A=5
>>> print ('A='str(A))
...       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print ('A='+str(A))
...       
A=5
