import random
from flask import Flask, Blueprint, render_template, request, redirect, url_for

from app import db
from app.data.tarjetas_dao import TarjetasDao


rutas_equipos = Blueprint("routes_equipos", __name__)


@rutas_equipos.route('/verTabla')   
def verTabla():
    tarjetas_dao = TarjetasDao()

    tarjetas = tarjetas_dao.select_all(db)
   
    return render_template('tabla2.html' ,tarjetas=tarjetas) 


@rutas_equipos.route('/addTarjetas', methods=['POST'])   
def addEquipo():
    tarjetas_dao = TarjetasDao()

    id = request.form['id']
    rival = request.form['rival']
    color = request.form['color']
    minuto = request.form['minuto']
    fecha = request.form['fecha']
    id_jugador = request.form['id_jugador']
    

    if (id == "" or rival == "" or color == "" or minuto == "" or fecha == "" or id_jugador == "" ):
        return redirect(url_for('routes_tarjetas./verTabla'))

    tarjetas_dao.insert(db,id,rival,color,minuto,fecha,id_jugador)
  
    return redirect(url_for('routes_tarjetas./verTabla'))    

@rutas_equipos.route('/delTarjetas', methods=['POST'])   
def delEquipo():
    tarjetas_dao = TarjetasDao()

    id = request.form['id']



    tarjetas_dao.delete(db,id)
   
    return redirect(url_for('routes_tarjetas./verTabla'))    

@rutas_equipos.route('/updateTarjetas', methods=['POST'])   
def updateEquipo():
    tarjetas_dao = TarjetasDao()

    id = request.form['id']
    rival = request.form['rival']
    color = request.form['color']
    minuto = request.form['minuto']
    fecha = request.form['fecha']
    id_jugador = request.form['id_jugador']

    if (rival == ""):
        tarjetas_dao.updateNombre(db,id,rival,color,minuto,fecha,id_jugador)
    else:
        tarjetas_dao.update(db,id,rival,color,minuto,fecha,id_jugador)
   
    return redirect(url_for('routes_tarjetas./verTabla'))