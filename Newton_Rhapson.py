from Function import *

def newton_rhapson(aa, bb, cc):

    func = Functions(aa, bb, cc)
    x = float(input("Masukkan nilai pendekatan awal: "))
    error = float(input("Masukkan error: "))
    n = int(input("Masukkan banyak iterasi: "))

    print("\nLoop\tx\tf(x)")

    for i in range(0, n):
        print("%d\t\t%.3f\t%.3f" % (i, x, func.fx(x)))
        if abs(func.fx(x)) <= error:
            break
        x = x - (func.fx(x) / func.turunan(x))

    return x