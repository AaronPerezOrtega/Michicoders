import flet as ft
from solitaire import Solitaire


import flet as ft
from solitaire import Solitaire

def main(page: ft.Page):
    solitaire = Solitaire()

    boton = ft.ElevatedButton(
        content=ft.Text("Cambiar fondo"),
        on_click=solitaire.siguiente_fondo
    )

    page.add(boton)
    page.add(solitaire)

ft.run(main, assets_dir="juanpiz")
#ft.run(main, assets_dir="cartas")
