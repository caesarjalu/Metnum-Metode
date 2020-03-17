from Function import *

def biseksi(aa, bb, cc):

    func = Functions(aa, bb, cc)
    a = float(input("Masukkan batas bawah: "))
    b = float(input("Masukkan batas atas: "))
    error = float(input("Masukkan error: "))
    i=1

    if (func.fx(a)*func.fx(b) > 0):
        print("\nDiantara batas bawah dan atas tidak ditemukan titik nol")
        return None

    print ("\nLoop\ta\t\tb\t\tc\t\tf(a)\tf(c)\tf(a)*f(c)\t|a-b|")

    while True:
        c = (a+b)/2
        print("%d\t\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t\t%.3f" % (i, a, b, c, func.fx(a), func.fx(c), func.fx(a)*func.fx(c), abs(a-b)))
        if abs(a-b) <= error:
            break
        elif (func.fx(a)*func.fx(c) == 0):
            break
        elif (func.fx(a)*func.fx(c) < 0):
            b = c
        else:
            a = c
        i+=1

    if abs(func.fx(a)) < abs (func.fx(b)):
        return a;
    else:
        return b;