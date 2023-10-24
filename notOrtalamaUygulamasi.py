Ort = 0
Y1 = int(input('1.Yazılı Notunuz ='))
Y2 = int(input('2.Yazılı Notunuz ='))
Ort = (Y1 + Y2)/2
Ort = int(Ort) # degiskene tanımladığımız icin float inte cevrilmiş oldu

print('Ortalamanız = ', int(Ort)) # int olarak yazdırır ama asılı degismez yukarda bölündüğü icin float yazar ayni islemi degiskene tanımlarsak floattan int e döner.
