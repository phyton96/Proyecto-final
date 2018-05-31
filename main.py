from flask import Flask, request, g, redirect, url_for, render_template, flash, session
import flask
import sys
from flask import json
import random

app=Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/', methods=['GET', 'POST'])
def index():
	"""
	"""
	error=""
	if (request.method == 'POST'):
		if (request.form['enviar'] == "Iniciar Sesión"):
			if (request.form['Usuario'] != "" and request.form['Contraseña'] != ""):
				usuario = str(request.form['Usuario'])
				contraseña = str(request.form['Contraseña'])
				info = open("login.txt", "r")
				data = info.readlines()
				info.close()
				b = 0	
				while (b < len(data)):
					if (usuario + "\n"  == str(data[b])):
						if(contraseña + "\n" == str(data[b+1])):
							return redirect(url_for('juego'))
						else:
							error="Contraseña incorrecta o usuario no registrado"
					b+=2


	return render_template('index.html',error=error)


@app.route('/registro', methods=['GET','POST'])
def registro():
	"""
	"""
	fallo=""
	if (request.method == 'POST'):
		if (request.form['enviar'] == "Registrarse"):
				if (request.form['Usuario'] != "" and request.form['Contraseña'] != ""):
					
					abrir=open("login.txt","r")
					a=abrir.readlines()
					abrir.close()
					usuario = str(request.form['Usuario'])
					contraseña = str(request.form['Contraseña'])
					conteo=False
					b=0
					while(b<len(a)):
						if (usuario + "\n"  == str(a[b])):
							conteo=True
						b+=2

					if(conteo==False):

						usuario = request.form['Usuario']
						contraseña = request.form['Contraseña']
						abierto= open("login.txt", "a")
						abierto.write(str(usuario) + "\n")
						abierto.write(str(contraseña) + "\n")
						abierto.close()
						return redirect(url_for('index'))
						fallo=""
					else:
						fallo="El usuario ya se encuentra registrado"

	return render_template('registro.html',fallo=fallo)



@app.route('/juego',  methods=['GET', 'POST'])
def juego():
	"""
	Descripción:Muestra el tablero y permite al usuario interactuar con los dados.
	Entrada:Presionar el boton de lanzar para obtener un valor entre 2 a 12 con los dados.
	Salida:Permite la visualizacion de el valor de los dados a traves de imagenes.
	"""
	dado1=0
	dado2=0
	if (request.method == 'POST'):
		if (request.form['Tirar'] == "Tirar"):
			dado1=random.randint(1,6)
			dado2=random.randint(1,6)
			R=dado1+dado2
	d1={'dado1':dado1,'dado2':dado2}
	
	return render_template('pagina_juego.html',d1=d1)

if __name__ == '__main__':
	app.run(debug=True)