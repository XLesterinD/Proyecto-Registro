from flask import Blueprint, render_template, request

index_bp = Blueprint('index_bp', __name__, 
                    template_folder='templates', 
                    static_folder='static', 
                    static_url_path='/Index/static')


@index_bp.route('/')
def index_page():
    return render_template ('Index.html')