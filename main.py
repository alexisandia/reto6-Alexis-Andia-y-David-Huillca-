from objeto_alumno import Alumno
from objeto_profesor import Profesor
from objeto_curso import Curso
from objeto_notas import Nota
from objeto_salon import Salon
from objeto_asignaciones import Asignacion


class Principal:
    def __init__(self):
        self.bienvenido()
        self.interfaz()

    def bienvenido(self):
        print ('''
            ____  _                           _     _       
            |  _ \(_)                         (_)   | |      
            | |_) |_  ___ _ ____   _____ _ __  _  __| | ___  
            |  _ <| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \ 
            | |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) |
            |____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/
                ''')

    def interfaz(self):
        while True:
            print(''' 
                ¿Ingrese una opcion?
                1) Alumno
                2) Profesor
                3) Curso
                4) Salon
                5) Notas
                6) Asigancion de cursos
                7) Salir de aplicación\n
            ''')
            opcion = input("> ")
            
            if opcion == "1":
                while True:
                    print(''' 
                    ¿Ingrese una opcion?
                    1) Listar alumnos
                    2) Registrar alumno nuevo
                    3) Editar datos de un alumno
                    4) Atras\n
                    ''')
                    opcion1 = input("> ")
                    if opcion1== "1":
                        self.mostrar_alumno()
                    elif opcion1=="2":
                        self.registrar_alumno()
                    elif opcion1 == "3":
                        self.editar_alumno()
                    elif opcion1 == "4":
                        break
                    else:
                        print("\nIntroduciste una opcion incorrecta")
            
            if opcion == "2":
                while True:
                    print(''' 
                    ¿Ingrese una opcion?
                    1) Listar profesores
                    2) Registrar profesor nuevo
                    3) Editar datos de un profesor
                    4) Atras\n
                    ''')
                    opcion2 = input("> ")
                    if opcion2== "1":
                        self.mostrar_profesor()
                    elif opcion2=="2":
                        self.registrar_profesor()
                    elif opcion2 == "3":
                        self.editar_profesor()
                    elif opcion2 == "4":
                        break
                    else:
                        print("\nIntroduciste una opcion incorrecta")

            if opcion == "3":
                while True:
                    print(''' 
                    ¿Ingrese una opcion?
                    1) Listar cursos
                    2) Registrar curso nuevo
                    3) Editar datos de un curso
                    4) Atras\n
                    ''')
                    opcion3 = input("> ")
                    if opcion3== "1":
                        self.mostrar_curso()
                    elif opcion3=="2":
                        self.registrar_curso()
                    elif opcion3 == "3":
                        self.editar_curso()
                    elif opcion3 == "4":
                        break
                    else:
                        print("\nIntroduciste una opcion incorrecta")

            if opcion == "4":
                while True:
                    print(''' 
                    ¿Ingrese una opcion?
                    1) Listar salones
                    2) Registrar salon nuevo
                    3) Editar datos de un salon
                    4) Atras\n
                    ''')
                    opcion4 = input("> ")
                    if opcion4== "1":
                        self.mostrar_salon()
                    elif opcion4=="2":
                        self.registrar_salon()
                    elif opcion4 == "3":
                        self.editar_salon()
                    elif opcion4 == "4":
                        break
                    else:
                        print("\nIntroduciste una opcion incorrecta")

            if opcion == "5":
                while True:
                    print(''' 
                    ¿Ingrese una opcion?
                    1) Listar Notas de todos los alumnos
                    2) Registrar una nota nuevo
                    3) Editar notas de un alumno
                    4) Atras\n
                    ''')
                    opcion5 = input("> ")
                    if opcion5== "1":
                        self.mostrar_nota()
                    elif opcion5=="2":
                        self.registrar_nota()
                    elif opcion5 == "3":
                        self.editar_nota()
                    elif opcion5 == "4":
                        break
                    else:
                        print("\nIntroduciste una opcion incorrecta")

            if opcion == "6":
                while True:
                    print(''' 
                    ¿Ingrese una opcion?
                    1) Listar Asignaciones de todos los cursos
                    2) Registrar una nueva asignacion
                    3) Editar una asignacion
                    4) Atras\n
                    ''')
                    opcion6 = input("> ")
                    if opcion6== "1":
                        self.mostrar_asignacion()
                    elif opcion6=="2":
                        self.registrar_asignacion()
                    elif opcion6 == "3":
                        self.editar_asignacion()
                    elif opcion6 == "4":
                        break
                    else:
                        print("\nIntroduciste una opcion incorrecta")


            if opcion == "7":
                break

           
    # Metodo para de la clase alumno
    def mostrar_alumno(self):
        a = Alumno( "", "", "", "", "")
        a= a.all_alumno()

    def registrar_alumno(self):
        lista_alumno=["nombre", "edad", "correo" , "id_salon"]
        datos=[]
        for i in lista_alumno:
            dato = input("ingrese" + str(lista_alumno[i]) + " del alumno: ")
            datos.append(dato)
        print("Registrando alumno...")
        a = Alumno( 1 , datos[0], datos[1], datos[2], datos[3])
        a= a.insert_alumno()
        print("Alumno registrado")
      
    def editar_alumno(self):
        lista_alumno=["id", "nombre", "edad", "correo" , "id_salon"]
        datos=[]
        for i in lista_alumno:
            dato = input("ingrese" + str(lista_alumno[i]) + " del alumno: ")
            datos.append(dato)
        print("Actualizando datos del alumno...")
        a = Alumno( datos[0], datos[1], datos[2], datos[3], datos[4])
        a= a.insert_alumno()
        print("Datos actualizados")

    
    # Metodo de la clase profesor
    def mostrar_profesor(self):
        a = Profesor( "", "", "", "", "")
        a= a.all_profesor()

    def registrar_profesor(self):
        nombre = input("ingrese nombre del profesor: ")
        edad = input("ingrese la edad del profesor: ")
        correo = input("ingrese el correo del profesor: ")
        id_salon = input("ingrese el id del salon asociado al profesor: ")
        print("Registrando profesor...")
        a = Profesor( 1, nombre, edad, correo, id_salon)
        a= a.insert_profesor()
        print("Profesor registrando")
        

    def editar_profesor(self):
        id_profesor = input("ingrese el id del profesor a modificar: ")
        nombre = input("ingrese el nuevo nombre del profesor: ")
        edad = input("ingrese la nueva edad del profesor: ")
        correo = input("ingrese el nuevo correo del profesor: ")
        id_salon = input("ingrese el nuevo id del salon asociado al profesor: ")
        print("Actualizando datos del profesor...")
        a = Profesor( id_profesor, nombre, edad, correo, id_salon)
        a= a.update_profesor()
        print("Datos del profesor actualizados")

