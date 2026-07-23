import math

gecmis = []

print("=" * 45)
print("        MathLab Calculator")
print("=" * 45)


while True:

    print("\n----- MENÜ -----")
    print("1 - Toplama")
    print("2 - Çıkarma")
    print("3 - Çarpma")
    print("4 - Bölme")
    print("5 - Üs Alma")
    print("6 - Karekök")
    print("7 - Faktöriyel")
    print("8 - Sinüs")
    print("9 - Kosinüs")
    print("10 - Tanjant")
    print("11 - Logaritma")
    print("12 - Mutlak Değer")
    print("13 - İşlem Geçmişi")
    print("14 - Çıkış")


    secim = input("\nİşlem seçiniz: ")


    if secim == "1":

        a = float(input("Birinci sayı: "))
        b = float(input("İkinci sayı: "))

        sonuc = a + b

        print("Sonuç:", sonuc)

        gecmis.append(f"{a} + {b} = {sonuc}")

        print("KAYIT EKLENDİ")


    elif secim == "2":

        a = float(input("Birinci sayı: "))
        b = float(input("İkinci sayı: "))

        sonuc = a - b

        print("Sonuç:", sonuc)

        gecmis.append(f"{a} - {b} = {sonuc}")


    elif secim == "3":

        a = float(input("Birinci sayı: "))
        b = float(input("İkinci sayı: "))

        sonuc = a * b

        print("Sonuç:", sonuc)

        gecmis.append(f"{a} × {b} = {sonuc}")


    elif secim == "4":

        a = float(input("Birinci sayı: "))
        b = float(input("İkinci sayı: "))

        if b == 0:
            print("Sıfıra bölme yapılamaz!")

        else:
            sonuc = a / b

            print("Sonuç:", sonuc)

            gecmis.append(f"{a} / {b} = {sonuc}")


    elif secim == "5":

        a = float(input("Taban sayı: "))
        b = float(input("Üs değeri: "))

        sonuc = a ** b

        print("Sonuç:", sonuc)

        gecmis.append(f"{a}^{b} = {sonuc}")


    elif secim == "6":

        a = float(input("Sayı: "))

        if a < 0:
            print("Negatif sayının karekökü yoktur.")

        else:
            sonuc = math.sqrt(a)

            print("Sonuç:", sonuc)

            gecmis.append(f"√{a} = {sonuc}")


    elif secim == "7":

        a = int(input("Sayı: "))

        if a < 0:
            print("Negatif sayının faktöriyeli yoktur.")

        else:
            sonuc = math.factorial(a)

            print("Sonuç:", sonuc)

            gecmis.append(f"{a}! = {sonuc}")


    elif secim == "8":

        derece = float(input("Derece: "))

        sonuc = math.sin(math.radians(derece))

        print("Sonuç:", sonuc)

        gecmis.append(f"sin({derece}) = {sonuc}")


    elif secim == "9":

        derece = float(input("Derece: "))

        sonuc = math.cos(math.radians(derece))

        print("Sonuç:", sonuc)

        gecmis.append(f"cos({derece}) = {sonuc}")


    elif secim == "10":

        derece = float(input("Derece: "))

        sonuc = math.tan(math.radians(derece))

        print("Sonuç:", sonuc)

        gecmis.append(f"tan({derece}) = {sonuc}")


    elif secim == "11":

        a = float(input("Sayı: "))

        if a <= 0:
            print("Pozitif sayı giriniz.")

        else:
            sonuc = math.log(a)

            print("Sonuç:", sonuc)

            gecmis.append(f"log({a}) = {sonuc}")


    elif secim == "12":

        a = float(input("Sayı: "))

        sonuc = abs(a)

        print("Sonuç:", sonuc)

        gecmis.append(f"|{a}| = {sonuc}")


    elif secim == "13":

        if len(gecmis) == 0:

            print("\nHenüz işlem yapılmadı.")

        else:

            print("\n===== İŞLEM GEÇMİŞİ =====")

            for i, islem in enumerate(gecmis, 1):

                print(f"{i}. {islem}")


    elif secim == "14":

        print("MathLab Calculator kapatılıyor...")
        break


    else:

        print("Geçersiz seçim yaptınız!")
    
