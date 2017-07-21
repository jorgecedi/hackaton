from flask import Flask, request, render_template, redirect, url_for, session, Response
import requests
from datetime import datetime
from app import app


#Logueo en el dashboard de visualizacion de los datos.
@app.route('/login',methods=["GET","POST"])
def login():
	if request.method == "POST":
		return redirect(url_for(dash))

	return render_template('login.html')

#Dashboard principal de la aplicacion
@app.route('/',methods=["GET","POST"])
@app.route('/dashboard',methods=["GET","POST"])
def dash():
	return render_template('dashboard.html',title='Dashboard Poncho 2017',title_dashboard='Poncho 2017',user='Daniel Godoy')


#Seccion Agencias
@app.route('/agencias',methods=["GET","POST"])
def agencias():
	agencias = requests.get('https://sgtur.catamarca.gob.ar/api/v1/agencia/')
	agencias = agencias.json()
	return render_template('agencias.html',title='Agencias Poncho 2017',title_dashboard='Poncho 2017',user='Daniel Godoy',agencias=agencias)

#Seccion Hospedajes
@app.route('/hospedajes',methods=["GET","POST"])
def hospedajes():
	hospedajes = requests.get('https://sgtur.catamarca.gob.ar/api/v1/hospedaje/')
	hospedajes = hospedajes.json()

	return render_template('hospedajes.html',title='Hospedajes Poncho 2017',title_dashboard='Poncho 2017',user='Daniel Godoy',hospedajes=hospedajes)




#Seccion Hospedajes
@app.route('/detalle_hospedaje',methods=["GET","POST"])
def detalle_hospedaje():
	id = request.args.get("id")
	url = 'https://sgtur.catamarca.gob.ar/api/v1/hospedaje/'
	hospedaje = requests.get(url+id)
	hospedaje = hospedaje.json()

	return render_template('detalle_hospedaje.html',title='Detalle Hospedaje Poncho 2017',title_dashboard='Poncho 2017',user='Daniel Godoy',hospedaje=hospedaje)




#Seccion Guias
@app.route('/guias',methods=["GET","POST"])
def guias():
	guias = requests.get('https://sgtur.catamarca.gob.ar/api/v1/guia/')
	guias = guias.json()

	return render_template('guias.html',title='Guias Poncho 2017',title_dashboard='Poncho 2017',user='Daniel Godoy',guias=guias)

#Seccion Transportes
@app.route('/transportes',methods=["GET","POST"])
def transportes():
	transportes = requests.get('https://sgtur.catamarca.gob.ar/api/v1/transporte/')
	transportes = transportes.json()

	return render_template('transportes.html',title='Transportes Poncho 2017',title_dashboard='Poncho 2017',user='Daniel Godoy',transportes=transportes)


@app.route('/profile',methods=["GET","POST"])
def profile():
	return render_template('profile.html',title='Perfil de Usuario Poncho 2017',title_dashboard='Poncho 2017',user='Daniel Godoy',about='Se un poco de todo.. y mucho de nada!')

@app.route('/data',methods=["GET","POST"])
def data():
	return render_template('data.html',title='Visualizacion de Datos Poncho 2017',title_dashboard='Poncho 2017',user='Daniel Godoy')

@app.route('/mapa', methods=['GET'])
def mapa():
    return render_template('mapa.html', title='Mapa de Datos Poncho 2017', title_dashboard='Poncho 2017', user='Daniel Godoy')


@app.route('/logout')
def logout():
#    session.clear()
    return redirect(url_for('login'))
