from flask import Blueprint, render_template

index_bp = Blueprint(
    'index_planes',
    __name__,
    template_folder='templates',
    static_folder='static', 
    static_url_path='/index_planes/static'
)

@index_bp.route('/planes')
def index_planes():
    return render_template('index_planes.html')
