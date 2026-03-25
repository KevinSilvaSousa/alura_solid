from abc import ABC, abstractmethod

#abstração
class Desconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass

# Aplicações concretas

class DescontoAniversario(Desconto):
    def calcular(self, valor):
        return valor * 0.9 # 10% desconto
    

class DescontoFidelidade(Desconto):
    def calcular(self, valor):
        return valor * 0.85 # 15% desconto
    

class DescontoFeriado(Desconto):
    def calcular(self, valor):
        return valor * 0.8 # 20% desconto
    

# Função que aplica qualquer desconto
def aplicar_desconto(desconto: Desconto, valor):
    return desconto.calcular(valor)

# Uso

preco_produto = 100

desconto_aniversario = DescontoAniversario()
desconto_fidelidade = DescontoFidelidade()
desconto_feriado = DescontoFeriado()

print(aplicar_desconto(desconto_aniversario, preco_produto))
print(aplicar_desconto(desconto_fidelidade, preco_produto))
print(aplicar_desconto(desconto_feriado, preco_produto))