class Actas:
    def __init__(self,casilla,tc,distrito,municipio,estado,seccion,VN,PAN,PRI,PRD,PVEM,PT,MC,MORENA,INDIE,PRIAN,PAI,PRN,PRID,PVTM,PTV,MV,PM,tv,qr,fp):
        if int(casilla) < 1:
            raise ValueError("Casilla inexistente")
        #El tipo de casillas son del 1 - 5 
        #1 basica entre 100 - 750
        #2 contigua 750 > hacia arriba
        #3 Extraodinaria: Casilla que atiende a residentes con dificil acceso por algun motico extraordinario
        #4 Extraordinaria contigua: "" "" excediendo de 750 electores/as
        #5 Especial: Casilla que recibe votos de l@s ciudadan@s en transito
        if not 0 < int(tc) <= 5 :
            raise ValueError("Tipo de casilla inexistente")
        #Distritos son 300 iniciando en el 001
        if not  0 < int(distrito) <= 300:
            raise ValueError("Distrito invalido")
        distrito = str(distrito).zfill(3)
        if int(tv) < 0:
            raise ValueError("Cantidad de votos invalida")
        if not 0 < int(municipio) <= 2478:
            raise ValueError("Municipio invalido")
        municipio = str(municipio).zfill(4)
        if not 0 < int(estado) <= 32:
            raise ValueError("Estado Invalido")
        estado = str(estado).zfill(2)
        if not 0 < int(seccion) <= 99999:
            raise ValueError("Seccion invalida")
        seccion = str(seccion).zfill(5)
        
        #Partidos politicos votos
        if VN < 0:
            raise ValueError("Cantidad de votos invalida")
        if PAN < 0:
            raise ValueError("Cantidad de votos invalida")
        if PRI < 0:
            raise ValueError("Cantidad de votos invalida")
        if PRD < 0:
            raise ValueError("Cantidad de votos invalida")
        if PVEM < 0:
            raise ValueError("Cantidad de votos invalida")
        if PT < 0:
            raise ValueError("Cantidad de votos invalida")
        if  MC < 0:
            raise ValueError("Cantidad de votos invalida")
        if MORENA < 0:
            raise ValueError("Cantidad de votos invalida")
        if INDIE < 0:
            raise ValueError("Cantidad de votos invalida")
        if PRIAN < 0:
            raise ValueError("Cantidad de votos invalida")
        if PAI < 0:
            raise ValueError("Cantidad de votos invalida")
        if PRN < 0:
            raise ValueError("Cantidad de votos invalida")
        if PRID < 0:
            raise ValueError("Cantidad de votos invalida")
        if PVTM < 0:
            raise ValueError("Cantidad de votos invalida")
        if PTV < 0:
            raise ValueError("Cantidad de votos invalida")
        if MV < 0:
            raise ValueError("Cantidad de votos invalida")
        if PM < 0:
            raise ValueError("Cantidad de votos invalida")
        
        self.__casilla = casilla
        #tc = tipo de casilla
        self.__tc = tc
        self.__distrito = distrito
        self.__municipio = municipio
        self.__estado = estado
        self.__seccion = seccion
        #tv = total de votos
        self.__VN = VN
        self.__PAN = PAN
        self.__PRI = PRI
        self.__PRD = PRD
        self.__PVEM = PVEM
        self.__PT = PT
        self.__MC = MC
        self.__MORENA = MORENA
        self.__INDIE = INDIE
        self.__PRIAN = PRIAN
        self.__PAI = PAI
        self.__PRN = PRN
        self.__PRID = PRID
        self.__PVTM = PVTM
        self.__PTV = PTV
        self.__MV = MV
        self.__PM = PM
        self.__tv = tv
        #QR
        self.__qr = qr
        #fp = fecha de procesamiento 
        self.__fp = fp

    def getcasilla(self):
        return self.__casilla
        
    def setcasilla(self, casilla):
        if int(casilla) < 1:
            raise ValueError("Casilla inexistente")
        self.__casilla = casilla

    def gettc(self):
        return self.__tc

    def settc(self,tc):
        if not 0 < int(tc) <= 5:
            raise ValueError("Tipo de casilla inexistente")
        self.__tc = tc

    def getdistrito(self):
        return self.__distrito

    def setdistrito(self,distrito):
        if not 0 < int(distrito) <= 300:
            raise ValueError("Distrito invalido")
        distrito = str(distrito).zfill(3)
        self.__distrito = distrito
        
    def getmunicipio(self):
        return self.__municipio

    def setmunicipio(self, municipio):
        if not 0 < int(municipio) <= 2478:
            raise ValueError("Municipio invalido")
        municipio = str(municipio).zfill(4)
        self.__municipio = municipio
    
    def getestado(self):
        return self.__estado

    def setestado(self, estado):
        if not 0 < int(estado) <= 32:
            raise ValueError("Estado Invalido")
        estado = str(estado).zfill(2)
        self.__estado = estado

    def getseccion(self):
        return self.__seccion

    def setseccion(self, seccion):
        if not 0 < int(seccion) <= 99999:
            raise ValueError("Seccion invalida")
        seccion = str(seccion).zfill(5)
        self.__seccion = seccion
    
    def getVN(self):
        return self.__VN

    def setVN(self, VN):
        if VN < 0:
            raise ValueError("Cantidad de votos invalida")
        self.__VN = VN

    def getPAN(self):
        return self.__PAN

    def setPAN(self, PAN):
        if PAN < 0:
            raise ValueError("Cantidad de votos invalida")
        self.__PAN = PAN

    def getPRI(self):
        return self.__PRI

    def setPRI(self, PRI):
        if PRI < 0:
            raise ValueError("Cantidad de votos invalida")
        self.__PRI = PRI

    def getPRD(self):
        return self.__PRD

    def setPRD(self, PRD):
        if PRD < 0:
            raise ValueError("Cantidad de votos invalida")
        self.__PRD = PRD

    def getPVEM(self):
        return self.__PVEM

    def setPVEM(self, PVEM):
        if PVEM < 0:
            raise ValueError("Cantidad de votos invalida")
        self.__PVEM = PVEM

    def getPT(self):
        return self.__PT

    def setPT(self, PT):
        if PT < 0:
            raise ValueError("Cantidad de votos invalida")
        self.__PT = PT

    def getMC(self):
        return self.__MC

    def setMC(self, MC):
        if MC < 0:
            raise ValueError("Cantidad de votos invalida")
        self.__MC = MC

    def getMORENA(self):
        return self.__MORENA

    def setMORENA(self, MORENA):
        if MORENA < 0:
            raise ValueError("Cantidad de votos invalida")
        self.__MORENA = MORENA

    def getINDIE(self):
        return self.__INDIE

    def setINDIE(self, INDIE):
        if INDIE < 0:
            raise ValueError("Cantidad de votos invalida")
        self.__INDIE = INDIE

    def getPRIAN(self):
        return self.__PRIAN

    def setPRIAN(self, PRIAN):
        if PRIAN < 0:
            raise ValueError("Cantidad de votos invalida")
        self.__PRIAN = PRIAN

    def getPAI(self):
        return self.__PAI

    def setPAI(self, PAI):
        if PAI < 0:
            raise ValueError("Cantidad de votos invalida")
        self.__PAI = PAI

    def getPRN(self):
        return self.__PRN

    def setPRN(self, PRN):
        if PRN < 0:
            raise ValueError("Cantidad de votos invalida")
        self.__PRN = PRN

    def getPRID(self):
        return self.__PRID

    def setPRID(self, PRID):
        if PRID < 0:
            raise ValueError("Cantidad de votos invalida")
        self.__PRID = PRID

    def getPVTM(self):
        return self.__PVTM

    def setPVTM(self, PVTM):
        if PVTM < 0:
            raise ValueError("Cantidad de votos invalida")
        self.__PVTM = PVTM

    def getPTV(self):
        return self.__PTV

    def setPTV(self, PTV):
        if PTV < 0:
            raise ValueError("Cantidad de votos invalida")
        self.__PTV = PTV

    def getMV(self):
        return self.__MV

    def setMV(self, MV):
        if MV < 0:
            raise ValueError("Cantidad de votos invalida")
        self.__MV = MV

    def getPM(self):
        return self.__PM

    def setPM(self, PM):
        if PM < 0:
            raise ValueError("Cantidad de votos invalida")
        self.__PM = PM

    def gettv(self):
        return self.__tv

    def settv(self,tv):
        if int(tv) < 0:
            raise ValueError("Cantidad de votos invalida")
        self.__tv = tv

    def getqr(self):
        return self.__qr

    def setqr(self, qr):
        self.__qr = qr

    def getfp(self):
        return self.__fp

    def setfp(self,fp):
        self.__fp = fp

    def __str__(self):
            return f"""-----------------------------------\nCasilla: {self.__casilla}\nTipo de casilla: {self.__tc}\nDistrito: {self.__distrito}\nMunicipio: {self.__municipio}\nEstado: {self.__estado}\nSeccion: {self.__seccion}\n\nVotos:\nVN: {self.__VN}\nPAN: {self.__PAN}\nPRI: {self.__PRI}\nPRD: {self.__PRD}\nPVEM: {self.__PVEM}\nPT: {self.__PT}\nMC: {self.__MC}\nMORENA: {self.__MORENA}\nINDIE: {self.__INDIE}\nPRIAN: {self.__PRIAN}\nPAI: {self.__PAI}\nPRN: {self.__PRN}\nPRID: {self.__PRID}\nPVTM: {self.__PVTM}\nPTV: {self.__PTV}\nMV: {self.__MV}\nPM: {self.__PM}\nTotal Votos: {self.__tv}\n\nQR: {self.__qr}\nFecha de Procesamiento: {self.__fp}\n-----------------------------------"""
    def mostrar(self,lista):
        if not lista:
            print("Vacia")
            return
        for i in lista:
            print(i)
        return

#Estados:
# 01 Aguascalientes
# 02 Baja California
# 03 Baja California Sur
# 04 Campeche
# 05 Coahuila
# 06 Colima
# 07 Chiapas
# 08 Chihuahua
# 09 Durango
# 10 Guanajuato
# 11 Guerrero
# 12 Hidalgo
# 13 Jalisco
# 14 México
# 15 Michoacán
# 16 Morelos
# 17 Nayarit
# 18 Nuevo León
# 19 Oaxaca
# 20 Puebla
# 21 Querétaro
# 22 Quintana Roo
# 23 San Luis Potosí
# 24 Sinaloa
# 25 Sonora
# 26 Tabasco
# 27 Tamaulipas
# 28 Tlaxcala
# 29 Veracruz
# 30 Yucatán
# 31 Zacatecas
# 32 CDMX
 
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
# VN - voto nulo
