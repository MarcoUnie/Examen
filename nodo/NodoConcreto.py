from nodo.py import Nodo
class NodoConcreto(Nodo):
    def __init__(self, valor=None):
        self._valor = valor
        self._siguiente = None

    def obtener_valor(self):
        return self._valor

    def establecer_valor(self, valor):
        self._valor = valor

    def obtener_siguiente(self):
        return self._siguiente

    def establecer_siguiente(self, nodo):
        self._siguiente = nodo

