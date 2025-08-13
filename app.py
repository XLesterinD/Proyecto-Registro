from flask import Flask, render_template
from pydoc import render_doc
from Index.index import index
from Planes.Index_planes.index_planes import index_bp
from Planes.Pagina_pago.pagina_pago import pago_bp
from Usuario.Login.login import login
from Usuario.Sign_up.sign_up import signup

app = Flask(__name__)

app.register_blueprint(index)
app.register_blueprint(index_bp)
app.register_blueprint(pago_bp)
app.register_blueprint(login)
app.register_blueprint(signup)

if __name__ == '__main__':
    app.run(debug=True)
