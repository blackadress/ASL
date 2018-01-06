from webapp import app
from pymongo import MongoClient
from flask import Flask, render_template, url_for, request, session, redirect
import bcrypt

#Definiendo la conexión a la base de datos
cliente = MongoClient('localhost', 27017)
#definiendo la DB
db = cliente.pruebas
#Accesos a las colecciones de la base de datos
usuario = db.usuario
videos = db.videos
##Registro de usuario
@app.route('/usuario/registro_usuario', methods=['POST','GET'])
def registro_usuario():
	if request.method == 'POST':
		usuario_existente = usuario.find_one({'nick' : request.form['usuario']})

		if usuario_existente is None:
			contraseña_hash = bcrypt.hashpw(request.form['contraseña'].encode('utf-8'), bcrypt.gensalt())
			usuario.insert({'nick' : request.form['usuario'],
							'contraseña' : contraseña_hash, 
							'email' : request.form['email']
							})
			session['username'] = request.form['usuario']
			return render_template('/home.html')

		return render_template('/usuario/registro_nombre_invalido.html')

	return render_template('/usuario/registro_usuario.html')

##Inicio de sesión
@app.route('/usuario/inicio_sesion', methods=['POST', 'GET'])
def inicio_sesion():
	if request.method == 'POST':
		login_user = usuario.find_one({'nick' : request.form['usuario']})
		if login_user:
			if bcrypt.hashpw(request.form['contraseña'].encode('utf-8'), login_user['contraseña']) == login_user['contraseña']:
				session['username'] = request.form['usuario']
				return render_template('/home.html')
		else:
			return render_template('/usuario/inicio_sesion_fallo.html')
	return render_template('/usuario/inicio_sesion.html')