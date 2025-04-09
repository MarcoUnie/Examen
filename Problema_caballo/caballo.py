# problema_caballo/caballo.py
import random
from nodo.Nodo import Nodos

class NodoCaballo(Nodos):
    def __init__(self, posicion):
        super().__init__(posicion)
    
    def movimientos_posibles(self, tamano_tablero):
        x, y = self.posicion
        movimientos = [
            (x+2, y+1), (x+2, y-1), (x-2, y+1), (x-2, y-1),
            (x+1, y+2), (x+1, y-2), (x-1, y+2), (x-1, y-2)
        ]
        return [(x, y) for x, y in movimientos if 0 <= x < tamano_tablero and 0 <= y < tamano_tablero]

class ProblemaCaballo:
    def __init__(self, tamano):
        self.tamano = tamano
        self.tablero = [[0] * tamano for _ in range(tamano)]
        self.pasos = []
    
    def resolver(self):
        x, y = random.randint(0, self.tamano-1), random.randint(0, self.tamano-1)
        caballo = NodoCaballo((x, y))
        self.tablero[x][y] = 1
        self.pasos.append(f"Caballo inicia en ({x}, {y})")
        
        visitados = {(x, y)}
        contador = 2
        
        while len(visitados) < self.tamano * self.tamano:
            movimientos = caballo.movimientos_posibles(self.tamano)
            movimientos_no_visitados = [m for m in movimientos if m not in visitados]
            
            if not movimientos_no_visitados:
                self.pasos.append("No hay más movimientos posibles")
                break
                
            siguiente = min(movimientos_no_visitados, 
                          key=lambda pos: len([m for m in NodoCaballo(pos).movimientos_posibles(self.tamano) 
                                            if m not in visitados]))
            
            caballo.posicion = siguiente
            visitados.add(siguiente)
            self.tablero[siguiente[0]][siguiente[1]] = contador
            self.pasos.append(f"Movimiento a {siguiente}")
            contador += 1
            
        return self.pasos
