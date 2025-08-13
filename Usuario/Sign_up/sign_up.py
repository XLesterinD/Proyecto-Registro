from flask import Flask, jsonify, request, render_template, Blueprint
from flask_mysqldb import MySQL

signup = Blueprint('signup', __name__,
                   template_folder='templates',
                   static_folder='static',
                   static_url_path='/Sign_up/static')

@signup.route('/signup')
def signup_def():
    return render_template('Sign_up.html')
