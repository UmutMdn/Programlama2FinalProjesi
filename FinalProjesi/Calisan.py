from Insan import Insan

class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas
        self.__zamOrani = 0

    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = sektor

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    def get_zamOrani(self):
        return self.__zamOrani

    def set_zamOrani(self, zamOrani):
        self.__zamOrani = zamOrani

    def zam_hakki(self):
        try:
            if self.__tecrube < 2:
                self.__zamOrani = 0
            elif 2 <= self.__tecrube <= 4 and self.__maas < 15000:
                self.__zamOrani = self.__maas % self.__tecrube
            elif self.__tecrube > 4 and self.__maas < 25000:
                self.__zamOrani = (self.__maas % self.__tecrube) / 2
            else:
                self.__zamOrani = 0

            yeni_maas = self.__maas + self.__zamOrani
            if yeni_maas == self.__maas:
                return self.__maas
            else:
                self.__maas = yeni_maas
                return yeni_maas

        except Exception as e:
            print("Hata:", e)

    def __str__(self):
        return f"{super().__str__()}, Tecrübe: {self.__tecrube}, Yeni Maaş: {self.__maas}"



