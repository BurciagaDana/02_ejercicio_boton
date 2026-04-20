import flet as ft

# función principal
def main(page: ft.Page):
    page.title = "App con botón"

    # texto inicial
    mensaje = ft.Text("Hola, mundo desde Flet!", size=25, color="pink")

    # función del botón
    def cambiar_texto(e):
        mensaje.value = "¡Adios, noob :V!"
        mensaje.color = "green"
        page.update()

    # botón
    boton1 = ft.ElevatedButton("Cambiar mensaje", on_click=cambiar_texto)

    # agregar a la ventana
    page.add(mensaje, boton1)

# ejecutar app
ft.app(target=main)