
# torre_hanoi/hanoi.py
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

class NodoHanoi(Nodos):
    def __init__(self, posicion, disco):
        super().__init__(posicion)
        self.disco = disco

class TorreHanoi:
    def __init__(self, n_discos):
        self.n_discos = n_discos
        self.pasos = []
        self.torres = [[NodoHanoi(i, d) for i, d in enumerate(range(n_discos, 0, -1))], [], []]
        self.engine = create_engine('sqlite:///:memory:', echo=False)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
    
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
            posicion = Posicion(
                juego="Hanoi",
                paso=len(self.pasos),
                posicion_x=destino,
                posicion_y=nodo.disco,
                detalle=paso
            )
            self.session.add(posicion)
            self.session.commit()
            self._mover_discos(n-1, auxiliar, destino, origen)
    
    def get_posiciones(self):
        return self.session.query(Posicion).filter_by(juego="Hanoi").all()