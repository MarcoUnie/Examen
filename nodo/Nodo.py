class Nodos:
    def __init__(self, tipo_ficha):
        self.tipo_ficha = tipo_ficha  # Puede ser 'caballo', 'reina' o 'torre_hanoi'
        self.siguiente = None
    def mover(self, posicion_actual, movimiento):
        if self.tipo_ficha == 'caballo':
            # Movimiento en forma de L
            posibles_movimientos = [
                (2, 1), (2, -1), (-2, 1), (-2, -1),
                (1, 2), (1, -2), (-1, 2), (-1, -2)
            ]
            if movimiento in posibles_movimientos:
                return (posicion_actual[0] + movimiento[0], posicion_actual[1] + movimiento[1])
        
        elif self.tipo_ficha == 'reina':
            # Movimiento en línea recta o diagonal
            if movimiento[0] == 0 or movimiento[1] == 0 or abs(movimiento[0]) == abs(movimiento[1]):
                return (posicion_actual[0] + movimiento[0], posicion_actual[1] + movimiento[1])
        
        elif self.tipo_ficha == 'torre_hanoi':
            # Movimiento solo en una dirección (vertical u horizontal)
            if movimiento[0] == 0 or movimiento[1] == 0:
                return (posicion_actual[0] + movimiento[0], posicion_actual[1] + movimiento[1])
