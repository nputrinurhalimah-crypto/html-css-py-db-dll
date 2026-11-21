# Soal 4: Pola Segitiga Bintang
n = int(input("Masukkan tinggi segitiga: "))

print("Segitiga normal:")
for i in range(1, n+1):
    print("*" * i)

print("\nSegitiga terbalik (tantangan tambahan):")
for i in range(n, 0, -1):
    print("*" * i)