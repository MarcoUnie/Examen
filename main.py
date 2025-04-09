# main.py
from hanoi.torresdehanoi import TorreHanoi
from Reina.ProblemaReina import ProblemaReinas
from Problema_caballo.caballo import ProblemaCaballo
def mostrar_menu():
    print("\n=== Menú de Juegos ===")
    print("1. Torre de Hanoi")
    print("2. Problema de las Reinas")
    print("3. Problema del Caballo")
    print("4. Salir")
    return input("Seleccione una opción (1-4): ")

def main():
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            juego = TorreHanoi(6)
            pasos = juego.resolver()
            print("\nPasos para resolver la Torre de Hanoi:")
            for i, paso in enumerate(pasos, 1):
                print(f"Paso {i}: {paso}")
        elif opcion == "2":
            try:
                tamano = int(input("Ingrese el tamaño del tablero para el Problema de las Reinas (ej. 8 para 8x8): "))
                if tamano <= 0:
                    print("Por favor, ingrese un número positivo.")
                    continue
                juego = ProblemaReinas(tamano)
                pasos = juego.resolver()
                print("\nPasos para el Problema de las Reinas:")
                for i, paso in enumerate(pasos, 1):
                    print(f"Paso {i}: {paso}")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        elif opcion == "3":
            juego = ProblemaCaballo()
            pasos = juego.resolver()
            print("\nPasos para el Problema del Caballo:")
            for i, paso in enumerate(pasos, 1):
                print(f"Paso {i}: {paso}")
        
        elif opcion == "4":
            print("¡Gracias por jugar! Hasta luego.")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 4.")

if __name__ == "__main__":
    main()