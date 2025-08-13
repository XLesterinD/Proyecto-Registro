from flask import Blueprint, render_template, request

index = Blueprint('index', __name__, 
                    template_folder='templates', 
                    static_folder='static', 
                    static_url_path='/Index/static')


@index.route('/index')
def Index():
    return render_template ('Index.html')