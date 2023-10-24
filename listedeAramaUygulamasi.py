L=[12,23,34,56,78,99]
print("Liste",L)
deger=int(input("Sayı giriniz : "))
if deger in L:
    indis=L.index(deger)
    print("Aranan",indis,"indis değerinde")
else:
    print("Aranan değer bulunamadı!")
