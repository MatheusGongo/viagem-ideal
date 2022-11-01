from flask import Flask, render_template, request
from flask_restful import Resource, Api
from flask_cors import CORS
import urllib.request, json
import requests

app = Flask(__name__)
CORS(app) ## To allow direct AJAX calls


@app.route("/")
@app.route("/index", methods=["POST", "GET"])
def index():

    limits = [1,2,3,4,5,6]
    pokemons_req = []
    
    preco_atual = 5.28
    target = request.form
    print(target)
    
    consumo = request.args.get('distance')
    distance = request.args.get('fuel')
    print(consumo)
    print(distance)
    uf_list = [
                    "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal", "Espírito Santo", 
                     "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", 
                     "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina", 
                     "São Paulo", "Sergipe", "Tocantins"
                ]


    list_titles = [{"thead": "Altura"}]

    print(list_titles)

    return render_template("index.html", uf_list = uf_list, list_titles = list_titles)


@app.route("/currency_travel", methods=["POST"])
def currency_travel():
    return render_template("form.html")


if __name__ == '__main__':
	app.run(debug=True)