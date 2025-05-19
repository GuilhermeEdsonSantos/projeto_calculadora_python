from abc import ABC, abstractmethod
import math

class IOperacaoMatematica(ABC):
    @abstractmethod
    def validar(self) -> bool:
        pass

    @abstractmethod
    def calcular(self) -> float:
        pass


class OperacaoMatematica(IOperacaoMatematica):
    def __init__(self, numero1: float, numero2: float):
        self._numero1 = numero1
        self._numero2 = numero2

    @property
    def numero1(self) -> float:
        return self._numero1

    @property
    def numero2(self) -> float:
        return self._numero2

    def validar(self) -> bool:
        return self._numero1 >= 0 and self._numero2 >= 0

    def calcular(self) -> float:
        if self.validar():
            return self.realizar_calculo()
        else:
            return -1

    @abstractmethod
    def realizar_calculo(self) -> float:
        pass


class Soma(OperacaoMatematica):
    def realizar_calculo(self) -> float:
        return self.numero1 + self.numero2


class Subtracao(OperacaoMatematica):
    def realizar_calculo(self) -> float:
        return self.numero1 - self.numero2


class Multiplicacao(OperacaoMatematica):
    def realizar_calculo(self) -> float:
        return self.numero1 * self.numero2


class Divisao(OperacaoMatematica):
    def validar(self) -> bool:
        return self.numero1 >= 0 and self.numero2 > 0

    def realizar_calculo(self) -> float:
        return self.numero1 / self.numero2


class Potenciacao(OperacaoMatematica):
    def realizar_calculo(self) -> float:
        return math.pow(self.numero1, self.numero2)


class FabricaOperacaoMatematica:
    @staticmethod
    def criar_operacao_matematica(numero1: float, numero2: float, operacao: str) -> IOperacaoMatematica:
        if operacao == "+":
            return Soma(numero1, numero2)
        elif operacao == "-":
            return Subtracao(numero1, numero2)
        elif operacao == "*":
            return Multiplicacao(numero1, numero2)
        elif operacao == "^":
            return Potenciacao(numero1, numero2)
        else:
            return Divisao(numero1, numero2)


class Calculadora:
    @staticmethod
    def calcular(calculo: str) -> float:
        partes = calculo.strip().split(" ")
        numero1 = float(partes[0])
        operacao = partes[1]
        numero2 = float(partes[2])
        operacao_matematica = FabricaOperacaoMatematica.criar_operacao_matematica(numero1, numero2, operacao)
        return operacao_matematica.calcular()


# Exemplo de uso
calculo = "10 + 10"
resultado = Calculadora.calcular(calculo)

if resultado >= 0:
    # Se o resultado for inteiro, mostrar sem decimal
    if resultado.is_integer():
        print(f"{calculo} = {int(resultado)}")
    else:
        print(f"{calculo} = {resultado}")
else:
    print("Operação inválida")
