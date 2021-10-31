print  ("@@@@@    @     @@@@  @ ")
print  ("@   @  @   @   @     @ ")
print  ("@@@@@  @ @ @   @@@@  @ ")
print  ("@ @    @   @   @     @ ")
print  ("@   @  @   @   @     @ ")
kok1=int(input("masukan total belanjaan= "))
kok2=int(input("masukan jumlah uang mu = "))
Kembalian= (kok2-kok1)
print("Uang Kembalian = ", "Rp.",Kembalian)
uang_pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000,]
jumlah_pecahan = {}
sisa = Kembalian
for pecahan in uang_pecahan:
    if sisa < pecahan:
        continue
    banyak_pecahan = int(sisa / pecahan)
    sisa = sisa - ( pecahan * banyak_pecahan )
    print('uang  Rp{} sebanyak: {} lembar'.format(pecahan, banyak_pecahan))