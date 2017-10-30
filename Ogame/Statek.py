from daneStatkow import *
class Statek:
    def __init__(self,param):
        idx = DaneStatkow.points.index(param)
        self.skrot=DaneStatkow.short[idx]
        self.nazwa=DaneStatkow.name[idx]
        self.p_s=DaneStatkow.points[idx]
        self.oslona=DaneStatkow.cover[idx]
        self.atak=DaneStatkow.attack[idx]
    
    
    def shoot(self,other_ship):
        pass
    
    def hit(self):
        pass
    
    def isDestroyed(self):
        pass
    
    def stats(self):
        pass