from dataclasses import dataclass
import datetime
from random import randint
@dataclass

class Actas:
    def __init__(self,casilla,tc,distrito,municipio,estado,seccion,tv,qr,fp):
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
        
        self.__casilla = casilla
        #tc = tipo de casilla
        self.__tc = tc
        self.__distrito = distrito
        self.__municipio = municipio
        self.__estado = estado
        self.__seccion = seccion
        #tv = total de votos
        self.__tv = tv
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
        if  0 < int(tc) <= 5:
            raise ValueError("Tipo de casilla inexistente")
        self.__tc = tc

    def getdistrito(self):
        return self.__distrito

    def setdistrito(self,distrito):
        if  0 < int(distrito) <= 300:
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
        return f"-----------------------------------\nCasilla: {self.__casilla}\nTipo de casilla: {self.__tc}\nDistrito: {self.__distrito}\nMunicipio: {self.__municipio}\nEstado: {self.__estado}\nSeccion: {self.__seccion}\nTotal Votos: {self.__tv}\nQR: {self.__qr}\nFecha de Procesamiento: {self.__fp}\n-----------------------------------"

    def mostrar(lista):
        if not lista:
            print("Vacia")
            return
        for i in lista:
            print(i)
        return
        
#(self,casilla,tc,distrito,municipio,estado,seccion,tv,qr,fp):
def main():
    
    Act1 = Actas("1","1","9","1","4","00001",243,"02,14,01,001,1",datetime.date.today())
    Act2 = Actas(randint(1,10000),randint(1,5),randint(1,300),randint(1,2478),randint(1,32),randint(1,10000),randint(1,132000000),"02,14,01,001,1",datetime.date.today())
    Act3 = Actas(randint(1,10000),randint(1,5),randint(1,300),randint(1,2478),randint(1,32),randint(1,10000),randint(1,132000000),"02,14,01,001,1",datetime.date.today())
    Act4 = Actas(randint(1,10000),randint(1,5),randint(1,300),randint(1,2478),randint(1,32),randint(1,10000),randint(1,132000000),"02,14,01,001,1",datetime.date.today())
    
    #manera 1 de mostrar la lista
    print(Act1)
    print(Act2)
    print(Act3)
    print(Act4)
    print()
    
    #manera 2 de mostrar la lista
    actas = [Act1,Act2,Act3,Act4]
    Actas.mostrar(actas)
    print()

if __name__ == "__main__":
    while True:
        try:
            main()
        except ValueError as error:
            print(error)
        break
        
 
#URGENTE       
#Checar errores con literales
#Implementar que salgan los nombres de los estados
#Crear la clase para los votos de cada partido
#Crear Main
#Preguntar acerca de la fecha de Procesamiento a la maestra
#Preguntar si es solo con un distrito o varios a la maestra

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
 
