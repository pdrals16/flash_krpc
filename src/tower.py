import json

from flask import Flask, request, jsonify

tower = Flask(__name__)

@tower.route('/set_altitude', methods=['POST'])
def set_altitude():
    data = request.json
    new_altitude = data.get('altitude')
    if new_altitude is not None:
        target_alt = float(new_altitude)
        with open("src/config/PARAMS.json", "w") as f:
            f.write(json.dumps({"altitude": target_alt}, indent=4))
        return jsonify({"status": "success", "new_target": target_alt})
    return jsonify({"status": "error", "message": "No altitude provided"})