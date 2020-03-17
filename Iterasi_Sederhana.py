from Function import *

def iterasi_sederhana(aa, bb, cc):

    func = Functions(aa, bb, cc)
    tebakan = float(input("Masukkan tebakan: "))
    error = float(input("Masukkan error: "))
    i = 1

    print("\nLoop\tTebakan\tSelisih")

    while True:
        xinv = func.IS_funcinv(tebakan)
        selisih = tebakan - xinv
        print("%d\t\t%.3f\t%.3f" % (i, tebakan, selisih))
        if abs(selisih) <= error:
            return tebakan
        tebakan = xinv
        i+=1