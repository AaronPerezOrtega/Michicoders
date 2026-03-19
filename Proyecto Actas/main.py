from actas import Actas
import datetime

def main():
    lis_acta = []

    while True:
        print("\n--- MENU ---")
        print("1. Agregar acta")
        print("2. Mostrar actas")
        print("3. Eliminar acta")
        print("4. Mostrar total de votos")

        opcion = int(input("Selecciona la tarea que deseas realizar: "))

        try:
            if opcion == 1:
                casilla = input("Casilla: ")
                tc = input("Tipo de casilla: ")
                distrito = input("Distrito: ")
                municipio = input("Municipio: ")
                estado = input("Estado: ")
                seccion = input("Seccion: ")
                votos_pan = input("Votos PAN: ")
                votos_pri = input("Votos PRI: ")
                votos_prd = input("Votos PRD: ")
                votos_pvem = input("Votos PVEM: ")
                votos_pt = input("Votos PT: ")
                votos_mc = input("Votos MC: ")
                votos_morena = input("Votos MORENA: ")
                votos_indie = input("Votos INDEPENDIENTE: ")
                # Coaliciones
                votos_prian = input("Votos PAN PRI PRD: ")
                votos_pai = input("Votos PAN PRI: ")
                votos_prn = input("Votos PAN PRD: ")
                votos_prid = input("Votos PRI PRD: ")
                votos_pvtm = input("Votos VERDE PT MORENA: ")
                votos_ptv = input("Votos VERDE PT: ")
                votos_mv = input("Votos MORENA VERDE: ")
                votos_pm = input("Votos PT MORENA: ")
                tv = input(f" Total de votos: {votos_pan+votos_pri+votos_prd+votos_pvem+votos_pt+votos_mc+votos_morena+votos_indie+votos_prian+votos_pai+votos_prn+votos_prid+votos_pvtm+votos_ptv+votos_mv+votos_pm}")
                qr = 1
                fp = datetime.date.today()
                # PAN - Partido Acción Nacional
                # PRI - Partido Revolucionario Institucional
                # PRD - Partido de la Revolución Democrática
                # PVEM - Partido Verde Ecologista de México
                # PT - Partido del Trabajo
                # MC - Movimiento Ciudadano
                # MORENA - Movimiento Regeneración Nacional
                # INDIE - INDEPENDIENTE
                # PRIAN - PAN PRI PRD
                # PAI - PAN PRI
                # PRN - PAN PRD
                # PRID - PRI PRD
                # PVTM - VERDE PT MORENA
                # PTV - VERDE PT
                # MV - MORENA VERDE
                # PM - PT MORENA
                acta = Actas(casilla, tc, distrito, municipio, estado, seccion, tv, qr, fp)
                lis_acta.append(acta)
                print("Acta agregada")

            elif opcion == 2:
                print(acta)

        except ValueError as error:
            print("Error:")

if __name__ == "__main__":
    main()
