class Sistema: 
    def __init__(self):
        self.materias = []
        self.profesores = []
        self.estudiantes = []

        self.corriendo = True #Variable que verifica si se esta ejecutando el bucle del menu de opciones

    def verListas(self): #Asociar las impresiones por pantalla de cada objeto a la clase con __str__()
        print("Lista de todos los estudiantes")
        for estudiante in self.estudiantes: 
            print(estudiante)
            for materia in estudiante.materias: 
                print(materia.nombre)

        print("Lista de todos los profesores")
        for profesor in self.profesores: 
            print(profesor)
        
        print("Lista de todas las materias")
        for materia in self.materias: 
            print(materia)      

    def menu(self): 
        while self.corriendo: 
            entrada = input("Ingrese la opción que desee.\n 1. Cargar nuevo Estudiante.\n 2. Cargar nuevo profesor.\n 3. Cargar nueva materia.\n 4. Inscribir a un Estudiante a una materia.\n 5. Cargar una nota para un estudiante en una materia.\n 6. Asignar un profesor a una materia.\n 7. Mostrar las notas y el promedio de cada materia para un estudiante.\n 8. Listar todos los estudiantes, profesores y materias \n 0. Salir")
            if entrada == "1":
                self.cargarAlumno()
            elif entrada == "2":
                self.cargarProfesor()
            elif entrada == "3":
                self.cargarMateria()
            elif entrada == "4":
                #Buscar el estudiante y la materia 
                estudianteAbuscar = input("Ingrese el nombre del estudiante que desea asignar a una materia")
                materiaAbuscar = input("Ingrese el nombre de la materia")
                estudianteEncontrado = Utilidades.buscar(estudianteAbuscar, self.estudiantes)
                materiaEncontrada = Utilidades.buscar(materiaAbuscar, self.materias)

                estudianteEncontrado.inscribirMateria(materiaEncontrada)
            
            elif entrada == "5": 
                #Buscar el estudiante y la materia dentro de las materias del estudiante 
                estudianteAbuscar = input("Ingrese el nombre del estudiante al que desea cargar una nota")
                materiaAbuscar = input("Ingrese el nombre de la materia")
                estudianteEncontrado = Utilidades.buscar(estudianteAbuscar, self.estudiantes)
                materiaEncontrada = Utilidades.buscar(materiaAbuscar, estudianteEncontrado.materias)
                
                nota = float(input("Ingrese la nota que desea cargar"))
                estudianteEncontrado.cargarNota(materiaEncontrada, nota)

            elif entrada == "6":
                #Buscar profesor y materia
                profesor = input("Ingrese el nombre del profesor que desea asginar a una materia")
                materia = input("Ingrese el nombre de la materia")
                profesorEncontrado = Utilidades.buscar(profesor, self.profesores)
                materiaEncontrada = Utilidades.buscar(materia, self.materias)
                
                materiaEncontrada.profesor = profesorEncontrado
                #Tambien al profesor se le asigna esa materia
                profesorEncontrado.materia = materiaEncontrada

            elif entrada == "7":
                estudianteAbuscar = input("Ingrese el nombre del alumno del que quiere consultar sus notas")
                estudianteEncontrado = Utilidades.buscar(estudianteAbuscar, self.estudiantes)
                estudianteEncontrado.verNotas()
            
            elif entrada == "8": #Listar todos los profesores, materias y alumnos
                self.verListas()

            else: 
                self.corriendo = False

    def cargarAlumno(self):
        nombre = input("Ingrese el nombre del nuevo estudiante")
        dni = input("Ingrese el dni del nuevo estudiante")
        legajo = input("Ingrese el legajo del nuevo estudiante")
                
        nuevo_estudiante = Estudiante(nombre, dni, legajo) #Le paso dos listas vacias que seria las notas y materias para que despues con los otros métodos se carguen
                
        self.estudiantes.append(nuevo_estudiante)
        print("Estudiante creado exitosamente") 
    
    def cargarProfesor(self):
        nombre = input("Ingrese el nombre del nuevo profesor")
        dni = int(input("Ingrese el dni del nuevo profesor"))
                
        nuevo_profesor = Profesor(nombre, dni) #Le paso dos listas vacias que seria las notas y materias para que despues con los otros métodos se carguen
                
        self.profesores.append(nuevo_profesor)
        print("Profesor creado exitosamente")
    
    def cargarMateria(self):
        nombre_materia = input("Ingrese el nombre de la nueva materia")        
        nueva_materia = Materia(nombre_materia) #Para crear una materia solo necesito el nombre
                
        self.materias.append(nueva_materia)
        print("Materia creada exitosamente")

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
        #Suponiendo que la clave es la instancia de Materia
        """

    def __str__(self): #Cómo se va a ver por consola el objeto cuando haga print(objeto)
        return f"Nombre: {self.nombre}\nLegajo: {self.legajo}\nDni: {self.dni}\n Materias: "

    def inscribirMateria(self, materia): 
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
            total_notas = len(datos[1])
            suma = 0
            for nota in datos[1]: #datos[1] seria el valor del diccioanrio que en este caso es una lista con las notas
                suma += nota 
                print(nota)
            promedio = suma/total_notas
            print(f"El promedio de esta materia es: {promedio}")
    
    def cargarNota(self, materia, nota): #Lo mejor sería que profesor tenga esta responsabilidad
        self.notas[materia].append(nota)
        print("La nota se cargó exitosamente")

class Profesor(Persona):
    def __init__(self, nombre, dni):
        super().__init__(nombre, dni)
        self.materia = None #Una única instancia, no es necesaria para instanciar al profesor por eso "None"
    
    def __str__(self): #Cómo se va a ver por consola el objeto cuando haga print(objeto)
        return f"Nombre:{self.nombre}\nDni:{self.dni}\nMateria:{self.materia.nombre}\n" 

class Materia(): 
    def __init__(self, nombre): 
        self.nombre = nombre 
        self.profesor = None #Dejo vacio el atributo de profesor
        self.estudiantes = [] #Tipo lista

    def __str__(self):
        return f"Nombre: {self.nombre}"#Podría mostrar sus alumnos y el profesor a cargo también

class Utilidades(): #Para buscar alternativamente se puede crear un método para cada lista en la clase Sistemas, buscar_profesro(), estudiante, etc.
    @staticmethod #Agrupa funcionaldiades que no requieren acceder a los atributos ni instancias de la clase
    def buscar(nombre_elemento, lista): #Devuelve la instancia de estudiante o materia o profesor dependiendo la lista que le pase 
        for elemento in lista: 
            if nombre_elemento == elemento.nombre:
                return elemento
        print("No se encontró ningún elemento con ese nombre")
        return None
    
sistema = Sistema()
sistema.menu()