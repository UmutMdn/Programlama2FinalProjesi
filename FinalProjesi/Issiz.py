from Insan import Insan

class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, status):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__statuler = {"mavi yaka": status["mavi yaka"], "beyaz yaka": status["beyaz yaka"], "yönetici": status["yönetici"]}
        self.__enUygunStatu = ""

    def get_statuler(self):
        return self.__statuler

    def set_statuler(self, statuler):
        self.__statuler = statuler

    def get_en_uygun_statu(self):
        return self.__enUygunStatu

    def set_en_uygun_statu(self, enUygunStatu):
        self.__enUygunStatu = enUygunStatu

    def statu_bul(self):
        try:
            max_etki = 0
            en_uygun_statu = ""
            for statu, yil in self.__statuler.items():
                if statu == "mavi yaka":
                    etki = yil * 0.20
                elif statu == "beyaz yaka":
                    etki = yil * 0.35
                elif statu == "yönetici":
                    etki = yil * 0.45

                if etki > max_etki:
                    max_etki = etki
                    en_uygun_statu = statu
            self.__enUygunStatu = en_uygun_statu

        except Exception as e:
            print("Hata:", e)

    def __str__(self):
        return f"{super().__str__()}, En Uygun Statü: {self.__enUygunStatu}"