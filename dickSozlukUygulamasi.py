gun=input("Türkçe gün adını girin :")
TrEn={'pazartesi':'monday','salı':'tuesday','çarşamba':'wednesday','perşembe':'thursday','cuma':'friday','cumartesi':'saturday','pazar':'sunday'}
print("ingilizcesi :", end=" ")
print(TrEn.get(gun,'Bu kelime sözlükte yok'))
