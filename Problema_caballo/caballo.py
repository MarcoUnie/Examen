# problema_caballo/caballo.py
import random
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
        self.engine = create_engine('sqlite:///:memory:', echo=False)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
    
    def resolver(self):
        x, y = random.randint(0, self.tamano-1), random.randint(0, self.tamano-1)
        caballo = NodoCaballo((x, y))
        self.tablero[x][y] = 1
        paso = f"Caballo inicia en ({x}, {y})"
        self.pasos.append(paso)
        posicion = Posicion(
            juego="Caballo",
            paso=len(self.pasos),
            posicion_x=x,
            posicion_y=y,
            detalle=paso
        )
        self.session.add(posicion)
        self.session.commit()
        
        visitados = {(x, y)}
        contador = 2
        
        while len(visitados) < self.tamano * self.tamano:
            movimientos = caballo.movimientos_posibles(self.tamano)
            movimientos_no_visitados = [m for m in movimientos if m not in visitados]
            
            if not movimientos_no_visitados:
                paso = "No hay más movimientos posibles"
                self.pasos.append(paso)
                posicion = Posicion(
                    juego="Caballo",
                    paso=len(self.pasos),
                    posicion_x=-1,
                    posicion_y=-1,
                    detalle=paso
                )
                self.session.add(posicion)
                self.session.commit()
                break
                
            siguiente = min(movimientos_no_visitados, 
                          key=lambda pos: len([m for m in NodoCaballo(pos).movimientos_posibles(self.tamano) 
                                            if m not in visitados]))
            
            caballo.posicion = siguiente
            visitados.add(siguiente)
            self.tablero[siguiente[0]][siguiente[1]] = contador
            paso = f"Movimiento a {siguiente}"
            self.pasos.append(paso)
            posicion = Posicion(
                juego="Caballo",
                paso=len(self.pasos),
                posicion_x=siguiente[0],
                posicion_y=siguiente[1],
                detalle=paso
            )
            self.session.add(posicion)
            self.session.commit()
            contador += 1
            
        return self.pasos
    
    def get_posiciones(self):
        posiciones = self.session.query(Posicion).filter_by(juego="Caballo").all()
        if not posiciones:
            print("No se encontraron posiciones en la base de datos.")  # Depuración
        return posiciones