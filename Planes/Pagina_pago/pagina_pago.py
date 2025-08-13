from flask import Blueprint, render_template, request

pago_bp = Blueprint('pagina_pago', __name__, 
                    template_folder='templates', 
                    static_folder='static', 
                    static_url_path='/Pagina_pago/static')

@pago_bp.route('/pago')
def pago():
    plan = request.args.get('plan', 'free')

    descripciones = {
        'free': 'Plan Free: acceso limitado pero gratis.',
        'starter': 'Plan Starter: ideal para comenzar.',
        'pro': 'Plan Pro: acceso completo y soporte premium.',
        'enterprise': 'Plan Enterprise: todo incluido para grandes empresas.'
    }

    descripcion = descripciones.get(plan, 'Plan no encontrado')
    return render_template('Pagina_pago.html', plan=plan, descripcion=descripcion)
