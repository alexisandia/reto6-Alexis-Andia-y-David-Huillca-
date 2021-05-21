from config.connection import Connection

class Profesor:
    def __init__(self, id_profesor, nombre, edad, correo, id_salon):
        self.id = id_profesor
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.id_salon = id_salon


    def all_profesor(self):
        try:
            conn = Connection('profesor')
            records = conn.select()
            
            for record in records:
                print(f'ID_profesor: {record[0]}')
                print(f'Nombre: {record[1]}')
                print(f'Edad: {record[2]}')
                print(f'Correo: {record[3]}')
                print(f'ID_salon: {record[4]}')
                print('=====================')
        except Exception as e:
            print(e)

    def insert_profesor(self):
        try:
            conn = Connection('profesor')
            conn.insert({
                'nombre': self.nombre,
                'edad': self.edad,
                'correo': self.correo,
                'id_salon': self.id_salon
            })
            print(f'Se registro el preofesor {self.nombre}')
        except Exception as e:
            print(e)
            
    def update_profesor(self):
        try:
            conn = Connection('profesor')
            conn.update({
                'id': self.id
            }, {
                'nombre': self.nombre,
                'edad': self.edad,
                'correo': self.correo,
                'id_salon': self.id_salon
            })
            print(f'Se cambio datos del profesor: {self.nombre}')
        except Exception as e:
            print(e)
            
#a = Profesor(2, 'Jorge', '40', 'Jorgito@gmail.com', 1)
#a= a.all_profesor()