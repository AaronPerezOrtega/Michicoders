from dataclasses import dataclass
from datetime import time
@dataclass

class Actas:
    def __init__(self,casilla,tc,distrito,municipio,seccion,tv,qr,fp):
        if int(casilla) < 1:
            raise ValueError("Casilla inexistente")
        
        self.__casilla = casilla
        #tc = tipo de casilla
        self.__tc = tc
        self.__distrito = distrito
        self.__municipio = municipio
        self.__seccion = seccion
        #tv = total de votos
        self.__tv = tv
        self.__qr = qr
        #fp = fecha de procesamiento 
        self.__fp = fp#datetime
        
        
    def getcasilla(self):
        return self.__casilla
    
    def gettc(self):
        return self.__tc

    def getdistrito(self):
        return self.__distrito

    def getmunicipio(self):
        return self.__municipio

    def getseccion(self):
        return self.__seccion

    def gettv(self):
        return self.__tv

    def getqr(self):
        return self.__qr

    def getfp(self):
        return self.__fp
    
    def __str__(self):
        return self.__casilla

def main():
    Act1 = Actas("-1","1","14","01","001","243","02,14,01,001,1","2026-03-08T10:00:00Z")

    print(Act1)


        


if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        print(error)

