from flask import Flask, request, jsonify, render_template
from core import parse_point, distance, format_hp

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/distance", methods=["POST"])
def calc_distance():
    data = request.json
    try:
        p1 = parse_point(data["p1"], data["unit"])
        p2 = parse_point(data["p2"], data["unit"])
        d = distance(p1, p2)
        return jsonify({"distance": round(d, 3)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/format", methods=["POST"])
def format_point():
    try:
        data = request.json
        p = parse_point(data["point"], data["unit"])
        return jsonify({
            "formatted": format_hp(data["name"], p, data["unit"])})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
