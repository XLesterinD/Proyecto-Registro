from flask import Blueprint, render_template, request, redirect, url_for
import requests
import json

pago_bp = Blueprint('pagina_pago', __name__,
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/Pagina_pago/static')

# Configuración QPayPro
QPAY_LOGIN = "WIoCLSC5JT2t4896"
QPAY_API_KEY = "811TVueoGPZS4896"
QPAY_SANDBOX = False  # True para pruebas, False para producción
QPAY_RELAY_URL = "https://3360773e3e4e.ngrok-free.app/confirmado"  # URL a donde volverá al finalizar

@pago_bp.route('/pago', methods=['GET'])
def pago():
    plan = request.args.get('plan', 'free')

    descripciones = {
        'free': 'Plan Free: acceso limitado pero gratis.',
        'starter': 'Plan Starter: ideal para comenzar.',
        'pro': 'Plan Pro: acceso completo y soporte premium.',
        'enterprise': 'Plan Enterprise: todo incluido para grandes empresas.'
    }

    precios = {
        'free': {'mensual': 0, 'anual': 0}, 
        'starter': {'mensual': 1, 'anual': 30},
        'pro': {'mensual': 6, 'anual': 65},
        'enterprise': {'mensual': 10, 'anual': 100}
    }

    return render_template('Pagina_pago.html', 
                           plan=plan, 
                           descripcion=descripciones.get(plan, 'Plan no encontrado'),
                           precio=precios.get(plan))

@pago_bp.route('/procesar-pago', methods=['POST'])
def procesar_pago():
    
    # Recibir datos del formulario
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    email = request.form.get('correo')
    telefono = request.form.get('telefono')
    direccion = request.form.get('direccion')
    ciudad = request.form.get('ciudad')
    estado = request.form.get('ciudad')  # algunos ejemplos usan el mismo para estado
    zip_code = request.form.get('zip')
    pais = request.form.get('pais')
    nit = request.form.get('nit', 'C/F')
    plan = request.form.get('plan')
    tipo_pago = request.form.get('tipo_pago')
    precio = request.form.get('precio')

    # Payload según el ejemplo que compartiste
    payload = {
        "x_login": QPAY_LOGIN,
        "x_api_key": QPAY_API_KEY,
        "x_amount": str(precio),
        "x_currency_code": "GTQ",
        "x_first_name": nombre,
        "x_last_name": apellido,
        "x_phone": telefono,
        "x_ship_to_address": direccion,
        "x_ship_to_city": ciudad,
        "x_ship_to_country": pais,
        "x_ship_to_state": estado,
        "x_ship_to_zip": zip_code,
        "x_ship_to_phone": telefono,
        "x_description": f"Compra plan {plan} ({tipo_pago})",
        "x_invoice_num": "12345",  # puedes generar dinámico
        "x_url_success": "https://3360773e3e4e.ngrok-free.app/exitoso",
        "x_url_error": "https://3360773e3e4e.ngrok-free.app/cancelado",
        "x_url_cancel": url_for('pagina_pago.pago', plan=plan, _external=True),
        "http_origin": "https://3360773e3e4e.ngrok-free.app",
        "x_company": nit,
        "x_address": direccion,
        "x_city": ciudad,
        "x_country": pais,
        "x_state": estado,
        "x_zip": zip_code,
        "products": json.dumps([[f"Plan {plan}", "SKU-001", "", "1", str(precio), str(precio)]]),
        "x_freight": "1.00",
        "taxes": "1.00",
        "x_email": email,
        "x_type": "AUTH_ONLY",
        "x_method": "CC",
        "custom_fields": json.dumps({"plan": plan, "tipo_pago": tipo_pago}),
        "x_visacuotas": "si",
        "x_relay_url": QPAY_RELAY_URL,
        "origen": "PLUGIN",
        "store_type": "hostedpage",
        "x_discount": "0"
    }

    
    # URL de QPayPro según ambiente
    QPAY_TOKEN_URL = "https://api-sandboxpayments.qpaypro.com/checkout/register_transaction_store" if QPAY_SANDBOX else "https://api-payments.qpaypro.com/checkout/register_transaction_store"
    
    response = requests.post(QPAY_TOKEN_URL, json=payload, verify=False)

    if response.status_code == 200:
        try:
            result = response.json()
        except ValueError:
            return f"Error al interpretar la respuesta: {response.text}"

        if result.get('estado') == 'success' and 'data' in result and 'token' in result['data']:
            token = result['data']['token']
            hosted_url = ("https://sandboxpayments.qpaypro.com/checkout/store?token=" if QPAY_SANDBOX 
                          else "https://payments.qpaypro.com/checkout/store?token=") + token
            return redirect(hosted_url)
        else:
            return f"Error en respuesta: {result}"
    else:
        return f"Error en la solicitud: {response.text}"
