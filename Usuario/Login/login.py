from flask import Flask, jsonify, request, render_template
from flask_mysqldb import MySQL

app = Flask (__name__)

app.config['MYSQL_HOST'] = 'bqg0wnfpwadbdjwz3uok-mysql.services.clever-cloud.com'
app.config['MYSQL_USER'] = 'ufb8tcwkdrueue0j'
app.config['MYSQL_PASSWORD'] = 'jOGbe9EOgQHbh1KidwMP'
app.config['MYSQL_DB'] = 'bqg0wnfpwadbdjwz3uok'

conexion = MySQL(app)

@app.route('/')
def index_login():
    return render_template('Login.html')

@app.route('/login', methods="POST")
def login():
    return 

if __name__ == '__main__':
    app.run(debug=True)
