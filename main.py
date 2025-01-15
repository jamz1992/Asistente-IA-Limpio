# Importar bibliotecas necesarias
from flask import Flask, request
from dotenv import load_dotenv
import os

# Crear una instancia de Flask
app = Flask(__name__)

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener las variables de entorno
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

# Verificar que las variables se carguen correctamente
print("SID de la cuenta:", TWILIO_ACCOUNT_SID)
print("Token de autenticación:", TWILIO_AUTH_TOKEN)
print("Número de Twilio:", TWILIO_PHONE_NUMBER)

# Rutas de ejemplo para probar el servidor
@app.route("/")
def home():
    return "¡La aplicación Flask está funcionando correctamente!"

# Ruta para manejar el webhook de Twilio
@app.route("/webhook", methods=["POST"])
def webhook():
    # Procesar datos del webhook
    data = request.json
    print("Datos recibidos en el webhook:", data)
    return "Webhook recibido correctamente", 200

# Configurar el puerto dinámico proporcionado por Render
if __name__ == "__main__":
    # Obtén el puerto desde la variable de entorno proporcionada por Render
    port = int(os.environ.get("PORT", 5000))  # Predeterminado: 5000
    # Ejecuta la aplicación en todas las interfaces disponibles
    app.run(host="0.0.0.0", port=port)
