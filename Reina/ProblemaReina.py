# problema_reinas/reinas.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from nodo.Nodo import Nodos
Base = declarative_base()

class Posicion(Base):
    __tablename__ = 'posiciones'
    id = Column(Integer, primary_key=True)
    juego = Column(String)
    paso = Column(Integer)
    posicion_x = Column(Integer)
    posicion_y = Column(Integer)
    detalle = Column(String)

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
        self.engine = create_engine('sqlite:///:memory:', echo=False)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
    
    def es_seguro(self, fila, col):
        # Verificar fila y diagonales
        for j in range(col):
            if self.tablero[fila][j] == 1:
                return False
            if fila - (col - j) >= 0 and self.tablero[fila - (col - j)][j] == 1:
                return False
            if fila + (col - j) < self.tamano and self.tablero[fila + (col - j)][j] == 1:
                return False
        return True
    
    def resolver(self):
        if self._resolver_util(0):
            paso = "Solución encontrada"
            self.pasos.append(paso)
            posicion = Posicion(
                juego="Reinas",
                paso=len(self.pasos),
                posicion_x=-1,
                posicion_y=-1,
                detalle=paso
            )
            self.session.add(posicion)
            self.session.commit()
        else:
            paso = "No se encontró solución"
            self.pasos.append(paso)
            posicion = Posicion(
                juego="Reinas",
                paso=len(self.pasos),
                posicion_x=-1,
                posicion_y=-1,
                detalle=paso
            )
            self.session.add(posicion)
            self.session.commit()
        return self.pasos
    
    def _resolver_util(self, col):
        if col >= self.tamano:
            return True
        
        for fila in range(self.tamano):
            if self.es_seguro(fila, col):
                self.tablero[fila][col] = 1
                reina = NodoReina((fila, col))
                self.reinas.append(reina)
                paso = f"Colocada reina en ({fila}, {col})"
                self.pasos.append(paso)
                posicion = Posicion(
                    juego="Reinas",
                    paso=len(self.pasos),
                    posicion_x=fila,
                    posicion_y=col,
                    detalle=paso
                )
                self.session.add(posicion)
                self.session.commit()
                
                if self._resolver_util(col + 1):
                    return True
                
                # Backtracking: quitar la reina si no lleva a una solución
                self.tablero[fila][col] = 0
                self.reinas.pop()
                paso = f"Retirada reina de ({fila}, {col}) - Backtracking"
                self.pasos.append(paso)
                posicion = Posicion(
                    juego="Reinas",
                    paso=len(self.pasos),
                    posicion_x=fila,
                    posicion_y=col,
                    detalle=paso
                )
                self.session.add(posicion)
                self.session.commit()
        
        return False
    
    def get_posiciones(self):
        return self.session.query(Posicion).filter_by(juego="Reinas").all()