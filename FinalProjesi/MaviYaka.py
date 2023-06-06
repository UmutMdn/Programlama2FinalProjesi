from Calisan import Calisan
class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__yipranma_payi = yipranma_payi
        self.__zamOnerisi = 0
        self.__yeniMaas = 0

    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self):
        try:
            if self.get_tecrube() < 2:
                self.__zamOnerisi = self.__yipranma_payi * 10
                self.__yeniMaas = self.get_maas() + self.__zamOnerisi
                self.set_maas(self.__yeniMaas)
            elif 2 <= self.get_tecrube() <= 4 and self.get_maas() < 15000:
                 self.__zamOnerisi = (self.get_maas() % self.get_tecrube() / 2) + (self.__yipranma_payi * 10)
                 self.__yeniMaas =  self.get_maas() + self.__zamOnerisi
                 self.set_maas(self.__yeniMaas)
            elif self.get_tecrube() > 4 and self.get_maas() < 25000:
                self.__zamOnerisi = (self.get_maas() % self.get_tecrube() / 3) + (self.__yipranma_payi * 10)
                self.__yeniMaas = self.get_maas() + self.__zamOnerisi
                self.set_maas(self.__yeniMaas)
            else:
                self.set_maas(self.get_maas())

        except Exception as e:
            print("Hata:", e)

    def __str__(self):
        return f"{super().__str__()}, Tecrübe: {self.get_tecrube()}, Yeni Maaş: {self.get_maas()}"
