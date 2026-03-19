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
                votos_pan = int(input("Votos PAN: "))
                votos_pri = int(input("Votos PRI: "))
                votos_prd = int(input("Votos PRD: "))
                votos_pvem = int(input("Votos PVEM: "))
                votos_pt = int(input("Votos PT: "))
                votos_mc = int(input("Votos MC: "))
                votos_morena = int(input("Votos MORENA: "))
                votos_indie = int(input("Votos INDEPENDIENTE: "))
                # Coaliciones
                votos_prian = int(input("Votos PAN PRI PRD: "))
                votos_pai = int(input("Votos PAN PRI: "))
                votos_prn = int(input("Votos PAN PRD: "))
                votos_prid = int(input("Votos PRI PRD: "))
                votos_pvtm = int(input("Votos VERDE PT MORENA: "))
                votos_ptv = int(input("Votos VERDE PT: "))
                votos_mv = int(input("Votos MORENA VERDE: "))
                votos_pm = int(input("Votos PT MORENA: "))
                votos_nulos = int(input("Votos Nulos: "))
                tv = votos_pan+votos_pri+votos_prd+votos_pvem+votos_pt+votos_mc+votos_morena+votos_indie+votos_prian+votos_pai+votos_prn+votos_prid+votos_pvtm+votos_ptv+votos_mv+votos_pm+votos_nulos
                print(f"Total de votos: {tv}")
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
                acta = Actas(casilla, tc, distrito, municipio, estado, seccion,votos_nulos,votos_pan,votos_pri,votos_prd,votos_pvem,votos_pt,votos_mc,votos_morena,votos_indie,votos_prian,votos_pai,votos_prn,votos_prid,votos_pvtm,votos_ptv,votos_mv,votos_pm ,tv, qr, fp)
                lis_acta.append(acta)
                print("Acta agregada")

            elif opcion == 2:
                print(acta)

        except ValueError:
            print("Error:")

if __name__ == "__main__":
    main()
