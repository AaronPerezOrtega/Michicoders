from actas import Actas
import datetime

def main():
    lis_acta = []

    while True:
        print("\n--- MENU ---")
        print("1. Agregar acta")
        print("2. Mostrar actas")
        print("3. Mostrar un acta para modificar algún dato (Buscar con su número de registro en la base de datos)")
        try:
            opcion = int(input("Selecciona la tarea que deseas realizar: "))
            if opcion>3:
                print("--Selecciona una opción del menú--")
        except:
            print("--Selecciona una opción valida--")
            continue

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
                if (len(lis_acta))<=0:
                    print("--Lista de actas vacia--")
                    continue
                for i in range (len(lis_acta)):
                    print("-----------------------------------")
                    print(f"Acta número: {i+1}")
                    print (f"{lis_acta[i]}")

            elif opcion==3:
                try:
                    buscar_acta=int(input("¿Qué acta deseas consultar? \n"))
                except :
                    print("El acta no existe")
                    pass 
                if buscar_acta<(len(lis_acta)-1) or buscar_acta>(len(lis_acta)):
                    print("El acta no existe")
                    continue
                print("-----------------------------------")
                print(f"Acta consultada: {buscar_acta}")
                print(lis_acta[buscar_acta-1])
                x=int(input("¿Deseas modificar algún dato? 1:si 2:no"))
                if x==1:
                    dato_mod=int(input("¿Qué dato deseas modificar? \n 1:Casilla"))
                    if dato_mod==1:
                         acta= lis_acta[buscar_acta-1]
                         nuevo=(int(input("Nueva casilla: ")))
                         acta.setcasilla(nuevo)
                else:
                    continue
                        
                        #casilla,tc,distrito,municipio,estado,seccion,VN,PAN,PRI,PRD,PVEM,PT,MC,MORENA,INDIE,PRIAN,PAI,PRN,PRID,PVTM,PTV,MV,PM,tv,qr,fp
        except ValueError:
            print("Error:")

if __name__ == "__main__":
    main()
