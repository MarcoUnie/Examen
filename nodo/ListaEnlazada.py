from nodo.Nodo import Nodo
from nodo.NodoConcreto import NodoConcreto

class ListaEnlazada:
    def __init__(self):
        self._cabeza = None

    def agregar(self, valor):
        nuevo_nodo = NodoConcreto(valor)
        if not self._cabeza:
            self._cabeza = nuevo_nodo
        else:
            actual = self._cabeza
            while actual.obtener_siguiente():
                actual = actual.obtener_siguiente()
            actual.establecer_siguiente(nuevo_nodo)

    def mostrar(self):
        actual = self._cabeza
        while actual:
            print(actual.obtener_valor(), end=" -> ")
            actual = actual.obtener_siguiente()
        print("None")