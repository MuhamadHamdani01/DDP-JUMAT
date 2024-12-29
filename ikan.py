from Animal import Animal
class Ikan(Animal):
    
    def __init__(self, nama, makanan, hidup, berkembang_biak,bernafas,habitat):
        super().__init__(nama,makanan,hidup,berkembang_biak,)
        self. bernafas = bernafas
        self.habitat = habitat
        
        
    def info_ikan(self):
        super().info_animal(),
        print("bernafas \t\t :", self. bernafas,
            "\nhabitat \t\t :", self.habitat
        )
ikan_paus= Ikan("paus","plankton","Air","Beranak","paru-paru","air laut")
ikan_mujair= Ikan("mujair","pelet","Air","Bertelur","insang","air tawar")
ikan_paus.info_ikan()
print("==============")
ikan_mujair.info_ikan()
