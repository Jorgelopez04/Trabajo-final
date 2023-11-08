from abc import ABC, abstractmethod
from modelo.errores import (
    LongitudClaveInsuficienteError,
    FaltaMayusculaError,
    FaltaMinusculaError,
    FaltaNumeroError,
    FaltaCaracterEspecialError,
    NoContieneCalistoError
)

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    @abstractmethod
    def es_valida(self, clave):
        pass

    def _validar_longitud(self, clave):
        if len(clave) < self._longitud_esperada:
            raise LongitudClaveInsuficienteError()

    def _contiene_mayuscula(self, clave):
        if not any(c.isupper() for c in clave):
            raise FaltaMayusculaError()

    def _contiene_minuscula(self, clave):
        if not any(c.islower() for c in clave):
            raise FaltaMinusculaError()

    def _contiene_numero(self, clave):
        if not any(c.isdigit() for c in clave):
            raise FaltaNumeroError()

class ReglaValidacionGanimedes(ReglaValidacion):
    def contiene_caracter_especial(self, clave):
        if not any(c in '@_#$%' for c in clave):
            raise FaltaCaracterEspecialError()

    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_mayuscula(clave)
        self._contiene_minuscula(clave)
        self._contiene_numero(clave)
        self.contiene_caracter_especial(clave)
        return True

class ReglaValidacionCalisto(ReglaValidacion):
    def contiene_calisto(self, clave):
        if 'calisto' not in clave.lower() or clave.isupper() or clave.islower():
            raise NoContieneCalistoError()

    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_mayuscula(clave)
        self._contiene_minuscula(clave)
        self._contiene_numero(clave)
        self.contiene_calisto(clave)
        return True

class Validador:
    def __init__(self, regla):
        self.regla = regla

    def es_valida(self, clave):
        return self.regla.es_valida(clave)


