import random
from flask import Flask, Blueprint, render_template, request, redirect, url_for

from app import db
from app.data.futbolista_dao import FutbolistasDao
from app.data.tarjetas_dao import TarjetasDao



rutas_futbol = Blueprint("routes", __name__)


@rutas_futbol.route('/')
def index():
    return render_template('index.html')

@rutas_futbol.route('/nueva.html')
def nueva():
    return render_template('nueva.html')

@rutas_futbol.route('/futbol.html')   
def test():
     return render_template('futbol.html')

@rutas_futbol.route('/verFutbolistas')   
def verFutbolistas():
    futbolistas_Dao = FutbolistasDao()

    futbolistas = futbolistas_Dao.select_all(db)

    return render_template('test.html' ,futbolistas=futbolistas)


@rutas_futbol.route('/addFutbolistas', methods=['POST'])   
def addEquipo():
    futbolistas_dao = FutbolistasDao()

    id = request.form['id']
    nombre = request.form['nombre']
    equipo = request.form['equipo']
    dorsal = request.form['dorsal']
    edad = request.form['edad']
    goles = request.form['goles']
    pais = request.form['pais']
    tarjetas = request.form['tarjetas']


    if (id == "" or nombre == "" or equipo == "" or dorsal == "" or edad == "" or goles == "" or pais == "" or tarjetas == ""):
        return redirect(url_for('routes.verFutbolistas'))

    futbolistas_dao.insert(db,id,nombre,equipo,dorsal,edad,goles,pais,tarjetas)
  
    return redirect(url_for('routes.verFutbolistas'))    

@rutas_futbol.route('/delFutbolistas', methods=['POST'])   
def delEquipo():
    futbolistas_dao = FutbolistasDao()

    id = request.form['id']



    futbolistas_dao.delete(db,id)
   
    return redirect(url_for('routes.verFutbolistas'))    

@rutas_futbol.route('/updateFutbolistas', methods=['POST'])   
def updateEquipo():
    futbolistas_dao = FutbolistasDao()

    id = request.form['id']
    nombre = request.form['nombre']
    equipo = request.form['equipo']
    dorsal = request.form['dorsal']
    edad = request.form['edad']
    goles = request.form['goles']
    pais = request.form['pais']
    tarjetas = request.form['tarjetas']

    if (pais == ""):
        futbolistas_dao.updateNombre(db,id,nombre,equipo,dorsal,edad,goles,tarjetas)
    else:
        futbolistas_dao.update(db,id,nombre,equipo,dorsal,edad,goles,pais,tarjetas)
   
    return redirect(url_for('routes.verFutbolistas'))


@rutas_futbol.route('/verTarjetas', methods=['POST','GET'])   
def verTarjetas():
    tarjetas = list()
    colortarjeta = ""
    futbolista_dao = FutbolistasDao()
    futbolistas = futbolista_dao.select_all(db)
    
    if (request.method == 'POST'):
        id_jugador = request.form['id_jugador']
        tarjetas_dao = TarjetasDao()
        tarjetas = tarjetas_dao.select_all(db,id_jugador)
        for futbolista in futbolistas:
            if (futbolista.id == id_jugador):
                print(futbolista)
                colortarjeta  = futbolista.nombre

    
    print(colortarjeta)

    return render_template('tabla2.html',
                           tarjetas = tarjetas,
                           futbolistas=futbolistas,
                           colortarjeta=colortarjeta)
