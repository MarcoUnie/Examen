# problema_reinas/reinas.py
import random
from nodo.Nodo import Nodos

class NodoReina(Nodos):
    def __init__(self, posicion):
        super().__init__(posicion)
    
    def amenaza(self, otra_posicion):
        x1, y1 = self.posicion
        x2, y2 = otra_posicion
        return (x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2))

class ProblemaReinas:
    def __init__(self, tamano):
        self.tamano = tamano
        self.tablero = [[0] * tamano for _ in range(tamano)]
        self.pasos = []
        self.reinas = []
    
    def colocar_reinas(self):
        for col in range(self.tamano):
            fila = random.randint(0, self.tamano-1)
            self.tablero[fila][col] = 1
            reina = NodoReina((fila, col))
            self.reinas.append(reina)
            self.pasos.append(f"Colocada reina en ({fila}, {col})")
    
    def resolver(self):
        self.colocar_reinas()
        conflictos = self.verificar_conflictos()
        self.pasos.append(f"Conflictos encontrados: {conflictos}")
        return self.pasos
    
    def verificar_conflictos(self):
        conflictos = []
        for i, reina1 in enumerate(self.reinas):
            for reina2 in self.reinas[i+1:]:
                if reina1.amenaza(reina2.posicion):
                    conflictos.append((reina1.posicion, reina2.posicion))
        return conflictos
