import random
sayi=random.randint(1,10)
tahmin=int(input("Tahmin Et :"))
skor=100
while True:
    if sayi==tahmin:
        print("Kazandınız :)\nTebrikler Skorunuz :",skor)
        break
    else:
        print("Olmadı :(\nSkorunuz:",skor)
        skor-=10
        tahmin=int(input("Tahmin Et:"))
