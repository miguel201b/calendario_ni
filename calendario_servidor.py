from flask import Flask, send_file, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Habilitar CORS

# Define the directory where your PDF files are stored
PDF_DIRECTORY = 'Resources'

# Define the endpoint that will return the PDF
@app.route('/get_calendar', methods=['GET'])
def get_calendar():
    letter = request.args.get('letter')
    shift = request.args.get('shift')

    if not letter or not shift:
        return jsonify({"error": "Please provide both 'letter' and 'shift' parameters"}), 400

    # Construct the filename based on the letter and shift
    filename = f"calendario_{letter.upper()}_{shift.capitalize()}.pdf"

    # Check if the file exists
    file_path = os.path.join(PDF_DIRECTORY, filename)
    if not os.path.isfile(file_path):
        return jsonify({"error": "File not found"}), 404

    # Send the file with the name 'calendario.pdf'
    return send_file(file_path, as_attachment=True, download_name='calendario.pdf')

if __name__ == '__main__':
    app.run(debug=True)