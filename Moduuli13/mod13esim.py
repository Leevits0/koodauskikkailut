# Moduuli 13 Python-palvelinesimerkki Flaskilla

from flask import Flask, Response, request
import json

app = Flask(__name__)

print(__name__)

def calc_sum(a,b):
    return a + b
def multiply(a,b):
    return a * b

@app.route('/calc/<type>')
def calculate(type):
    # print(request.args.get("num1"))
    try:
        num1 = float(request.args.get("num1"))
        num2 = float(request.args.get("num2"))
        if type == "sum":
            result = (calc_sum(num1, num2))
        elif type == "multiply":
            result = multiply(num1,num2)
        else:
            response_body = json.dumps(
                {"error": "unknown calculation type", "status": 400}
            )
            return Response(response=response_body, status=400, minetype="application/json")
        return {"result": result, "numbers": [num1, num2]}
    # Oletuksena dictionary muuttetaan http-vastaukeen automaattisesti jsoniksi
    except:
        # TODO : muuta virhekoodi myös https-vastauksen otsikkotiedoissa
        return {"error": "invalid parameters", "status": 400}

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")



if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1',port=3000)


