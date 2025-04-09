class Nodo:
    def __init__(self, tipo_ficha):
        self.tipo_ficha = tipo_ficha  # Puede ser 'caballo', 'reina' o 'torre_hanoi'
        self.siguiente = None

    def __str__(self):
        return f"{self.tipo_ficha.capitalize()}({self.valor})"