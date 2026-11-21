# Soal 5: Bilangan Prima dalam Rentang
bawah = int(input("Batas bawah: "))
atas = int(input("Batas atas: "))

prima_list = []

for angka in range(bawah, atas+1):
    if angka > 1:
        is_prima = True
        for j in range(2, int(angka**0.5) + 1):
            if angka % j == 0:
                is_prima = False
                break
        if is_prima:
            prima_list.append(angka)

print("Bilangan prima:", end=" ")
for p in prima_list:
    print(p, end=" ")
print()
print(f"Jumlah: {len(prima_list)}")