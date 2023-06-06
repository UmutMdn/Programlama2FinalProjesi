from Calisan import Calisan
class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi
        self.__zamOnerisi = 0

    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    def zam_hakki(self):
        try:
            if self.get_tecrube() < 2:
                self.__zamOnerisi = self.__tesvik_primi
                self.set_maas(self.get_maas() + self.__zamOnerisi)
            elif 2 <= self.get_tecrube() <= 4 and self.get_maas() < 15000:
                self.__zamOnerisi = (self.get_maas() % self.get_tecrube()) * 5 + self.__tesvik_primi
                self.set_maas(self.get_maas() + self.__zamOnerisi)
            elif self.get_tecrube() > 4 and self.get_maas() < 25000:
                self.__zamOnerisi = (self.get_maas() % self.get_tecrube()) * 4 + self.__tesvik_primi
                self.set_maas(self.get_maas() + self.__zamOnerisi)
            else:
                self.set_maas(self.get_maas())

        except Exception as e:
            print("Hata:", e)

    def __str__(self):
        return f"{super().__str__()}, Tecrübe: {self.get_tecrube()}, Yeni Maaş: {self.get_maas()}"
