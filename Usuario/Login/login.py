from flask import Flask, jsonify, request, render_template, Blueprint
from flask_mysqldb import MySQL

login_bp = Blueprint('login', __name__,
                   template_folder='templates',
                   static_folder='static',
                   static_url_path='/Login/static')

@login_bp.route('/login', methods=['GET', 'POST'])
def login_def():
    return render_template('Login.html')