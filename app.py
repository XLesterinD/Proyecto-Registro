from flask import Flask, render_template
from pydoc import render_doc
from Index.index import index_bp
from Planes.Index_planes.index_planes import planes_bp
from Planes.Pagina_pago.pagina_pago import pago_bp
from Usuario.Login.login import login_bp
from Usuario.Sign_up.sign_up import signup

app = Flask(__name__)

app.register_blueprint(index_bp)
app.register_blueprint(planes_bp)
app.register_blueprint(pago_bp)
app.register_blueprint(login_bp)
app.register_blueprint(signup)

if __name__ == '__main__':
    app.run(debug=True)
