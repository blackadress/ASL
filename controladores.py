from webapp import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')

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