from Tabel import *
from Biseksi import *
from Regula_Falsi import *
from Iterasi_Sederhana import *
from Newton_Rhapson import *
from Secant import *

print("ax^2 + bx + c\n")
aa = float(input("masukan nilai a: "))
bb = float(input("masukan nilai b: "))
cc = float(input("masukan nilai c: "))

print(f"\nfungsi: ({aa})x^2 + ({bb})x + ({cc})\n")

print("Menu Metode Penyelesaian:\n"
      "1. Metode table\n"
      "2. Metode biseksi\n"
      "3. Metode regula falsi\n"
      "4. Metode iterasi sederhana\n"
      "5. Metode Newton Raphson\n"
      "6. Metode Secant\n")

pilihan_metode = int(input("masukan pilihan: "))

print("")

if pilihan_metode == 1:
    hasil = tabel(aa, bb, cc)
elif pilihan_metode == 2:
    hasil = biseksi (aa, bb, cc)
elif pilihan_metode == 3:
    hasil = regula_falsi(aa, bb, cc)
elif pilihan_metode == 4:
    hasil = iterasi_sederhana(aa, bb, cc)
elif pilihan_metode == 5:
    hasil = newton_rhapson(aa, bb, cc)
elif pilihan_metode == 6:
    hasil = secant(aa, bb, cc)


print(f"\nHasil = {hasil}")