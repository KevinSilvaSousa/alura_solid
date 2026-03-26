from abc import ABC, abstractmethod

class MotoristaComum(ABC):
    @abstractmethod
    def aceitar_corrida_individuais(self, destino: str) -> None:
        pass

class CaronaCompartilhada(ABC):
    @abstractmethod
    def aceitar_carona_compartilhada(self, destino: str, passageiros: list) -> None:
        pass


class TransportarCarga(ABC):
    @abstractmethod
    def transportar_carga(self, peso: float) -> None:
        pass


class IMotoristaComum(MotoristaComum ):
    def aceitar_corrida_individuais(self, destino: str) -> None:
        print(f"O seu destino individual é: {destino}")


class ICaronaCompartilhada(CaronaCompartilhada):
    def aceitar_carona_compartilhada(self, destino: str) -> None:
        print(f"O destino compartilhado é: {destino}")


class ITransportarCarga(TransportarCarga):
    def transportar_carga(self, peso: float) -> None:
        print(f"O peso de sua carga é: {peso}")