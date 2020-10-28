# latihan class
"""
class BangunSegitiga:

    def __init__(self, a=None, b=None, c=None, t=None, d=None, e=None, f=None ):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.t = t 
        
    def getLuas(self):
        print("Luas Segitiga :", 0.5 * self.a * self.t)
        
    def getKeliling(self):
        print("Keliling Segitiga: ", self.a + self.b + self.c)
        
    def LuasPersegiP(self):
        print("Luas Persegi P :", self.d * self.e)
        
    def KelilingPesegiP(self):
        print("Keliling Persegi P :", self.d + self.f + self.e)


luas1 = BangunSegitiga(a=10, t=5)
luas1.getLuas()

keliling1 = BangunSegitiga(a=13, b=5, c=9)
keliling1.getKeliling()

luas2 = BangunSegitiga(d=15, e=10)
luas2.LuasPersegiP()        

keliling2 = BangunSegitiga(d=15, f=10, e=8)
keliling2.KelilingPesegiP()
print(self.record)
"""
class SaveData:

    def __init__(self):
        self.record = []
           
    def save(self, nama, jabatan):
        self.record.append({"nama": nama, "jabatan": jabatan})
        
        
    def getData(self):
        return self.record
                             

ListData = SaveData()

ListData.save("Darul ihsan", "General Manager")

ListData.save("Adela Dwi", "CEO mengookies")

print(ListData.getData())      
    
    
    
  
    
    
    
        