
# torre_hanoi/hanoi.py
from nodo.Nodo import Nodos

class NodoHanoi(Nodos):
    def __init__(self, posicion, disco):
        super().__init__(posicion)
        self.disco = disco  # Tamaño del disco

class TorreHanoi:
    def __init__(self, n_discos):
        self.n_discos = n_discos
        self.pasos = []
        self.torres = [[NodoHanoi(i, d) for i, d in enumerate(range(n_discos, 0, -1))], [], []]
    
    def resolver(self):
        self._mover_discos(self.n_discos, 0, 2, 1)
        return self.pasos
    
    def _mover_discos(self, n, origen, destino, auxiliar):
        if n > 0:
            self._mover_discos(n-1, origen, auxiliar, destino)
            nodo = self.torres[origen].pop()
            self.torres[destino].append(nodo)
            paso = f"Mover disco {nodo.disco} de torre {origen} a torre {destino}"
            self.pasos.append(paso)
            self._mover_discos(n-1, auxiliar, destino, origen)
