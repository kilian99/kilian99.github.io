
from app.data.modelo.futbolista import Futbolista

class FutbolistasDao:

    def select_all(self,db) -> list[Futbolista]:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Futbolistas')
        equipos_en_db = cursor.fetchall()
        futbolistas : list[Futbolista]= list()
        for equipo in equipos_en_db:
            futbolistas.append(Futbolista(equipo[0], equipo[1], equipo[2], equipo[3], equipo[4], equipo[5], equipo[6], equipo[7]))

        cursor.close()
        return futbolistas
    
    def select_uno(self,db,nombre) -> Futbolista:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM futbolistas where nombre = %s',[nombre])
        equipos_en_db = cursor.fetchall()
        if (equipos_en_db == []):
            return None
        equipo_en_db = equipos_en_db[0]        
        futbolista = Futbolista(equipo_en_db[0], equipo_en_db[1], equipo_en_db[2], equipo_en_db[3], equipo_en_db[4], equipo_en_db[5], equipo_en_db[6], equipo_en_db[7])
        cursor.close()
        return futbolista
    
    def insert(self,db,id,nombre,pais,equipo,dorsal,edad,goles,tarjetas):
        cursor = db.cursor()
        sql = ("INSERT INTO Futbolistas (id,nombre,pais,equipo,dorsal,edad,goles,tarjetas) values (%s,%s,%s,%s,%s,%s,%s,%s) ")
        data = (id,nombre,pais,equipo,dorsal,edad,goles,tarjetas)
        cursor.execute(sql,data)
        db.commit()

    def delete(self,db,id):
        cursor = db.cursor()
        sql = ("delete from Futbolistas where id = %s ")
        data = [id]
        cursor.execute(sql, data)
        db.commit()
        
    def update(self,db,id,nombre,pais,equipo,dorsal,edad,goles,tarjetas):
        cursor = db.cursor()
        sql = ("update Futbolistas set nombre = %s, pais = %s,equipo = %s,dorsal = %s,edad = %s,goles = %s,tarjetas = %s where id = %s ")
        data = [nombre,pais,equipo,dorsal,edad,goles,tarjetas,id]
        cursor.execute(sql, data)
        db.commit()   
           
    def updateNombre(self,db,id,nombre):
        cursor = db.cursor()
        sql = ("update Futbolistas set nombre = %s where id = %s ")
        data = [nombre,id]
        cursor.execute(sql, data)
        db.commit()