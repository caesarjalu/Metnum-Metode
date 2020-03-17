from Function import *

def secant(aa, bb, cc):

    func = Functions(aa, bb, cc)
    x0 = float(input("Masukkan x0: "))
    x1 = float(input("Masukkan x1: "))
    error = float(input("Masukkan error: "))
    n = int(input("Masukkan banyak iterasi: "))
    i = 0

    if (func.fx(x0)*func.fx(x1) > 0):
        print("\nDiantara x0 dan x1 tidak ditemukan titik nol")
        return None

    print("\ni\t\txi\t\tf(xi)")
    print("%d\t\t%.3f\t%.3f" % (i, x0, func.fx(x0)))

    for i in range(0, n):
        y0 = func.fx(x0)
        y1 = func.fx(x1)
        print("%d\t\t%.3f\t%.3f" % (i+1, x1, y1))
        if abs(y1) <= error:
            break
        x2 = func.Sct_nilx2(x0, x1, y0, y1)
        x0 = x1
        x1 = x2

    return x1
