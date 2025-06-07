class Persona: 
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

class Estudiante(Persona): 
    def __init__(self, nombre, dni, legajo):
        super().__init__(nombre, dni)
        self.legajo = legajo
        self.notas = {} #Tipo direccionario
        self.materias = [] #Tipo lista
        
        """
        Ejemplo
        notas = {
            'Álgebra y Geometría Analítica': [5, 7, 2],  
            'Paradigmas de programación': [1, 3, 9] 
        } 
        #Suponiendo que la clave es solo el nombre y no la instancia de Materia
        """

    def inscribirseMateria(self, materia): 
        self.materias.append(materia)
        print("Se inscribió correctamente")
        #También hay que cargar esa materia al diccionario de notas, con la lista de notas vacia
        self.notas[materia] = [] #Inicia vacío
        #También hay que cargar al estudiante en la lista de estudiantes de la materia
        materia.estudiantes.append(self)

    def verNotas(self):
        print(f"Notas del alumno/a {self.nombre}") 
        for datos in self.notas.items():
            print(f"Notas de la materia '{datos[0].nombre}'")
            #datos[0] seria la instancia materia, que seria la clave
            total_materias = len(datos[1]) #O len(self.materias) también
            suma = 0
            for nota in datos[1]: #datos[1] seria el valor del diccioanrio que en este caso es una lista con las notas
                suma += nota 
                print(nota)
            promedio = suma/total_materias
            print(f"El promedio de esta materia es: {promedio}")

class Profesor(Persona):
    def __init__(self, nombre, dni):
        super().__init__(nombre, dni)
        self.materia = None #Una única instancia, no es necesaria para instanciar al profesor por eso "None"


class Materia(): 
    def __init__(self, nombre): 
        self.nombre = nombre 
        self.profesor = None #Dejo vacio el atributo de profesor
        self.estudiantes = [] #Tipo lista


def buscar(nombre_elemento, lista): #Devuelve la instancia de estudiante o materia o profesor dependiendo la lista que le pase 
    for elemento in lista: 
        if nombre_elemento == elemento.nombre:
            return elemento
    print("No se encontró ningun elemento con ese nombre")
    return None

salir = True
todos_estudiantes = []
todos_profesores = []
todas_materias = []

while salir == True: 
    entrada = input("Ingrese la opción que desee.\n 1. Cargar nuevo Estudiante.\n 2. Cargar nuevo profesor.\n 3. Cargar nueva materia.\n 4. Inscribir a un Estudiante a una materia.\n 5. Cargar una nota para un estudiante en una materia.\n 6. Asignar un profesor a una materia.\n 7. Mostrar las notas y el promedio de cada materia para un estudiante.\n 8. Listar todos los estudiantes, profesores y materias \n 0. Salir")
    if entrada == "1":
        nombre = input("Ingrese el nombre del nuevo estudiante")
        dni = input("Ingrese el dni del nuevo estudiante")
        legajo = input("Ingrese el legajo del nuevo estudiante")
        
        nuevo_estudiante = Estudiante(nombre, dni, legajo) #Le paso dos listas vacias que seria las notas y materias para que despues con los otros métodos se carguen
        
        todos_estudiantes.append(nuevo_estudiante)
        print("Estudiante creado exitosamente")

    elif entrada == "2":
        nombre = input("Ingrese el nombre del nuevo profesor")
        dni = int(input("Ingrese el dni del nuevo profesor"))
        
        nuevo_profesor = Profesor(nombre, dni) #Le paso dos listas vacias que seria las notas y materias para que despues con los otros métodos se carguen
        
        todos_profesores.append(nuevo_profesor)
        print("Profesor creado exitosamente")
    
    elif entrada == "3":
        nombre_materia = input("Ingrese el nombre de la nueva materia")        
        nueva_materia = Materia(nombre_materia) #Para crear una materia solo necesito el nombre
        todas_materias.append(nueva_materia)
        print("Materia creada exitosamente")

    elif entrada == "4":
        #Buscar el estudiante y la materia 
        estudianteAbuscar = input("Ingrese el nombre del estudiante que desea asignar a una materia")
        materiaAbuscar = input("Ingrese el nombre de la materia")
        estudianteEncontrado = buscar(estudianteAbuscar, todos_estudiantes)
        materiaEncontrada = buscar(materiaAbuscar, todas_materias)

        estudianteEncontrado.inscribirseMateria(materiaEncontrada)
    elif entrada == "5":
        #Buscar el estudiante y la materia dentro de las materias del estudiante 
        estudianteAbuscar = input("Ingrese el nombre del estudiante al que desea cargar una nota")
        materiaAbuscar = input("Ingrese el nombre de la materia")
        estudianteEncontrado = buscar(estudianteAbuscar, todos_estudiantes)
        materiaEncontrada = buscar(materiaAbuscar, estudianteEncontrado.materias)

        nota = float(input("Ingrese la nota que desea cargar"))
        estudianteEncontrado.notas[materiaEncontrada].append(nota)

    elif entrada == "6": 
        profesor = input("Ingrese el nombre del profesor que desea asginar a una materia")
        #Buscar profesor
        profesorEncontrado = buscar(profesor, todos_profesores)

        materia = input("Ingrese el nombre de la materia")
        #Buscar materia
        materiaEncontrada = buscar(materia, todas_materias)
        
        materiaEncontrada.profesor = profesorEncontrado

        #Tambien al profesor se le asigna esa materia
        profesorEncontrado.materia = materiaEncontrada

    elif entrada == "7":
        estudianteAbuscar = input("Ingrese el nombre del alumno del que quiere consultar sus notas")
        estudianteEncontrado = buscar(estudianteAbuscar, todos_estudiantes)
        estudianteEncontrado.verNotas()
    
    elif entrada == "8": #Listar todos los profesores, materias y alumnos
        print("Lista de todos los estudiantes")
        for estudiante in todos_estudiantes: 
            print(f"Nombre: {estudiante.nombre}\nLegajo: {estudiante.legajo}\ndni: {estudiante.dni}\n")
            for materia in estudiante.materias: 
                print(materia.nombre)

        print("Lista de todos los profesores")
        for profesor in todos_profesores: 
            print(f"Nombre: {profesor.nombre}\ndni:{profesor.dni}\nmateria:{profesor.materia.nombre}\n")
        
        print("Lista de todas las materias")
        for materia in todas_materias: 
            print(f"Nombre: {materia.nombre}")#Podría mostrar sus alumnos y el profesor a cargo también
    else: 
        salir = False

        