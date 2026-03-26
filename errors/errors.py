class ErrorNegocio(Exception):
    pass


class ProdutoSemEstoqueError(ErrorNegocio):
    def __init__ (self, produto, estoque_disponivel):
        super().__init__(
            f"Produto {produto} sem estoque"
        )

    def main():
        raise ProdutoSemEstoqueError("batatinhas", 0)
    

class CNPJInvalidError(ValueError):
    def __init__ (self, cnpj):
        super(). __init__(
            f"O cnpg está correto: {cnpj}"
        )


try:
    pass
except CNPJInvalidError:
    pass