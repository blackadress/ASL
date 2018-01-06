from flask import Flask, render_template, url_for, request, session, redirect
import bcrypt

app = Flask(__name__)

#Importando configuraciones desde config.py
app.config.from_pyfile('config.py')

#importando los Controladores
from controladores import *

#importando el modelo
from modelo import *

if __name__ == '__main__':
	app.run()