Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> Adres='Bahçelievler-İstanbul'
>>> Adres2='Kadıköy'+Adres[12:]
>>> print(Adres2)
Kadıköy-İstanbul
>>> print(Adres)
Bahçelievler-İstanbul
>>> Adres.replace('Bahçelievler','Bakırköy') #degistirmek istenilen eski,yeni değer gir
'Bakırköy-İstanbul'
>>> print(Adres)
Bahçelievler-İstanbul
>>> Adres=Adres.replace('Bahçelievler','Bakırköy')
>>> print(Adres)
Bakırköy-İstanbul
