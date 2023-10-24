L=[]
Toplam=0

for i in range(0,5):
    sayi=int(input("Sayı girin: "))
    L.append(sayi)
    Toplam+=sayi
    
print("En küçük sayı = " ,min(L))
print("En büyük sayı = " ,max(L))
print("En küçük sayı ve en büyük sayının toplamı = " ,min(L)+max(L))
print("Aritmetik ortalaması",Toplam/len(L)) #1 kullanım
print("\nArdışık kullanılan sayıda\nAynı sonucu verecektir Aritmetik ortalama",(min(L)+max(L))/2) #2 kullanım olarak da kullanılabilir
