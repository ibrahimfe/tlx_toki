jumlah_angka = int(input())
arr_angka = []
for i in range(jumlah_angka):
    arr_angka.append(input())
for angka in arr_angka:
    print(int("".join(reversed(angka))))