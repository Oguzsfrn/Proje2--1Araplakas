import re, json, ast

def menu():
    print("╔═════════════════════╗")
    print("║  ARAÇ PLAKA UYGULAMASI ║")
    print("║                     ║")
    print("║  1-Plaka ekle       ║")
    print("║  2-Listele          ║")
    print("║  3-Ara              ║")
    print("║  4-Düzelt           ║")
    print("║  5-Sil              ║")
    print("║  6-Çıkış            ║")
    print("║                     ║")
    print("║  Seçiminiz nedir?   ║")
    print("╚═════════════════════╝")
    # 201 ╔ 187 ╗ 200 ╚  # 188 ╝

    secim = input("")
    if secim == "1":
        plakaEkle()
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
    elif secim == "6":
        print("Çıkış yapılıyor...")
        exit()
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")
        menu()

def listele():
    try:
        with open('plakalar.json', 'r', encoding='utf-8') as file:
            plakalar = json.load(file)
            for arac in plakalar:
                print(f"Plaka: {arac['plaka']}, Sahibi: {arac['sahibi']}")
    except FileNotFoundError:
        print("Kayıtlı araç yok.")

def plakaEkle():
    plaka = input("Plaka: ")
    sahibi = input("Sahibi: ")
    yeni_arac = {"plaka": plaka, "sahibi": sahibi}
    
    try:
        with open('plakalar.json', 'r+', encoding='utf-8') as file:
            plakalar = json.load(file)
            plakalar.append(yeni_arac)
            file.seek(0)
            json.dump(plakalar, file, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        with open('plakalar.json', 'w', encoding='utf-8') as file:
            json.dump([yeni_arac], file, ensure_ascii=False, indent=4)

def ara():
    aranan = input("Aramak istediğiniz plaka: ")
    try:
        with open('plakalar.json', 'r', encoding='utf-8') as file:
            plakalar = json.load(file)
            for arac in plakalar:
                if arac['plaka'] == aranan:
                    print(f"Plaka: {arac['plaka']}, Sahibi: {arac['sahibi']}")
                    return
            print("Araç bulunamadı.")
    except FileNotFoundError:
        print("Kayıtlı araç yok.")

def duzelt():
    aranan = input("Düzeltmek istediğiniz plaka: ")
    try:
        with open('plakalar.json', 'r+', encoding='utf-8') as file:
            plakalar = json.load(file)
            for arac in plakalar:
                if arac['plaka'] == aranan:
                    yeni_plaka = input("Yeni plaka: ")
                    yeni_sahibi = input("Yeni sahibi: ")
                    arac['plaka'] = yeni_plaka
                    arac['sahibi'] = yeni_sahibi
                    file.seek(0)
                    json.dump(plakalar, file, ensure_ascii=False, indent=4)
                    print("Araç bilgileri güncellendi.")
                    return
            print("Araç bulunamadı.")
    except FileNotFoundError:
        print("Kayıtlı araç yok.")

def sil():
    aranan = input("Silmek istediğiniz plaka: ")
    try:
        with open('plakalar.json', 'r+', encoding='utf-8') as file:
            plakalar = json.load(file)
            for arac in plakalar:
                if arac['plaka'] == aranan:
                    plakalar.remove(arac)
                    file.seek(0)
                    file.truncate()
                    json.dump(plakalar, file, ensure_ascii=False, indent=4)
                    print("Araç silindi.")
                    return
            print("Araç bulunamadı.")
    except FileNotFoundError:
        print("Kayıtlı araç yok.")

if __name__ == "__main__":
    menu()