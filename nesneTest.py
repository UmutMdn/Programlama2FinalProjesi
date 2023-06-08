import pandas as pd
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

try:
    # İnsan sınıfı için nesne oluşturma
    insan1 = Insan("11111111111", "Umut", "Madanoglu", 21, "Erkek", "Türk")
    insan2 = Insan("22222222222", "Baris", "Madanoglu", 18, "Erkek", "Türk")

    print("İnsan 1:")
    print(insan1)
    print("\nİnsan 2:")
    print(insan2)

    # İşsiz sınıfı için nesne oluşturma
    status1 = {"mavi yaka": 5, "beyaz yaka": 10, "yönetici": 3}
    issiz1 = Issiz("33333333333", "Kemal", "Baris", 40, "Erkek", "Türk", status1)
    issiz1.statu_bul()
    status2 = {"mavi yaka": 8, "beyaz yaka": 4, "yönetici": 0}
    issiz2 = Issiz("44444444444", "Yeliz", "Baris", 32, "Kadın", "Türk", status2)
    issiz2.statu_bul()
    status3 = {"mavi yaka": 2, "beyaz yaka": 5, "yönetici": 11}
    issiz3 = Issiz("55555555555", "Gorkem", "Karayel", 27, "Erkek", "Türk", status3)
    issiz3.statu_bul()

    print("\nİşsiz 1:")
    print(issiz1)
    print("\nİşsiz 2:")
    print(issiz2)
    print("\nİşsiz 3:")
    print(issiz3)

    # Çalışan sınıfı için nesne oluşturma
    calisan1 = Calisan("66666666666", "Derya", "Madanoglu", 42, "Kadın", "Türk", "Bankacılık", 17, 12754)
    calisan1.zam_hakki()
    calisan2 = Calisan("77777777777", "Seyfi", "Madanoglu", 40, "Erkek", "Türk", "Bilişim", 11, 20325)
    calisan2.zam_hakki()
    calisan3 = Calisan("88888888888", "Alperen", "Dilaver", 27, "Erkek", "Türk", "Pazarlama", 1, 10208)
    calisan3.zam_hakki()

    print("\nÇalışan 1:")
    print(calisan1)
    print("\nÇalışan 2:")
    print(calisan2)
    print("\nÇalışan 3:")
    print(calisan3)

    # MaviYaka sınıfı için nesne oluşturma
    mavi_yaka1 = MaviYaka("99999999999", "Engin", "Atakul", 35, "Erkek", "Türk", "Bankacılık", 4, 14500, 0.5)
    mavi_yaka1.zam_hakki()
    mavi_yaka2 = MaviYaka("10101010101", "Sude", "Baris", 28, "Kadın", "Türk", "Bilişim", 2, 8000, 0.2)
    mavi_yaka2.zam_hakki()
    mavi_yaka3 = MaviYaka("12121212121", "Baran", "Pacaci", 27, "Erkek", "Türk", "Pazarlama", 9, 20000, 0.7)
    mavi_yaka3.zam_hakki()

    print("\nMavi Yaka 1:")
    print(mavi_yaka1)
    print("\nMavi Yaka 2:")
    print(mavi_yaka2)
    print("\nMavi Yaka 3:")
    print(mavi_yaka3)

    # BeyazYaka sınıfı için nesne oluşturma
    beyaz_yaka1 = BeyazYaka("13131313131", "Erkan", "Ak", 35, "Erkek", "Türk", "Bankacılık", 4, 15000, 2000)
    beyaz_yaka1.zam_hakki()
    beyaz_yaka2 = BeyazYaka("14141414141", "Rabia", "Kahraman", 28, "Kadın", "Türk", "Bilişim", 2, 8000, 1000)
    beyaz_yaka2.zam_hakki()
    beyaz_yaka3 = BeyazYaka("15151515151", "Ertan", "Ak", 27, "Erkek", "Türk", "Pazarlama", 6, 20000, 2500)
    beyaz_yaka3.zam_hakki()

    print("\nBeyaz Yaka 1:")
    print(beyaz_yaka1)
    print("\nBeyaz Yaka 2:")
    print(beyaz_yaka2)
    print("\nBeyaz Yaka 3:")
    print(beyaz_yaka3)
    print()

except Exception as e:
    print("Hata:", e)