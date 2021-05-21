from config.connection import Connection

class Salon:
    def __init__(self, id_salon, nombre, ano_escolar):
        self.id = id_salon
        self.nombre = nombre
        self.ano_escolar = ano_escolar
    
    def all_salon(self):
        try:
            conn = Connection('salon')
            records = conn.select()
            for record in records:
                print(f'ID: {record[0]}')
                print(f'Nombre: {record[1]}')
                print(f'Año escolar: {record[2]}')
                print('=====')
        except Exception as e:
            print(e)

    def insert_salon(self):
        try:
            conn = Connection('salon')
            conn.insert({
                'nombre': self.nombre,
                'ano_escolar': self.ano_escolar
            })
            print(f'Se registro el salon {self.nombre} con año dec curso {self.ano_escolar}')
        except Exception as e:
            print(e)

    def update_salon(self):
        try:
            conn = Connection('salon')
            conn.update({
                'id': self.id
            }, {
                'nombre': self.nombre,
                'ano_escolar': self.ano_escolar
            })
            print(f'Se cambio el salon: {self.id} con el nombre {self.nombre} y año escolar {self.ano_escolar}')
        except Exception as e:
            print(e)

#a = Salon(3, 'Las estrellitas','3do grado')
#a.insert_salon()
