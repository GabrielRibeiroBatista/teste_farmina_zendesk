from flask import Flask, render_template, request
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import json
import os

app = Flask(__name__)

# Carrega variáveis do .env
load_dotenv()

# Credenciais da API (lidas do .env)
API_USER = os.getenv('API_USER')
API_PASS = os.getenv('API_PASS')
API_BASE_URL = os.getenv('API_BASE_URL')

# Função para obter a lista de cuidados especiais
def get_special_cares(species):
    url = f"{API_BASE_URL}/specialcares/list"
    payload = {
        "species": species,
        "country": "IT",
        "languageId": "1",
        "type": "dietetic"
    }
    response = requests.post(url, json=payload, auth=HTTPBasicAuth(API_USER, API_PASS))
    if response.status_code == 200:
        data = response.json()
        cares = data['result'][0]['specialcares'][0]['list']
        return cares
    else:
        return []

# Função para buscar produtos com base nos filtros
def get_products(filters):
    url = f"{API_BASE_URL}/nutritionalplans/products/list"
    payload = {
        "country": "IT",
        "languageId": "20",
        "productType": filters['productType'],
        "type": filters['species'],
        "lifeStage": filters['lifeStage'],
        "gestation": filters['gestation'],
        "lactation": filters['lactation'],
        "specialcares": filters['specialcares'],
        "appsAndEshop": True
    }

    try:
        response = requests.post(url, json=payload, auth=HTTPBasicAuth(API_USER, API_PASS))
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[ERRO] Falha na requisição para a API: {e}")
        return []

    try:
        data = response.json()
    except ValueError:
        print("[ERRO] Falha ao interpretar o JSON da resposta.")
        print("Resposta bruta:", response.text)
        return []

    # Verifica se 'result' e 'products' existem no JSON
    if 'result' in data and 'products' in data['result']:
        return data['result']['products']
    else:
        print("[ERRO] Estrutura inesperada na resposta da API.")
        print("JSON recebido:", json.dumps(data, indent=2))
        return []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Captura os dados do formulário
        productType = request.form.get('productType')
        species = request.form.get('species')
        gestation = request.form.get('gestation') == 'yes'
        lactation = request.form.get('lactation') == 'yes'
        lifeStage = request.form.get('lifeStage')
        specialcares = request.form.getlist('specialcares')

        # Monta o dicionário de filtros
        filters = {
            'productType': productType,
            'species': species,
            'gestation': gestation,
            'lactation': lactation,
            'lifeStage': lifeStage,
            'specialcares': specialcares
        }

        # Busca os produtos com base nos filtros
        products = get_products(filters)

        return render_template('results.html', products=products)

    else:
        # Para o método GET, renderiza o formulário com os cuidados especiais
        species = 'dog'  # Padrão inicial
        special_cares = get_special_cares(species)
        return render_template('index.html', special_cares=special_cares)

if __name__ == '__main__':
    app.run(debug=True)
