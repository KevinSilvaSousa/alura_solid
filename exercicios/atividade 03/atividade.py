from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass


class Retangulo(Forma):
    def __init__ (self, largura: float, altura: float):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura
    

class Quadrado(Forma):
    def __init__ (self, lado: float):
        self.lado = lado

    
    def area(self): 
        return self.lado * self.lado
    

class Triangulo(Forma):
    def __init__ (self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura)
        
