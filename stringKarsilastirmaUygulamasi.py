sifre="1234"
Kullanici='emre'

K_giris=input('Kullanıcı adını giriniz: ')
if K_giris==Kullanici:   
    S_giris=input('Şifrenizi giriniz: ')
    if S_giris == sifre: 
        print('Hoş geldiniz :)')
    else:
        print('Şifre Hatalı')
else:
    print('Kullanıcı Adı Hatalı')
        
