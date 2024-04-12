from flask import Flask, Response, request
import json

app = Flask(__name__)

print(__name__)








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


