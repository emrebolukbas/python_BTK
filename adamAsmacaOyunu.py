import random
Liste = ["python","print","random","while","choice"]
kelime = random.choice(Liste)
adam = [
        '''
    +----+
         |
         |
         |
         |
        ---''',
        '''
    +----+
    o    |
         |
         |
         |
        ---''',
        '''
    +----+
    o    |
    |    |
         |
         |
        ---''',
        '''
    +----+
    o    |
   /|    |
         |
         |
        ---''',
        '''
    +----+
    o    |
   /|\\   |
         |
         |
        ---''',
        '''
    +----+
    o    |
   /|\\   |
   /     |
         |
        ---''',
        '''
    +----+
    o    |
   /|\\   |
   / \\   |
         |
        ---'''

    ]
dogruHarf=[]
yanlisHarf=[]
hak=len(adam)

while hak > 0:
    out=""
    for h in kelime:
        if h in dogruHarf:
            out+=h
        else:
            out+=" _"
    if out == kelime:
        break
    print("Kelime :",out)
    print(adam[hak-1])
    girHarf=input()
    if girHarf in dogruHarf or girHarf in yanlisHarf:
        print(girHarf,"Zaten girildi")
    elif girHarf in kelime:
        dogruHarf.append(girHarf)
    else:
        print("Yanlış Harf..!\nKalan Hakkınız :",hak)
        hak-=1
        yanlisHarf.append(girHarf)
        
if hak!=0:
    print("Tebrikler...Kazandınız...Kelimeniz : ",kelime.capitalize())
else:
    print("Malesef...Kaybettiniz...Kelimeniz : ",kelime.capitalize(),"idi.")
