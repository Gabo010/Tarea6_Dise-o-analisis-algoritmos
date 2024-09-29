import random


# Nodo del Árbol Binario de Búsqueda
class NodoAlumno:
    def __init__(self, num_cuenta, nombre, edad, correo, semestre, materias, promedio):
        self.num_cuenta = num_cuenta
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.semestre = semestre
        self.materias = materias
        self.promedio = promedio
        self.izq = None
        self.der = None


# Árbol Binario de Búsqueda
class ArbolAlumnos:
    def __init__(self):
        self.raiz = None

    # Insertar un alumno en el árbol
    def insertar(self, alumno):
        if self.raiz is None:
            self.raiz = alumno
        else:
            self._insertar_recursivo(self.raiz, alumno)

    def _insertar_recursivo(self, nodo_actual, alumno):
        if alumno.num_cuenta < nodo_actual.num_cuenta:
            if nodo_actual.izq is None:
                nodo_actual.izq = alumno
            else:
                self._insertar_recursivo(nodo_actual.izq, alumno)
        else:
            if nodo_actual.der is None:
                nodo_actual.der = alumno
            else:
                self._insertar_recursivo(nodo_actual.der, alumno)

    # Buscar un alumno por número de cuenta
    def buscar(self, num_cuenta):
        return self._buscar_recursivo(self.raiz, num_cuenta)

    def _buscar_recursivo(self, nodo_actual, num_cuenta):
        if nodo_actual is None or nodo_actual.num_cuenta == num_cuenta:
            return nodo_actual
        elif num_cuenta < nodo_actual.num_cuenta:
            return self._buscar_recursivo(nodo_actual.izq, num_cuenta)
        else:
            return self._buscar_recursivo(nodo_actual.der, num_cuenta)


# Función para generar alumnos aleatorios
def generar_alumnos(n):
    nombres = ["Lucas","Mateo","Santiago","Tomás","Nicolás","Sebastián","Martín","Andrés","Joaquín","Valentín","Alejandro",
               "Ignacio","Daniel","Emilio","Felipe","Rodrigo","Carlos","Adrián","Miguel","Diego","Fernando","Pablo","César",
               "Javier","Rubén","Raúl","Esteban","Alfonso","Gabriel","Héctor","Luis","Manuel","Óscar","Ricardo","Alberto",
               "Enrique","Antonio","Cristian","Damián","David","Eduardo","Federico","Germán","Hugo","Ismael","Iván","Jacobo",
               "Jaime","José","Leonardo","Marcos","Maximiliano","Orlando","Patricio","Ramiro","Salvador","Vicente","Ángel",
               "Bruno","Rafael","Sergio","Francisco","Gonzalo","Guillermo","Hernán","Isidro","Jorge","Leandro","Lorenzo",
               "Mauricio","Nelson","Octavio","Pascual","Renato","Simón","Teodoro","Ulises","Vasco","Walter","Xavier","Yago",
               "Zacarías","Aaron","Bernardo","Bautista","Clemente","Domingo","Esteban","Fabián","Gerardo","Humberto","Iker",
               "Jonás","Kevin","Lázaro","Mariano","Norberto","Omar","Pío","Quirino","Rigoberto","Samuel"]

    apellidos = ["González","Rodríguez","García","Fernández","López","Martínez","Pérez","Sánchez","Romero","Díaz","Torres",
                 "Ruiz","Ramírez","Flores","Benítez","Acosta","Medina","Suárez","Herrera","Molina","Castro","Ortiz","Silva",
                 "Núñez","Rojas","Vargas","Gómez","Cabrera","Morales","Castillo","Ramos","Jiménez","Ibarra","Moreno","Vega",
                 "Sosa","Cáceres","Ponce","Aguirre","Valdez","Navarro","Domínguez","Vázquez","Carrizo","Salinas","Cruz",
                 "Paredes","Muñoz","Méndez","Figueroa","Escobar","Pizarro","Arias","Bravo","Reyes","Peña","Campos","Correa",
                 "Olivares","Sepúlveda","Alarcón","Sandoval","Palacios","Cardozo","Bustos","Luna","Mendoza","Peralta","Araya",
                 "Soto","Montes","Barrios","Gallardo","Varela","Cortés","Ríos","Orellana","Zamora","Villalba","Cuevas",
                 "Espinoza","Franco","Miranda","Cáceres","Alonso","Báez","Carrasco","Farfán","Hidalgo","Infante","Lagos",
                 "Pereira","Quintana","Rivera","Salazar","Tapia","Vidal","Yáñez","Zárate","Delgado","Bravo","Padilla","Sierra",
                 "Vallejo"]

    materias_lista = ["Matemáticas", "Gestion de Proyectos", "Programación", "Cálculo", "Bases de Datos",
                      "Redes", "Inteligencia Artificial", "Emprendimiento", "Algoritmos", "Sistemas Operativos"]

    arbol = ArbolAlumnos()
    numeros_de_cuenta = random.sample(range(100000000, 399999999), n)  # Generar números de cuenta únicos

    for i in range(n):
        nombre_completo = f"{random.choice(nombres)} {random.choice(apellidos)} {random.choice(apellidos)}"
        edad = random.randint(18, 25)
        correo = f"{nombre_completo.split()[0].lower()}{numeros_de_cuenta[i]}@aragon.unam.mx"
        semestre = random.randint(1, 9)
        materias = random.sample(materias_lista, 5)
        promedio = round(random.uniform(5.0, 10.0), 2)

        alumno = NodoAlumno(numeros_de_cuenta[i], nombre_completo, edad, correo, semestre, materias, promedio)
        arbol.insertar(alumno)

        # Mostrar la información generada de cada alumno
        print(f"Alumno {i + 1}:")
        print(f"  Número de cuenta: {numeros_de_cuenta[i]}")
        print(f"  Nombre: {nombre_completo}")
        print(f"  Edad: {edad}")
        print(f"  Correo: {correo}")
        print(f"  Semestre: {semestre}")
        print(f"  Materias: {', '.join(materias)}")
        print(f"  Promedio: {promedio}")
        print()

    return arbol


# Mostrar información del alumno
def mostrar_informacion(alumno):
    if alumno:
        print(f"Nombre: {alumno.nombre}")
        print(f"Materias: {', '.join(alumno.materias)}")
        print(f"Promedio: {alumno.promedio}")
    else:
        print("Alumno no encontrado.")


# Función principal para interactuar con el usuario
def menu(arbol):
    while True:
        print("\n--- Menú ---")
        print("1. Insertar nuevo alumno")
        print("2. Buscar alumno por número de cuenta")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre completo: ")
            edad = int(input("Edad: "))
            correo = input("Correo electrónico: ")
            semestre = int(input("Semestre (1-9): "))
            materias = input("Ingresa 5 materias separadas por comas: ").split(",")
            promedio = float(input("Promedio general: "))
            num_cuenta = int(input("Número de cuenta: "))

            nuevo_alumno = NodoAlumno(num_cuenta, nombre, edad, correo, semestre, materias, promedio)
            arbol.insertar(nuevo_alumno)
            print(f"Alumno con número de cuenta {num_cuenta} insertado con éxito.")

        elif opcion == "2":
            num_cuenta = int(input("Ingresa el número de cuenta del alumno: "))
            alumno = arbol.buscar(num_cuenta)
            mostrar_informacion(alumno)

        elif opcion == "3":
            break
        else:
            print("Opción no válida.")


arbol = generar_alumnos(100)
menu(arbol)
