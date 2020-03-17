from Function import *

def regula_falsi(aa, bb, cc):

    func = Functions(aa, bb, cc)
    a = float(input("Masukkan batas bawah: "))
    b = float(input("Masukkan batas atas: "))
    error = float(input("Masukkan error: "))
    n = int(input("Masukkan banyak iterasi: "))
    Fa = func.fx(a)
    Fb = func.fx(b)

    if (func.fx(a)*func.fx(b) > 0):
        print("\nDiantara batas bawah dan atas tidak ditemukan titik nol")
        return None

    print("\nLoop\ta\t\tb\t\tc\t\tf(a)\tf(c)\tf(a)*f(c)")

    for i in range(0, n):
        c = func.RF_nilc(a, b, Fa, Fb)
        Fc = func.fx(c)
        print("%d\t\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f" % (i+1, a, b, c, Fa, Fc, Fa * Fc))
        if abs(Fc) < error:
            break
        elif Fa*Fc < 0:
            b = c
            Fb = Fc
        else:
            a = c
            Fa = Fc

    return c