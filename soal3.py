# Soal 3: Deret Bilangan dan Penjumlahan
n = int(input("Masukkan n: "))

print("Deret:", end=" ")
for i in range(1, n+1):
    print(i, end=" ")
print()

jumlah_semua = sum(range(1, n+1))

jumlah_genap = 0
for i in range(1, n+1):
    if i % 2 == 0:
        jumlah_genap += i

print(f"Jumlah semua: {jumlah_semua}")
print(f"Jumlah genap: {jumlah_genap}")