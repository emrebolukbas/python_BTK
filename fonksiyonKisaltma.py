#def dolar(TL):
#   return(TL/26)

dolar=lambda TL: TL/18 #kısa içeriği fazla olmayan fonksiyonlarda kullanılır
                        # yukardaki ile aynı sonucu verir.
TL=int(input("Dönüştürmek istediğiniz Türk Lirası miktarını giriniz: "))
print(TL,"Türk Lirası ",dolar(TL)," Dolar")
