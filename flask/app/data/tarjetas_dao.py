
from app.data.modelo.tarjeta import Tarjeta
from app.data.modelo.futbolista import Futbolista

class TarjetasDao:

    def select_all(self,db,id_jugador) -> list[Tarjeta]:
        cursor = db.cursor()
        cursor.execute(
            """
            SELECT j.*,e.nombre FROM 
            tarjetas j inner join Futbolistas e on j.id_jugador = e.id
            where j.id_jugador = %s
            """,[id_jugador])
        tarjetas_en_db = cursor.fetchall()
        tarjetas : list[Tarjeta]= list()
        for tarjeta_en_db in tarjetas_en_db:
            tarjetas.append(Tarjeta(tarjeta_en_db[0], tarjeta_en_db[1], tarjeta_en_db[2], tarjeta_en_db[3], tarjeta_en_db[4], tarjeta_en_db[5]))

        cursor.close()
        return tarjetas
    
    def select_uno(self,db,nombre) -> Futbolista:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Futbolistas where nombre = %s',[nombre])
        equipos_en_db = cursor.fetchall()
        if (equipos_en_db == []):
            return None
        equipo = equipos_en_db[0]        
        equipo = Futbolista(equipo[0], equipo[1], equipo[2], equipo[3], equipo[4], equipo[5], equipo[6], equipo[7])
        cursor.close()
        return equipo
