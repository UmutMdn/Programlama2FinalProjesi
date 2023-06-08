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

    # DataFrame oluşturma
    data = {
        "nesne": ["Çalışan", "Çalışan", "Çalışan", "Mavi Yaka", "Mavi Yaka", "Mavi Yaka",
                  "Beyaz Yaka", "Beyaz Yaka", "Beyaz Yaka"],
        "tc_no": [calisan1.get_tcNo(), calisan2.get_tcNo(), calisan3.get_tcNo(), mavi_yaka1.get_tcNo(),
                  mavi_yaka2.get_tcNo(), mavi_yaka3.get_tcNo(),
                  beyaz_yaka1.get_tcNo(), beyaz_yaka2.get_tcNo(), beyaz_yaka3.get_tcNo()],
        "ad": [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(), mavi_yaka1.get_ad(), mavi_yaka2.get_ad(),
               mavi_yaka3.get_ad(),
               beyaz_yaka1.get_ad(), beyaz_yaka2.get_ad(), beyaz_yaka3.get_ad()],
        "soyad": [calisan1.get_soyAd(), calisan2.get_soyAd(), calisan3.get_soyAd(), mavi_yaka1.get_soyAd(),
                  mavi_yaka2.get_soyAd(), mavi_yaka3.get_soyAd(),
                  beyaz_yaka1.get_soyAd(), beyaz_yaka2.get_soyAd(), beyaz_yaka3.get_soyAd()],
        "yas": [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(), mavi_yaka1.get_yas(), mavi_yaka2.get_yas(),
                mavi_yaka3.get_yas(),
                beyaz_yaka1.get_yas(), beyaz_yaka2.get_yas(), beyaz_yaka3.get_yas()],
        "cinsiyet": [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(),
                     mavi_yaka1.get_cinsiyet(), mavi_yaka2.get_cinsiyet(),
                     mavi_yaka3.get_cinsiyet(), beyaz_yaka1.get_cinsiyet(), beyaz_yaka2.get_cinsiyet(),
                     beyaz_yaka3.get_cinsiyet()],
        "uyruk": [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(), mavi_yaka1.get_uyruk(),
                  mavi_yaka2.get_uyruk(), mavi_yaka3.get_uyruk(),
                  beyaz_yaka1.get_uyruk(), beyaz_yaka2.get_uyruk(), beyaz_yaka3.get_uyruk()],
        "sektor": [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(), mavi_yaka1.get_sektor(),
                   mavi_yaka2.get_sektor(),
                   mavi_yaka3.get_sektor(), beyaz_yaka1.get_sektor(), beyaz_yaka2.get_sektor(),
                   beyaz_yaka3.get_sektor()],
        "tecrube": [calisan1.get_tecrube(), calisan2.get_tecrube(), calisan3.get_tecrube(), mavi_yaka1.get_tecrube(),
                    mavi_yaka2.get_tecrube(),
                    mavi_yaka3.get_tecrube(), beyaz_yaka1.get_tecrube(), beyaz_yaka2.get_tecrube(),
                    beyaz_yaka3.get_tecrube()],
        "maas": [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), mavi_yaka1.get_maas(),
                 mavi_yaka2.get_maas(), mavi_yaka3.get_maas(),
                 beyaz_yaka1.get_maas(), beyaz_yaka2.get_maas(), beyaz_yaka3.get_maas()],
        "yipranma_payi": [0, 0, 0, mavi_yaka1.get_yipranma_payi(), mavi_yaka2.get_yipranma_payi(),
                          mavi_yaka3.get_yipranma_payi(),
                          0, 0, 0],
        "tesvik_primi": [0, 0, 0, 0, 0, 0, beyaz_yaka1.get_tesvik_primi(), beyaz_yaka2.get_tesvik_primi(),
                         beyaz_yaka3.get_tesvik_primi()],

    }

    # DataFrame oluşturma
    df = pd.DataFrame(data)

    # Değişken değerlerini 0 atama
    df.fillna(0, inplace=True)

    # Çalışan, mavi yaka ve beyaz yaka için gruplandırma ve ortalamaları
    grouped = df.groupby('nesne')
    ort_tecrube = grouped['tecrube'].mean()
    ort_yeni_maaş = grouped['maas'].mean()
    print("Mavi Yaka Ortalama Tecrübe:", ort_tecrube['Mavi Yaka'])
    print("Mavi Yaka Ortalama Yeni Maaş:", ort_yeni_maaş['Mavi Yaka'])
    print("Beyaz Yaka Ortalama Tecrübe:", ort_tecrube['Beyaz Yaka'])
    print("Beyaz Yaka Ortalama Yeni Maaş:", ort_yeni_maaş['Beyaz Yaka'])
    print()

    # Maaşı 15000TL üzerinde olanların toplam sayısı
    maas_ustu_15000 = df[df['maas'] > 15000].shape[0]
    print("Maaşı 15000 TL üzerinde olanların toplam sayısı:", maas_ustu_15000)
    print()

    # Maaşa göre DataFrame'i küçükten büyüğe sıralama
    df_sirali = df.sort_values(by='maas')
    print("Maaşa göre sıralanmış DataFrame:")
    print(df_sirali)
    print()

    # Tecrübesi 3 seneden fazla olan Beyaz yakalıları bulma
    filtre2 = (df['nesne'] == 'Beyaz Yaka') & (df['tecrube'] > 3)
    beyaz_yakalar = df[filtre2]
    print("Tecrübesi 3 seneden fazla olan Beyaz yakalılar:")
    print(beyaz_yakalar)
    print()

    # Yeni maaşı 10000 TL üzerinde olanlar için 2-5 satır aralığındaki verileri seçme
    filtre2 = (df['maas'] > 10000)
    satirlar = df[filtre2].iloc[2:5][['tc_no', 'maas']]
    print("Yeni maaşı 10000 TL üzerinde olanlar için 2-5 satır aralığındaki veriler:")
    print(satirlar)
    print()

    # Yeni DataFrame oluşturma (ad, soyad, sektör ve yeni_maaş sütunlarını içerir)
    yeni_df = df.loc[:, ['ad', 'soyad', 'sektor', 'maas']]
    print("Yeni DataFrame:")
    print(yeni_df)
    print()

except Exception as e:
    print("Hata:", e)


