from config.connection import Connection

class Curso:
    def __init__(self, id_curso, nombre):
        self.id = id_curso
        self.nombre = nombre
    
    def all_curso(self):
        try:
            conn = Connection('curso')
            records = conn.select()
            for record in records:
                print(f'ID: {record[0]}')
                print(f'Nombre: {record[1]}')
                print('=====')
        except Exception as e:
            print(e)

    def insert_curso(self):
        try:
            conn = Connection('curso')
            conn.insert({
                'nombre': self.nombre
            })
            print(f'Se registro el curso {self.nombre}')
        except Exception as e:
            print(e)

    def update_curso(self):
        try:
            conn = Connection('curso')
            conn.update({
                'id': self.id
            }, {
                'nombre': self.nombre
            })
            print(f'Se cambio el curso: {self.id} con el nombre {self.nombre}')
        except Exception as e:
            print(e)

#a = Curso(2, 'Biologia')
#a.all_curso()
