import math

class Functions:
    def __init__(self, aa, bb, cc):
        self.aa = aa
        self.bb = bb
        self.cc = cc

    def fx(self, x):
        return self.aa*x**2 + self.bb*x + self.cc

    def RF_nilc(self, a, b, Fa, Fb):
        return ((Fb*a - Fa*b) / (Fb - Fa))

    def IS_funcinv(self, x):
        return math.sqrt((-1 * (self.bb * x + self.cc)) / self.aa)

    def turunan(self, x):
        return self.aa*2*x + self.bb

    def Sct_nilx2(self, x0, x1, y0, y1):
        return x1 - (y1 * ((x1 - x0) / (y1 - y0)))