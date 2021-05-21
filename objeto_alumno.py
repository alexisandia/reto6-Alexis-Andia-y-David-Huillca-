from config.connection import Connection

class Alumno:
    def __init__(self, id_alumno, nombre, edad, correo, id_salon):
        self.id = id_alumno
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.id_salon = id_salon


    def all_alumno(self):
        try:
            conn = Connection('alumno')
            records = conn.select()
            
            for record in records:
                print(f'ID: {record[0]}')
                print(f'Nombre: {record[1]}')
                print(f'Edad: {record[2]}')
                print(f'Correo: {record[3]}')
                print(f'ID_salon: {record[4]}')
                print('=====================')
        except Exception as e:
            print(e)

    def insert_alumno(self):
        try:
            conn = Connection('alumno')
            conn.insert({
                'nombre': self.nombre,
                'edad': self.edad,
                'correo': self.correo,
                'id_salon': self.id_salon
            })
            print(f'Se registro el alumno {self.nombre}')
        except Exception as e:
            print(e)
            
    def update_alumno(self):
        try:
            conn = Connection('alumno')
            conn.update({
                'id': self.id
            }, {
                'nombre': self.nombre,
                'edad': self.edad,
                'correo': self.correo,
                'id_salon': self.id_salon
            })
            print(f'Se cambio datos del alumno: {self.nombre}')
        except Exception as e:
            print(e)
            
#a = Alumno(3, 'Juan', '18', 'Juanito@gmail.com', 2)
#a= a.all_alumno()