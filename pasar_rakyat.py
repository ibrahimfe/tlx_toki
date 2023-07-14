from math import gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

jumlah_pedagang = int(input())
frekuensi_kunjungan = []
for i in range(jumlah_pedagang):
    frekuensi_kunjungan.append(int(input()))

lcm_value = frekuensi_kunjungan[0]
for i in range(1, jumlah_pedagang):
    lcm_value = lcm(lcm_value, frekuensi_kunjungan[i])

print(lcm_value)