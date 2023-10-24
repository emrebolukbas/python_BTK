masaNo=0
liste= ['ali','veli','hasan','miray','özge','bahar']
liste2= ['emre','mustafa','ayşe','fatma']
print(liste,"Bugün olan randevu listesi")
print(liste2,"Diğer günlerde olan randevu listesi")
isim=input('İsminiz Nedir : ')

if isim=='ali':
    masaNo=5
if isim=='veli':
    masaNo=7
if isim=='hasan':
    masaNo=9
if isim=='miray':
    masaNo=11
if isim=='özge':
    masaNo=13
if isim=='bahar':
    masaNo=15

if isim in liste:
    print (masaNo," Numaralı masada randevunuz var.")
    
elif isim in liste2:
    print ("Rezervasyonunuz bu akşam değildir.")

elif isim not in liste and isim not in liste: #isim liste1 ve liste2 de değilse (not in)
   print("Rezarvasyonunuz yoktur.") 