# Metodos para curso
    def mostrar_curso(self):
        a= Curso("","")
        a= a.all_curso()

    def registrar_curso(self):

        dato=input("ingrese nombre del curso: ")
        print("Registrando curso...")
        a = Curso( 1, dato )
        a= a.insert_curso()
        print("Curso registrado")

    def editar_curso(self):
        id_curso=input("ingrese id del curso: ")
        nombre=input("ingrese el nuevo nombre del curso: ")

        print("Actualizando curso...")
        a = Curso( id_curso, nombre)
        a= a.update_curso()
        print("Curso actualizado")


#Metodos para salon
    def mostrar_salon(self):
        a= Salon("","")
        a= a.all_salon()

    def registrar_salon(self):
        nombre = input("ingrese nombre del salon: ")
        ano_escolar = input("ingrese año escolar del salon: ")
        print("Registrando salon...")
        a = Salon( 1, nombre, ano_escolar)
        a= a.insert_salon()
        print("Salon registrado")

    def editar_salon(self):
        id_salon = input("ingrese ID del salon: ")
        nombre = input("ingrese nuevo nombre del salon: ")
        ano_escolar = input("ingrese nuevo año escolar del salon: ")
        print("Actualizando salon...")
        a = Salon( id_salon, nombre, ano_escolar)
        a= a.update_salon()
        print("Salon actualizado")


#Metodos para asignaciones
    def mostrar_asignacion(self):
        a= Asignacion("","","","")
        a= a.all_asignacion()

    def registrar_asignacion(self):
        id_salon = input("ingrese ID del salon a asignar: ")
        id_curso = input("ingrese ID del curso a asignar: ")
        id_profesor = input("ingrese ID del profesor a asignar: ")
        print("Registrando asignacion...")
        a = Asignacion(1, id_salon, id_curso, id_profesor)
        a= a.insert_asignacion()
        print("Asignacion registrada")

    def editar_asignacion(self):
        id_asignacion = input("ingrese ID de la asignacion: ")
        id_salon = input("ingrese nuevo ID del salon: ")
        id_curso = input("ingrese nuevo ID del curso: ")
        id_profesor = input("ingrese nuevo ID del profesor: ")
        print("Actualizando asignacion...")
        a = Asignacion(id_asignacion, id_salon, id_curso, id_profesor)
        a= a.update_asignacion()
        print("Asignacion actualizada")



        #Metodos para notas
    def mostrar_nota(self):
        a= Nota("","","","")
        a= a.all_nota()

    def registrar_nota(self):
        id_alumno = input("ingrese ID del alumno: ")
        bimestre = input("ingrese el bimestre: ")
        nota = input("ingrese la nota correspondiente: ")
        print("Registrando Nota...")
        a = Nota(1, id_alumno, bimestre, nota)
        a= a.insert_nota()
        print("Nota registrada")

    def editar_nota(self):
        id_nota = input("ingrese ID de la nota a actualizar: ")
        id_alumno = input("ingrese ID nuevo del alumno: ")
        bimestre = input("ingrese el nuevo bimestre: ")
        nota = input("ingrese la nueva nota correspondiente: ")
        print("Actualizando Nota...")
        a = Nota(id_nota, id_alumno, bimestre, nota)
        a= a.update_nota()
        print("Nota actualizada")





# Clase principal para correr el programa
Principal()