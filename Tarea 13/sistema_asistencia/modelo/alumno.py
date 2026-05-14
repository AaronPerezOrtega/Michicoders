class Alumno:
    def __init__(self,nombre,grupo,materia,presente):
        self.nombre = nombre
        self.grupo = grupo
        self.materia = materia
        self.presente = presente
    
    def __str__(self):
        estado = "Presente" if self.presente else "Ausete"
        return f"{self.nombre}. Del Grupo: {self.grupo} - {estado} en {self.materia}"