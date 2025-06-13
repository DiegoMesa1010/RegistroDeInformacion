from flask import request, jsonify

def registrar_rutas(app):
    @app.route("/")
    def home():
        return jsonify({"message": "¡El backend está corriendo correctamente!"}), 200

    @app.route('/enviar-datos', methods=['POST'])
    def enviar_datos():
        try:
            data = request.json
            client = app.config['SHEETS_CLIENT']
            spreadsheet_id = app.config['SPREADSHEET_ID']
            sheet = client.open_by_key(spreadsheet_id).sheet1

            sheet.append_row([
                data.get("Maquina"),
                data.get("Fecha"),
                data.get("Turno"),
                data.get("HR_reporte"),
                data.get("Hr_Inicio"),
                data.get("Hr_Final"),
                data.get("Tiempo_Falla"),
                data.get("Horómetro"),
                data.get("Tiempo_de_falla"),
                data.get("Falla"),
                data.get("Nombre_Mecanico"),
                data.get("Diagnostico"),
                data.get("Labor_Realizada")
            ])

            return jsonify({"message": "Datos enviados correctamente"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
