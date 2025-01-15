# Importar bibliotecas necesarias
from dotenv import load_dotenv
import os

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
