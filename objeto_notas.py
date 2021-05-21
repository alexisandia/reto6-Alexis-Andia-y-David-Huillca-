from config.connection import Connection

class Nota:
    def __init__(self, id_nota, id_alumno, bimestre, nota):
        self.id=id_nota
        self.id_alumno = id_alumno
        self.bimestre = bimestre
        self.nota = nota


    def all_nota(self):
        try:
            conn = Connection('notas')
            records = conn.select()
            
            for record in records:
                print(f'ID_nota: {record[0]}')
                print(f'ID_alumno: {record[1]}')
                print(f'bimestre: {record[2]}')
                print(f'nota: {record[3]}')
                print('=====================')
        except Exception as e:
            print(e)

    def insert_nota(self):
        try:
            conn = Connection('notas')
            conn.insert({
                'id_alumno': self.id_alumno,
                'bimestre': self.bimestre,
                'nota': self.nota
            })
            print(f'Se registro notas del alumno de id {self.id_alumno}')
        except Exception as e:
            print(e)
            
    def update_nota(self):
        try:
            conn = Connection('notas')
            conn.update({
                'id': self.id
            }, {
                'id_alumno':self.id_alumno,
                'bimestre': self.bimestre,
                'nota': self.nota
            })
            print(f'Se cambio notas del alumno de id: {self.id_alumno}')
        except Exception as e:
            print(e)
            
#a = Nota(2, 3, 2, 19)
#a= a.all_nota()