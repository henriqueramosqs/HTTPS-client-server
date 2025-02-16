from flask import Flask, request, jsonify
import hashlib
import ssl
from flask_talisman import Talisman

app = Flask(__name__)

# Configuração de Segurança HTTP Headers
Talisman(app, content_security_policy={
    'default-src': '\'self\'',
    'script-src': '\'self\'',
    'style-src': '\'self\'',
    'frame-ancestors': '\'none\''
}, force_https=True, strict_transport_security=True)

def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

@app.route('/secure-data', methods=['POST'])
def secure_data():
    data = request.json.get("message")
    if not data:
        return jsonify({"error": "Nenhuma mensagem enviada"}), 400
    
    response = {
        "message_received": data,
        "message_hash": generate_hash(data)
    }
    return jsonify(response)

if __name__ == '__main__':
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")
    context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1  # Desativa TLS 1.0 e 1.1 (obsoletos)

    app.run(host='0.0.0.0', port=5000, ssl_context=context)
