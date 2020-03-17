from Function import *

def tabel(aa, bb, cc):

    func = Functions(aa, bb, cc)
    a = float(input("Masukkan batas bawah: "))
    b = float(input("Masukkan batas atas: "))
    n = int(input("Masukkan banyak cacahan: "))
    h = (b - a) / n

    print ("\nLoop\tx1\t\tx2\t\tf(x1)\tf(x2)\tf(x1)*f(x2)")

    for i in range(0, n):
        x1 = a + i*h
        x2 = a + (i+1)*h
        y1 = func.fx(x1)
        y2 = func.fx(x2)
        print("%d\t\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f" % (i+1, x1, x2, y1, y2, y1*y2))
        if y1*y2 <= 0:
            break

    if (i+1) == n:
        print("\nHasil tidak ditemukan")
    else:
        if abs(y1) < abs (y2):
            return x1
        else:
            return x2