from datetime import datetime as date

class Title:
  global personels
  personels = []

  global header
  header = "{:<5}{:<15}{:<15}{:<13}{:<25}{:<20}{:<30}".format("NO","AD","SOYAD","TELEFON","ADRES","GÜNLÜK UCRET($)","işe Giriş Tarihi(yyyy-aa-gg)= ")

  def show_personels():
    for key,value in enumerate(personels):
      print("{:<5}{:<15}{:<15}{:<13}{:<25}{:<20}{:<40}".format(key+1, value["ad"], value["soyad"], value["telefon"], value["adres"], value["gunlukucret"], value["işe Giriş Tarihi(yyyy-aa-gg)= "]))
  
  def add_developer(ad, soyad, telefon, adres, gunlukucret, tarih):
    personels.append({"ad" : ad, "soyad": soyad, "telefon": telefon, "adres": adres, "gunlukucret": gunlukucret, "işe Giriş Tarihi(yyyy-aa-gg)= ": tarih})
    print("yazılımcı bilgileri eklendi..")  

  def devolopersearch(aranan_ad):
    return
    

  while True:

    print("::menü::")
    print("1-yazılımcı ekleme")
    print("2-yazılımcı listeleme")
    print("3-yazılımcı arama")
    print("4-yazılımcı güncelleme")
    print("5-yazılımcı silme")
    print("6-yazılımcı listesini gör")
    print("7-çıkış")
    print("8-yazılımcı maliyeti")
  
    secim = input("Seçiminiz =")

    if secim=="7":
      print("çıkılıyor..")
      break
    elif secim=="6":
      print(personels)
    elif secim=="1":
      add_developer(input("ad ="), input("soyad ="), input("telefon ="), input("adres ="), input("gunlukucret ($)="), input("işe Giriş Tarihi(yyyy-aa-gg)= "))

    #  ad=input("ad =")
    #  soyad=input("soyad =")
    #  telefon=input("telefon =")
    #  adres=input("adres =")
    #  gunlukucret=input("gunlukucret ($)=")
    #  giristarihi=input("işe giriş tarihi (yyyy/aa/gg) =")
    #  eklenecek_veri = {
    #    "ad":ad,
    #    "soyad":soyad,
    #    "telefon":telefon,
    #    "adres":adres,
    #    "gunlukucret":gunlukucret,
    #    "işe giriş tarihi":giristarihi
    #    }
    #  personel.append(eklenecek_veri)
    #  print("yazılımcı bilgileri eklendi..")

    elif secim=="2":
      print(header)
      show_personels()
      print("listeleme bitti..")

    elif secim=="3":
      aranan_ad=input("aramak istediğiniz yazılımcı adı =")
      adet = 0
      print(header)         
      for key,value in enumerate(personels):
            if aranan_ad==value["ad"]:
                print("{:<5}{:<15}{:<15}{:<13}{:<25}{:<20}{:<30}".format(key+1, value["ad"], value["soyad"], value["telefon"], value["adres"], value["gunlukucret"], value["işe Giriş Tarihi(yyyy-aa-gg)= "]))
                adet = (adet + 1)
      if adet==0:
        print("aradığınız yazılımcı kişisi bulunamadı...")

    elif secim=="4":
      aranan_ad=input("güncellemek istediğiniz yazılımcı adı =")
      adet = 0
      bulunanlar_sozluk={}
      print(header)
      for key,value in enumerate(personels):
        if aranan_ad==value["ad"]:
          show_personels()
          adet = (adet + 1)
          bulunanlar_sozluk[key]=key
      if adet==0:
        print("güncellemek istediğiniz yazılımcı kişi bulunamadı")
      else:
        sor=int(input("güncellemek istediğiniz yazılımcı no="))
        sor = (sor - 1)
        if sor in bulunanlar_sozluk:
          ad=input("yeni ad =")
          soyad=input("yeni soyad =")
          telefon=input("yeni telefon =")
          adres=input("yeni adres =")
          guncellenecek_veri = {
            "ad":ad,
            "soyad":soyad,
            "telefon":telefon,
            "adres":adres
          }
          personels[sor]=guncellenecek_veri
          print("değişiklikler eklendi..")
        else:
          print("hatalı yazılımcı no değeri girildi...")


    elif secim=="5":
      silinecek_ad=input("silmek istediğiniz yazılımcı adı =")
      adet = 0
      bulunanlar_sozluk={}
      print(header)
      for key,value in enumerate(personels):
        if silinecek_ad==value["ad"]:
          show_personels()
          adet = (adet + 1)
          bulunanlar_sozluk[key]=key
      if adet==0:
        print("silmek istediğiniz yazılımcı bulunamadı..")
      else:
        sor=int(input("silmek istediğiniz yazılımcı no="))
        sor = (sor - 1)
        if sor in bulunanlar_sozluk:
          del(personels[sor])
          print("yazılımcı kişisi silindi")
        else:
          print("hatalı yazılımcı no değeri girildi...")
    elif secim=="8":
      aranan_ad=input("aramak istediğiniz yazılımcı adı =")
      adet = 0
      kod = int(input("günlük yazılan kod satırı ="))
      gunlukucret = int(gunlukucret)
      gider = kod*gunlukucret
      print("{:<5}{:<15}{:<15}{:<15}{:<25}{:<25}".format("NO","AD","SOYAD","GÜNLÜK UCRET($)","işe Giriş Tarihi(yyyy-aa-gg)= ","TOTAL GİDER ($)"))
      for key,value in enumerate(personels):
        if aranan_ad==value["ad"]:
          print("{:<5}{:<15}{:<15}{:<15}{:<25}{:<25}".format(key+1, value["ad"], value["soyad"], value["gunlukucret"], value["işe Giriş Tarihi(yyyy-aa-gg)= "], gider))
          adet = (adet + 1)
      if adet==0:
        print("aradığınız yazılımcı kişisi bulunamadı...")