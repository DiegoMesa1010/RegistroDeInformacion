import os
import json
from flask import Flask
from dotenv import load_dotenv
import gspread
from google.oauth2.service_account import Credentials
from Router.Rutas import registrar_rutas

# Cargar variables de entorno
load_dotenv()

# Configurar Flask
app = Flask(__name__)

# Configurar Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
google_creds = os.getenv('GOOGLE_CREDS_JSON')
info = json.loads(google_creds)
creds = Credentials.from_service_account_info(info, scopes=SCOPES)
client = gspread.authorize(creds)

# Guardar cliente y spreadsheet_id en la app
app.config['SHEETS_CLIENT'] = client
app.config['SPREADSHEET_ID'] = os.getenv('SPREADSHEET_ID')

# Registrar rutas desde routes.py
registrar_rutas(app)

# Ejecutar servidor Flask
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))  # Usa el puerto definido en .env o 5000 por defecto
    app.run(host='0.0.0.0', port=port)
