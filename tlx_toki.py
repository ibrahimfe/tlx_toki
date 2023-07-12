# Membaca anggota-anggota matriks A
a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
g, h, i = map(int, input().split())

# Melakukan transpose matriks
transposed_matrix = [[a, d, g], [b, e, h], [c, f, i]]

# Menampilkan anggota-anggota transpos matriks
for row in transposed_matrix:
    print(' '.join(map(str, row)))

