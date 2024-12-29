from Animal import Animal
class ular(Animal):
    
    def __init__(self, nama, makanan, hidup, berkembang_biak,corak,ukuran):
        super().__init__(nama,makanan,hidup,berkembang_biak,)
        self. corak = corak
        self.ukuran = ukuran
            
        
    def info_ular(self):
        super().info_animal(),
        print("corak \t\t\t :", self.corak,
            "\nukuran \t\t\t :", self.ukuran
        )
ular_piton= ular("piton","daging","darat","Bertelur","abu-abu","besar")
ular_welang= ular("welang","daging","darat","Bertelur","hitam-kuning","kecil")
ular_piton.info_ular()
print("==============")
ular_welang.info_ular()
