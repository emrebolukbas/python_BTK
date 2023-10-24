class Araba():
    def __init__(self,model,marka,renk): #metot
        self.model=model #selfden sonra 1.
        self.marka=marka #2.
        self.renk=renk   #3.


Taksi=Araba(2020,"Fiat",'Sarı') # nesne tanımlama
print(Taksi.model)
print(Taksi.marka)
print(Taksi.renk)
Taksi.model=2023
print("yükseltilen yeni model :",Taksi.model)
