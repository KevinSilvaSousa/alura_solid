from src.domain.entities.produto import Produto
from typing import List
import uuid
from enum import Enum, auto

class CartStatus(Enum):
    ATIVO = auto()
    FINALIZADO = auto()
    EXPIRADO = auto()


class Cart:

    def __init__ (self, products,  cart_id: str):
        self._products = products
        self._cart_id = cart_id
        self._status = CartStatus.ATIVO

    def get_id(self):
        if not self._cart_id:
            self._cart_id = uuid.uuid4()
        return self._cart_id
    
    def add_novo_produto(self, produto:Produto):
        self._products.append(produto)

    def remover_produto(self,produto: Produto):
        self._products.remove(produto)

    def switch(self, new_status):
        self._status = new_status
        return self._status
    
    def get_status(self):
        return self._status
    
    def _cal_subtotal(self):
        prices = [product.get_price() for product in self._products 
                  if product.is_available() is True
                  ]
        return sum(prices)
    
    def get_subtotal(self):
        return self._cal_subtotal()