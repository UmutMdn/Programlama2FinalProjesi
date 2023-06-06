class Insan:
    def __init__(self, tcNo, ad, soyAd, yas, cinsiyet, uyruk):
        self.__tcNo = tcNo
        self.__ad = ad
        self.__soyAd = soyAd
        self.__yas = yas
        self.__cinsiyet = cinsiyet
        self.__uyruk = uyruk

    def get_tcNo(self):
        return self.__tcNo

    def set_tcNo(self, tc_no):
        self.__tcNo = tc_no

    def get_ad(self):
        return self.__ad

    def set_ad(self, ad):
        self.__ad = ad

    def get_soyAd(self):
        return self.__soyAd

    def set_soyAd(self, soyad):
        self.__soyAd = soyad

    def get_yas(self):
        return self.__yas

    def set_yas(self, yas):
        self.__yas = yas

    def get_cinsiyet(self):
        return self.__cinsiyet

    def set_cinsiyet(self, cinsiyet):
        self.__cinsiyet = cinsiyet

    def get_uyruk(self):
        return self.__uyruk

    def set_uyruk(self, uyruk):
        self.__uyruk = uyruk

    def __str__(self):
        return f"TC No: {self.__tcNo}Ad: {self.__ad}Soyad: {self.__soyAd}Yaş: {self.__yas}Cinsiyet: {self.__cinsiyet}Uyruk: {self.__uyruk}"
