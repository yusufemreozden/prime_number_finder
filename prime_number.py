# ************************************************************************** #
#                                                                            #
#                                                                            #
#    Prime Number Finder                                                     #
#                                                                            #
#    By: Yusuf Emre OZDEN | <yusufemreozdenn@gmail.com>                      #
#                                                                            #                                            
#    https://GitHub.com/yusufemreozden                                       #
#    https://linkedIn.com/in/yusufemreozden                                  #
#    https://sites.google.com/view/yusufemreozden                            #
#                                                                            #
# ************************************************************************** #


def asal_sayilari_bul(baslangic, bitis):
    asal_sayilar = []

    for sayi in range(baslangic, bitis + 1):
        if sayi > 1:
            for i in range(2, int(sayi**0.5) + 1):
                if (sayi % i) == 0:
                    break
            else:
                asal_sayilar.append(sayi)

    return asal_sayilar

baslangic_sayisi = int(input("Başlangıç sayısını girin: "))
bitis_sayisi = int(input("Bitiş sayısını girin: "))

asal_sayilar = asal_sayilari_bul(baslangic_sayisi, bitis_sayisi)

print(f"{baslangic_sayisi} ile {bitis_sayisi} arasındaki asal sayılar (yazdığınız sayıların da asallığı kontrol edilmiştir): {asal_sayilar}")

# made by yusufemreozden