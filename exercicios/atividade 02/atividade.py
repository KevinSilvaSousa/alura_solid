from abc import ABC, abstractmethod

class Frete(ABC):
    @abstractmethod
    def calcular(self, pedido):
        pass

class FreteNormal(Frete):
    def calcular(self, pedido):
        return 10
    
class FreteExpresso(Frete):
    def calcular(self, pedido):
        return 20

class FreteEconomico(Frete):
    def calcular(self, pedido):
        return 30
    
class CalculadoraFrete:
    def __init__(self, tipos_fretes: Frete):
        self.tipos_frete = tipos_fretes
   
    def calcular_total(self, pedido):
        return sum(f.calcular(pedido) for f in self.tipos_frete)
    