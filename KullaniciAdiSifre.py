k_Adi='admin'
sifre= 1234

user=input('Kullanıcı Adı :')
password=int(input('Şifre :'))

if k_Adi==user and sifre==password: #user=='admin' and password == '1234'
    print("Hoş Geldiniz")
else:
    print("Yetkisiz Giriş")
