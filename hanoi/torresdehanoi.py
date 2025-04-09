from nodo.Nodo.py import Nodos

class FichaHanoi(Nodos):
    def __init__(self, tamaño):
        super().__init__(tipo_ficha='torre_hanoi')
        self.tamaño = tamaño

        return self.tamaño

def resolver_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover ficha de {origen} a {destino}")
        return
    resolver_hanoi(n - 1, origen, auxiliar, destino)
    print(f"Mover ficha de {origen} a {destino}")
    resolver_hanoi(n - 1, auxiliar, destino, origen)

if __name__ == "__main__":
    # Crear las fichas de Hanoi
    fichas = [FichaHanoi(tamaño=i) for i in range(6, 0, -1)]
    
    # Definir los nombres de las torres
    torre_origen = "A"
    torre_destino = "C"
    torre_auxiliar = "B"
    
    # Resolver el problema de las Torres de Hanoi
    resolver_hanoi(len(fichas), torre_origen, torre_destino, torre_auxiliar)