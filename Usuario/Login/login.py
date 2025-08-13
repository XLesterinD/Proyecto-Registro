from flask import Flask, jsonify, request, render_template, Blueprint
from flask_mysqldb import MySQL

login = Blueprint('login', __name__,
                   template_folder='templates',
                   static_folder='static',
                   static_url_path='/Login/static')

@login.route('/login', methods=['GET'])
def login_def():
    return render_template('Login.html')