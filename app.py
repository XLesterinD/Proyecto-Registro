from flask import Flask, render_template
from pydoc import render_doc
from flask_mysqldb import MySQL
from Index.index import index_bp
from Planes.Index_planes.index_planes import planes_bp
from Planes.Pagina_pago.pagina_pago import pago_bp
from Usuario.Login.login import login_bp
from Usuario.Sign_up.sign_up import signup

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'bqg0wnfpwadbdjwz3uok-mysql.services.clever-cloud.com'
app.config['MYSQL_USER'] = 'ufb8tcwkdrueue0j'
app.config['MYSQL_PASSWORD'] = 'jOGbe9EOgQHbh1KidwMP'
app.config['MYSQL_DB'] = 'bqg0wnfpwadbdjwz3uok'


conexion = MySQL(app)

signup.mysql = conexion

app.register_blueprint(index_bp)
app.register_blueprint(planes_bp)
app.register_blueprint(pago_bp)
app.register_blueprint(login_bp)
app.register_blueprint(signup)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
