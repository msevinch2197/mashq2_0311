class Tortburchak:
    def __init__(self, uzunlik, kenglik):
        self.uzunlik = uzunlik
        self.kenglik = kenglik

    def yuza(self):
        return self.uzunlik * self.kenglik

    def perimetr(self):
        return 2 * (self.uzunlik + self.kenglik)

# Misol
tortburchak = Tortburchak(8, 5)
print("Yuza:", tortburchak.yuza())
print("Perimetr:", tortburchak.perimetr())
