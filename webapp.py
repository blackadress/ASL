from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'pruebas'
app.config['MONGO_USERNAME'] = 'root'
app.config['MONGO_PASSWORD'] = '1234'

mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/usuario/inicio_sesion', methods=['POST', 'GET'])
def inicio_sesion():
	if request.method == 'POST':
		usuario = mongo.db.pruebas
		login_user = usuario.find_one({'nick' : request.form['usuario']})
		if login_user:
			if bcrypt.hashpw(request.form['contraseña'].encode('utf-8'), login_user['contraseña']) == login_user['contraseña']:
				session['username'] = request.form['usuario']
				return render_template('/home.html')
		else:
			return render_template('/usuario/inicio_sesion_fallo.html')
	return render_template('/usuario/inicio_sesion.html')

@app.route('/usuario/registro_usuario', methods=['POST','GET'])
def registro_usuario():
	if request.method == 'POST':
		usuario = mongo.db.pruebas
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

@app.route('/primaria')
def primaria():
	return render_template('primaria/home_primaria.html')

@app.route('/primaria/ciencia')
def primaria_ciencia():
	return render_template('primaria/primaria_ciencia.html')

@app.route('/primaria/historia')
def primaria_historia():
	return render_template('primaria/primaria_historia.html')

@app.route('/primaria/matematica')
def primaria_matematica():
	return render_template('primaria/primaria_matematica.html')
	
@app.route('/secundaria/ciencia')
def secundaria_ciencia():
	return render_template('secundaria/secundaria_ciencia.html')
	
@app.route('/secundaria/economia')
def secundaria_economia():
	return render_template('secundaria/secundaria_economia.html')
	
@app.route('/secundaria/historia')
def secundaria_historia():
	return render_template('secundaria/secundaria_historia.html')
	
@app.route('/secundaria/matematica')
def secundaria_matematica():
	return render_template('secundaria/secundaria_matematica.html')
	
@app.route('/universidad/ciencia')
def universidad_ciencia():
	return render_template('universidad/universidad_ciencia.html')
	
@app.route('/universidad/economia')
def universidad_economia():
	return render_template('universidad/universidad_economia.html')
	
@app.route('/universidad/historia')
def universidad_historia():
	return render_template('universidad/universidad_historia.html')
	
@app.route('/universidad/matematica')
def universidad_matematica():
	return render_template('universidad/universidad_matematica.html')

if __name__ == '__main__':
	app.secret_key = 'super secret'
	#app.config['SESSION_TYPE'] = 'mongodb'

	app.run(debug=True)