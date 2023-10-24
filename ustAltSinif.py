import datetime
class araba:                #üstSınıf
    def __init__(self,model,fiyat):
        self.model=model
        self.fiyat=fiyat
    def arabaBilgi(self):
        print("Araba Modeli:",self.model,"\nAraba Fiyatı:",self.fiyat)
        return(datetime.datetime.now())

class kamyon(araba):        #altSınıf
    def __init__(self,model,fiyat,renk):
        araba.__init__(self,model,fiyat)
        self.renk=renk

k1=kamyon(2020,120000,"Kırmızı")
k1.arabaBilgi()
