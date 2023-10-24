print ("Çıkmak için 0 girin")

while True:                                 #sonsuz döngü çıkmak için
    D=int(input('Bir sayı giriniz: '))
    print("Bu sayının karesi= ",D*D)
    if(D==0):                               #if şartı gerçekleştiğinde break ile cıkar
        break
        
