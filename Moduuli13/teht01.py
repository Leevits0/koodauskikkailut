from flask import Flask, Response, request
import json
import math

app = Flask(__name__)

def onko_alkuluku(luku):
    if luku <= 1:
        return False
    elif luku == 2:
        return True
    elif luku % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(luku)) + 1, 2):
            if luku % i == 0:
                return False
        return True

@app.route("/alkuluku")
def alkuluku():
    args = request.args
    luku = float(args.get("luku"))
    is_prime = onko_alkuluku(luku)
    result = {"Number": luku, "isPrime": is_prime}
    return Response(json.dumps(result), status=200, mimetype='application/json')


if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
