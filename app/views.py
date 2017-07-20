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


@app.route('/dashboard',methods=["GET","POST"])
def dash():
	return render_template('dashboard.html',title='Dashboard Poncho 2017',title_dashboard='Poncho 2017',user='Daniel Godoy')


@app.route('/report',methods=["GET","POST"])
def report():
	agencia = requests.get('https://sgtur.catamarca.gob.ar/api/v1/agencia/')
	agencias = agencia.json()

	return render_template('report.html',title='Reportes Poncho 2017',title_dashboard='Poncho 2017',user='Daniel Godoy',agencias=agencias)

@app.route('/profile',methods=["GET","POST"])
def profile():
	return render_template('profile.html',title='Perfil de Usuario Poncho 2017',title_dashboard='Poncho 2017',user='Daniel Godoy',about='Se un poco de todo.. y mucho de nada!')

@app.route('/data',methods=["GET","POST"])
def data():
	return render_template('data.html',title='Visualizacion de Datos Poncho 2017',title_dashboard='Poncho 2017',user='Daniel Godoy')


@app.route('/logout')
def logout():
#    session.clear()
    return redirect(url_for('login'))
