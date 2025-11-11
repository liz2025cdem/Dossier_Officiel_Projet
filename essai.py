from math import pi


class Cercle:




    def __init__(self, rayon,):
        self.rayon = rayon

    def calcul_circonference(self):
        print(2*pi*self.rayon)

    def calcul_aire(self):
        print(self.rayon*pi*self.rayon)



m = Cercle(3)
m.calcul_circonference()
m.calcul_aire()



class Héro:


