from flask import Flask, jsonify, request, render_template, Blueprint
from flask_mysqldb import MySQL

signup = Blueprint('signup', __name__,
                   template_folder='templates',
                   static_folder='static',
                   static_url_path='/Sign_up/static')

@signup.route('/signup')
def signup_def():
    return render_template('Sign_up.html')

@signup.route('/registrarse', methods=['POST'])
def sign_up_registro():
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    correo = request.form.get('correo')
    contrasena = request.form.get('contrasena')
    telefono = request.form.get('telefono')
    pais = request.form.get('pais')

    try: 

        cursor = signup.mysql.connection.cursor()
        query = '''INSERT INTO usuarios (nombre_usuario, apellido_usuario, correo_usuario, contrasena_usuario, telefono_usuario, pais_usuario)
        VALUES (%s, %s, %s, %s, %s, %s)'''
        cursor.execute(query, (nombre, apellido, correo, contrasena, telefono, pais,))
        signup.mysql.connection.commit()
        cursor.close()

        return render_template("Login.html", mensaje="Usuario registrado exitosamente"), 200


    except Exception as ex: 
        return f"Error: {str(ex)}", 500