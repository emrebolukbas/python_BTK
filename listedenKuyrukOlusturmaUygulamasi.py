L=[]

while True:
    isim=input("İsim giriniz = ")
    L.append(isim)
    if isim=="sıradaki":
        L.pop(-1)
        print(L.pop(0))
        
    if isim=="bitti":
        L.pop(-1)
        break
        
