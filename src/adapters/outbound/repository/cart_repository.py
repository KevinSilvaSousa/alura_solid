from src.domain.ports.outbound.repository_protocol import (
    GetRepositoryProtocol, DeleteRepositoryProtocol, InsertRepositoryProtocol
)


LIST_CART = []


class CartRepository(GetRepositoryProtocol, 
                     DeleteRepositoryProtocol,
                     InsertRepositoryProtocol):
    def __init__(self):
        self._carts = LIST_CART
    
    def delete(self, item_id: str):
        result = [unique for unique in self._carts if unique ["cart_id"] == item_id] 
        self._carts.remove(result)
    
    
    def read(self, item_id: str):
        result = [unique for unique in self._carts if unique ["cart_id"] == item_id] 
        return result

    def save(self, data: dict):
        self._carts.append(data)


