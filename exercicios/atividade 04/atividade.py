from abc import ABC, abstractmethod

class Ave(ABC):
    @abstractmethod
    def tipo(self):
        pass

class AveQueVoa(Ave):
    def voar(self):
        return "Esta ave pode voar"

class Pardal(AveQueVoa):
    pass

class Pinguim(Ave):
    def tipo(self):
        return "Esta ave não voa"

def mostrar_voo(ave: Ave):
    if isinstance(ave, AveQueVoa):
        print(ave.voar())
    else:
        print(ave.tipo())

pardal = Pardal()
pinguim = Pinguim()

mostrar_voo(pardal)   # Esta ave pode voar
mostrar_voo(pinguim)  # Esta ave não voa