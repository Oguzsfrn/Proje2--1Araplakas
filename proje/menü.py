import re, json, ast

def menu():
    print("╔═════════════════════╗")
    print("║  REHBER UYGULAMASI  ║")
    print("║                     ║")
    print("║  1-Kişi ekle        ║")
    print("║  2-Listele          ║")
    print("║  3-Ara              ║")
    print("║  4-Düzelt           ║")
    print("║  5-Sil              ║")
    print("║                     ║")
    print("║  Seçimiz nedir?     ║")
    print("╚═════════════════════╝")
    # 201 ╔ 187 ╗ 200 ╚  # 188 ╝

    secim = input("")
    if secim == "1":
        kisiEkle()
        listele()
        menu()
    elif secim == "2":
        listele()
        menu()
    elif secim == "3":
        ara()
        menu()
    elif secim == "4":
        duzelt()
        listele()
        menu()
    elif secim == "5":
        sil()
        listele()
        menu()
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")
        menu()

def listele():
    try:
        with open('rehber.json', 'r', encoding='utf-8') as file:
            rehber = json.load(file)
            for kisi in rehber:
                print(f"Ad: {kisi['ad']}, Telefon: {kisi['telefon']}")
    except FileNotFoundError:
        print("Rehberde kayıtlı kimse yok.")

def kisiEkle():
    ad = input("Ad: ")
    telefon = input("Telefon: ")
    yeni_kisi = {"ad": ad, "telefon": telefon}
    
    try:
        with open('rehber.json', 'r+', encoding='utf-8') as file:
            rehber = json.load(file)
            rehber.append(yeni_kisi)
            file.seek(0)
            json.dump(rehber, file, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        with open('rehber.json', 'w', encoding='utf-8') as file:
            json.dump([yeni_kisi], file, ensure_ascii=False, indent=4)

def ara():
    aranan = input("Aramak istediğiniz kişinin adını girin: ")
    try:
        with open('rehber.json', 'r', encoding='utf-8') as file:
            rehber = json.load(file)
            for kisi in rehber:
                if kisi['ad'] == aranan:
                    print(f"Ad: {kisi['ad']}, Telefon: {kisi['telefon']}")
                    return
            print("Kişi bulunamadı.")
    except FileNotFoundError:
        print("Rehberde kayıtlı kimse yok.")

def duzelt():
    aranan = input("Düzeltmek istediğiniz kişinin adını girin: ")
    try:
        with open('rehber.json', 'r+', encoding='utf-8') as file:
            rehber = json.load(file)
            for kisi in rehber:
                if kisi['ad'] == aranan:
                    yeni_ad = input("Yeni ad: ")
                    yeni_telefon = input("Yeni telefon: ")
                    kisi['ad'] = yeni_ad
                    kisi['telefon'] = yeni_telefon
                    file.seek(0)
                    json.dump(rehber, file, ensure_ascii=False, indent=4)
                    print("Kişi bilgileri güncellendi.")
                    return
            print("Kişi bulunamadı.")
    except FileNotFoundError:
        print("Rehberde kayıtlı kimse yok.")

def sil():
    aranan = input("Silmek istediğiniz kişinin adını girin: ")
    try:
        with open('rehber.json', 'r+', encoding='utf-8') as file:
            rehber = json.load(file)
            for kisi in rehber:
                if kisi['ad'] == aranan:
                    rehber.remove(kisi)
                    file.seek(0)
                    file.truncate()
                    json.dump(rehber, file, ensure_ascii=False, indent=4)
                    print("Kişi silindi.")
                    return
            print("Kişi bulunamadı.")
    except FileNotFoundError:
        print("Rehberde kayıtlı kimse yok.")

if __name__ == "__main__":
    menu()