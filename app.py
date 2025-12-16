from flask import Flask, request, jsonify
from core import parse_point, distance, format_hp

app = Flask(__name__)

@app.route("/distance", methods=["POST"])
def calc_distance():
    data = request.json
    p1 = parse_point(data["p1"], data["unit"])
    p2 = parse_point(data["p2"], data["unit"])
    d = distance(p1, p2)
    return jsonify({"distance": round(d, 3)})

@app.route("/format", methods=["POST"])
def format_point():
    data = request.json
    p = parse_point(data["point"], data["unit"])
    return jsonify({
        "formatted": format_hp(data["name"], p, data["unit"])
    })

if __name__ == "__main__":
    app.run(debug=True)
