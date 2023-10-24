def ustel(a,b):
    if b==0:
        return 1
    else:
        return a*ustel(a,b-1) # 2üssü4 2*2*2*2 sonra 0 olacağı için if e girer *1
a=int(input("Tabanı giriniz: "))
b=int(input("Üssü giriniz: "))
print(a," üzeri ",b," = ",ustel(a,b))
