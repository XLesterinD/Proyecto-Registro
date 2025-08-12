from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL
import requests
import json

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'bnme9sfdxfbeid2jdknd-mysql.services.clever-cloud.com'
app.config['MYSQL_USER'] = 'u5gywpg3gymmsuku'
app.config['MYSQL_PASSWORD'] = 'QVKIYfrleZBkE5cWZ7Vy'
app.config['MYSQL_DB'] = 'bnme9sfdxfbeid2jdknd'

conexion = MySQL(app)

@app.route('/buscar_elemento', methods=['POST'])
def solicitar_datos():
    
    data = request.get_json()
    id = data.get('id')

    try:
        cursor = conexion.connection.cursor()
        query = 'SELECT id, nombre, altura, peso, habilidades, fecha FROM historial_busqueda_pokemon WHERE id=%s'
        cursor.execute(query, (id,))
        data = cursor.fetchall()

        if data: 
            return jsonify(data)
        else:
            return f'Error'
    
    except Exception as ex:
        return f'Error en la busqueda: {str(ex)}', 500
    
if __name__ == '__main__':
    app.run(debug=True)