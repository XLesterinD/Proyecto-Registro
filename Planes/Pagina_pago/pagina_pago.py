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
        'starter': f'Plan Starter: ideal para comenzar.',
        'pro': f'Plan Pro: acceso completo y soporte premium.',
        'enterprise': f'Plan Enterprise: todo incluido para grandes empresas.'
    }

    precio = {
        'free': {'mensual': 0, 'anual': 0}, 
        'starter': {'mensual': 3, 'anual': 30},
        'pro': {'mensual': 6, 'anual': 65},
        'enterprise': {'mensual': 10, 'anual': 100}
    }


    descripcion = descripciones.get(plan, 'Plan no encontrado')
    precio = precio.get(plan, 'Precio no encontrado')
    return render_template('Pagina_pago.html', plan=plan, descripcion=descripcion, precio=precio)
