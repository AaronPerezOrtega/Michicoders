import flet as ft

from vista.asistenciaView import AsistenciaView
from controller.asistenciaController import Asistencia_Controller

def main(page: ft.Page):

    vista = AsistenciaView(page)

    controller = Asistencia_Controller(vista)

    vista.btn_registrar.on_click = controller.resgistrar_asistencia
    
    vista.btn_eliminar.on_click = controller.eliminar_registros

    page.add(
        vista.construir_interfaz()
    )

ft.app(target = main)
