# main.py
# main.py
import gradio as gr
from hanoi.torresdehanoi import TorreHanoi
from Reina.ProblemaReina import ProblemaReinas
from Problema_caballo.caballo import ProblemaCaballo


class GameController:
    def __init__(self):
        self.juego = None

    def iniciar_juego(self, juego_seleccionado, tamano_reinas):
        print(f"Iniciando juego: {juego_seleccionado}, tamaño reinas: {tamano_reinas}")  # Depuración
        if juego_seleccionado == "Torre de Hanoi":
            self.juego = TorreHanoi(6)  # Tamaño fijo: 3 discos
            pasos = self.juego.resolver()
            posiciones = self.juego.get_posiciones()
            print(f"Pasos generados para Hanoi: {pasos}")  # Depuración
            return self.format_pasos(pasos, posiciones)
        
        elif juego_seleccionado == "Problema de las Reinas":
            try:
                tamano = int(tamano_reinas) if tamano_reinas else 8  # Por defecto 8
                if tamano <= 0:
                    return "Por favor, ingrese un número positivo para las Reinas."
                self.juego = ProblemaReinas(tamano)
                pasos = self.juego.resolver()
                posiciones = self.juego.get_posiciones()
                print(f"Pasos generados para Reinas: {pasos}")  # Depuración
                return self.format_pasos(pasos, posiciones)
            except ValueError:
                return "Por favor, ingrese un número válido para las Reinas."
        
        elif juego_seleccionado == "Problema del Caballo":
            self.juego = ProblemaCaballo(8)  # Tamaño fijo: 5x5
            pasos = self.juego.resolver()
            posiciones = self.juego.get_posiciones()
            print(f"Pasos generados para Caballo: {pasos}")  # Depuración
            return self.format_pasos(pasos, posiciones)
        
        return "Seleccione un juego válido."

    def format_pasos(self, pasos, posiciones):
        if not pasos:
            return "No se generaron pasos."
        result = []
        for i, (paso, pos) in enumerate(zip(pasos, posiciones), 1):
            result.append(f"Paso {i}: {paso}\nPosición: ({pos.posicion_x}, {pos.posicion_y})")
        return "\n\n".join(result)

def create_interface():
    controller = GameController()

    with gr.Blocks(title="Juegos de Tablero") as demo:
        gr.Markdown("# Juegos de Tablero")
        
        with gr.Row():
            juego_dropdown = gr.Dropdown(
                choices=["Torre de Hanoi", "Problema de las Reinas", "Problema del Caballo"],
                label="Seleccione un juego",
                value="Torre de Hanoi"
            )
            tamano_input = gr.Textbox(
                label="Tamaño del tablero (solo para Reinas, ej. 8)",
                value="8",
                visible=False
            )
        
        def update_tamano_visibility(juego):
            return gr.update(visible=(juego == "Problema de las Reinas"))
        
        juego_dropdown.change(
            fn=update_tamano_visibility,
            inputs=juego_dropdown,
            outputs=tamano_input
        )
        
        iniciar_btn = gr.Button("Iniciar Juego")
        
        output_text = gr.Textbox(label="Pasos del Juego", lines=10, interactive=False)

        iniciar_btn.click(
            fn=controller.iniciar_juego,
            inputs=[juego_dropdown, tamano_input],
            outputs=output_text
        )

    return demo

if __name__ == "__main__":
    interface = create_interface()
    interface.launch(debug=True)  # Modo debug para ver mensajes en la consola