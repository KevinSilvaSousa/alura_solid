from abc import ABC, abstractmethod

class InterfaceImpressora(ABC):
    @abstractmethod
    def imprimir(self, documento: str):
        pass


class InterfaceDigitalizar(ABC):
    @abstractmethod
    def digitalizar(self, documento: str):
        pass


class InterfaceFax(ABC):
    @abstractmethod
    def fax(self, numero: str,  documento: str):
        pass


class ImpressoraAntiga(InterfaceImpressora):
    def imprimir(self, documento: str):
        print(f"imprimindo {documento}")


class MultiFuncional(InterfaceImpressora, InterfaceDigitalizar, InterfaceFax):
    def imprimir(self, documento: str):
        print(f"imprimindo: {documento}")


    def digitalizar(self, documento: str):
        print(f"Digitalizando: {documento}")


    def fax(self, numero: str,  documento: str):
        print(f"Fax: {numero} - {documento}")
