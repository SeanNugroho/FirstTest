#program perkalian matriks

ka = int(input("Masukkan banyak kolom pada matriks A : "))
ba = int(input("Masukkan banyak baris pada matriks A : "))
kb = int(input("Masukkan banyak kolom pada matriks B : "))
bb = int(input("Masukkan banyak baris pada matriks B : "))
a = [[0 for i in range(ka)]for j in range(ba)]
b = [[0 for i in range(kb)]for j in range(bb)]

for i in range(ba):
    for j in range(ka):
        a[i][j] = int(input("Masukkan elemen matriks A baris {} kolom {} : ".format(i+1,j+1)))

for i in range(bb):
    for j in range(kb):
        b[i][j] = int(input("Masukkan elemen matriks B baris {} kolom {} : ".format(i+1,j+1)))

print(a)
print(b)
 #3x3
if ka== bb:
    bm = ba
    k = kb
    m = [[0 for i in range(k)]for j in range(bm)]
    print(m)
    for c in range(ka):
        for i in range(bm):
            for j in range(k):
                m[i][j] += a[i][c]*b[c][j]
    print("hasil perkaliannya adalah :")
    for i in range(bm):
        for j in range(k):
            print(str(m[i][j]), end=" ")
        print("")
else:
    print("Matriks A harus memiliki jumlah kolom yang sama dengan jumlah baris pada matriks B")


