class Asignatura:

    def __init__(self, nombre=None, salon="remoto"):
        self._nombre = nombre
        self._salon = salon

    def __str__(self):
        #Defino lo que va a imprimir el __str__
         return str(self._nombre)+" "+str(self._salon)
