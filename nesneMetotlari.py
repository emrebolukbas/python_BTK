class Araba(): #sınıf
    def __init__(self,model,marka,renk): #metot
        self.model=model
        self.marka=marka
        self.renk=renk
    def aracBilgisi(self):
        print("markası:",self.marka)
        print("model:",self.model)
        print("renk:",self.renk)

Taksi=Araba(2020,'Fiat','Sarı') #nesne
Kamyon=Araba(2004,'Man','Siyah')
print('\nKamyon Bilgisi\n')
Kamyon.aracBilgisi()
print('\nTaksi Bilgisi\n')
Taksi.aracBilgisi()
