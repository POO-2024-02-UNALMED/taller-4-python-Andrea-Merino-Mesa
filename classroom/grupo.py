from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"
    #Cambio el None por 12 para que coincida con la impresión
    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        #Cambié ordinado por predeterminado porque es lo que muestra al imprimir grupo 1
        #Pongo estudiantes=None por si no se pasa ese argumento se quede con ese valor
        #Además que si pongo una lista, esta es mutable y me acumularía los datos
        if asignaturas is None:
            asignaturas = []
        if estudiantes is None:
            estudiantes= []
            #Como asignaturas esun atributo que recibe listas, si no se pasa toca crearla
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        #Le faltaban los asteriscos a kwargs
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        #Cambio lista=[] por None para que no se acumulen datos de objetos diferentes en la misma lista
        if lista is None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    def __str__(self):
        #Defino lo que va a imprimir el __str__
        return "Grupo de estudiantes: "+str(self._grupo)

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre
    #No es necesario comentarla ya que Python solo toma en cuenta el último de los métodos si hay varios iguales
    
    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    #@ classmethod
    #def asignarNombre(cls, nombre="Grado 4"):
        #cls.grado = nombre
    #Porque en Python no hay sobrecarga sino que se toma el último de los métodos si hay varios iguales
    #Como queremos que imprima grupo 6, comentamos esta función
