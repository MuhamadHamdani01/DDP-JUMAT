from Animal import Animal
class Burung(Animal):
    
    def __init__(self, nama, makanan, hidup, berkembang_biak, paruh,warna_bulu):
        super().__init__(nama,makanan,hidup,berkembang_biak,)
        self.paruh = paruh
        self.warna_bulu = warna_bulu
        
        
    def info_burung(self):
        super().info_animal(),
        print("Paruh \t\t\t :", self.paruh,
            "\nWarna Bulu \t\t :", self.warna_bulu
        )
burung_beo= Burung("Beo","Jagumg","Darat","Bertelur","melemgkung","warna warni")
burung_gagak= Burung("gagak","daging","Darat","Bertelur","lurus","hitam")
burung_gagak.info_burung()
print("=====================")
burung_beo.info_burung()
