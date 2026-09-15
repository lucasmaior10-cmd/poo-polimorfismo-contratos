from abc import ABC, abstractmethod
import math

class Sensor(ABC):
    def __init__(self, tag: str):
        self._tag = tag

    def tag(self) -> str:
        return self._tag

    @abstractmethod
    def valor(self) -> float:
        pass

    @abstractmethod
    def unidade(self) -> str:
        pass

    @abstractmethod
    def atualizar(self, leitura: float) -> bool:
        pass

    @abstractmethod
    def em_alerta(self) -> bool:
        pass


class SensorNivel(Sensor):
    def __init__(self, tag: str):
        super().__init__(tag)
        self._valor = 50.0

    def valor(self) -> float:
        return self._valor

    def unidade(self) -> str:
        return "%"

    def atualizar(self, leitura: float) -> bool:
        if not math.isfinite(leitura) or leitura < 0.0 or leitura > 100.0:
            return False
        self._valor = leitura
        return True

    def em_alerta(self) -> bool:
        return self._valor < 20.0


class SensorTemperatura(Sensor):
    def __init__(self, tag: str):
        super().__init__(tag)
        self._valor = 25.0

    def valor(self) -> float:
        return self._valor

    def unidade(self) -> str:
        return "C"

    def atualizar(self, leitura: float) -> bool:
        if not math.isfinite(leitura) or leitura < -40.0 or leitura > 125.0:
            return False
        self._valor = leitura
        return True

    def em_alerta(self) -> bool:
        return self._valor > 45.0


class SensorPressao(Sensor):
    def __init__(self, tag: str):
        super().__init__(tag)
        self._valor = 1.0

    def valor(self) -> float:
        return self._valor

    def unidade(self) -> str:
        return "bar"

    def atualizar(self, leitura: float) -> bool:
        if not math.isfinite(leitura) or leitura < 0.0 or leitura > 10.0:
            return False
        self._valor = leitura
        return True

    def em_alerta(self) -> bool:
        return self._valor > 8.0
        