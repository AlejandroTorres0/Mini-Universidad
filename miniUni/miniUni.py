class Persona: 
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

class Estudiante(Persona): 
    def __init__(self, nombre, dni, legajo, notas, materias):
        super().__init__(nombre, dni)
        self.legajo = legajo
        self.notas = notas
        self.materias = materias #Tipo lista

    def inscribirseMateria(): 
        print("exito")
    
    def verNotas(): 
        print("2")
    
class Profesor(Persona):
    def __init__(self, nombre, dni, materia):
        super().__init__(nombre, dni)
        self.materia = materia
        

class Materia(): 
    def __init__(self, nombre, profesor, estudiantes): 
        self.nombre = nombre 
        self.profesor = profesor
        self.estudiantes = estudiantes #Tipo lista

salir = True
todos_estudiantes = []
todos_profesor = []
todas_materias = []
while salir == True: 
    entrada = input("Ingrese la opción que desee.\n 1. Cargar nuevo Estudiante.\n 2. Cargar nuevo profesor.\n 3. Cargar nueva materia.\n 4. Inscribir a un Estudiante a una materia.\n 5. Cargar una nota para un estudiante en una materia.\n 6. Asignar un profesor a una materia.\n 7. Mostrar las notas y el promedio de cada materia para un estudiante.\n 8. Listar todos los estudiantes, profesores y materias \n 0. Salir")
    if entrada == "1":
        nombre = input("Ingrese el nombre del nuevo estudiante")
        dni = int(input("Ingrese el dni del nuevo estudiante"))
        legajo = int(input("Ingrese el legajo del nuevo estudiante"))
        nuevo_estudiante = Persona(nombre, dni, legajo, [], []) #Le paso dos listas vacias que seria las notas y materias para que despues con los otros métodos se carguen
        todos_estudiantes.push(nuevo_estudiante)
        print("Estudiante creado exitosamente")
    elif entrada == "2":
        nombre = input("Ingrese el nombre del nuevo profesor")
        dni = int(input("Ingrese el dni del nuevo profesor"))
        materia = int(input("Ingrese la materia del nuevo profesor")) #Solo te deja cargarle una materia
        nuevo_profesor = Profesor(nombre, dni, materia) #Le paso dos listas vacias que seria las notas y materias para que despues con los otros métodos se carguen
        todos_profesores.push(nuevo_estudiante)
        print("Profesor creado exitosamente")
    elif entrada == "3":
        nombre = input("Ingrese el nombre de la nueva materia")
        
        profesor = Profesor(nombre) #Tendria que instanciar un profesor de 0 o lo puedo asignar nomas?
        
        materia = int(input("Ingrese la nueva materia")) #Solo te deja cargarle una materia
        nueva_materia = Materia(nombre, profesor, estudiantes)
        todas_materias.push(nueva_materia)
    elif entrada == "4":
        print("exito")
    else: 
        salir = False
  