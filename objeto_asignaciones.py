from config.connection import Connection

class Asignacion:
    def __init__(self, id_asignacion, id_salon, id_curso, id_profesor):
        self.id=id_asignacion
        self.id_salon = id_salon
        self.id_curso = id_curso
        self.id_profesor = id_profesor


    def all_asignacion(self):
        try:
            conn = Connection('asignacion_cursos')
            records = conn.select()
            
            for record in records:
                print(f'ID_asignacion: {record[0]}')
                print(f'ID_salon: {record[1]}')
                print(f'ID_curso: {record[2]}')
                print(f'ID_profesor: {record[3]}')
                print('=====================')
        except Exception as e:
            print(e)

    def insert_asignacion(self):
        try:
            conn = Connection('asignacion_cursos')
            conn.insert({
                'id_salon': self.id_salon,
                'id_curso': self.id_curso,
                'id_profesor': self.id_profesor
            })
            print(f'Se registro asignaciones de: salon {self.id_salon}, curso {self.id_curso} , profesor {self.id_profesor}')
        except Exception as e:
            print(e)
            
    def update_asignacion(self):
        try:
            conn = Connection('asignacion_cursos')
            conn.update({
                'id': self.id
            }, {
                'id_salon': self.id_salon,
                'id_curso': self.id_curso,
                'id_profesor': self.id_profesor
            })
            print(f'Se cambio asignaciones de: salon {self.id_salon}, curso {self.id_curso} , profesor {self.id_profesor}')
        except Exception as e:
            print(e)
            
#a = Asignacion(5, 1, 1,2)
#a= a.update_asignacion()
