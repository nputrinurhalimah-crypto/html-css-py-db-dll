# Soal 1: Penentu Bilangan Ganjil/Genap dan Positif/Negatif
bilangan = int(input("Masukkan bilangan: "))

if bilangan == 0:
    print("Bilangan nol")
elif bilangan > 0:
    if bilangan % 2 == 0:
        print("Bilangan positif dan genap")
    else:
        print("Bilangan positif dan ganjil")
else: # bilangan < 0
    if bilangan % 2 == 0:
        print("Bilangan negatif dan genap")
    else:
        print("Bilangan negatif dan ganjil")