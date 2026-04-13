from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/clientes', methods=['GET'])
def listar_clientes():
    clientes = [
        {
            "id": 1,
            "nome": "Anderson Silva",
            "endereco": "Rua A",
            "bairro": "Jardim Las Vegas",
            "cidade": "Santo André",
            "estado": "SP",
            "cep": "09182-370"
        },
        {
            "id": 2,
            "nome": "Lilian Tabata",
            "endereco": "Rua B",
            "bairro": "Jardins",
            "cidade": "São Paulo",
            "estado": "SP",
            "cep": "01400-000"
        },
        {
            "id": 3,
            "nome": "João",
            "endereco": "Rua C",
            "bairro": "Copacabana",
            "cidade": "Rio de Janeiro",
            "estado": "RJ",
            "cep": "22000-000"
        },
        {
            "id": 4,
            "nome": "Maria",
            "endereco": "Rua D",
            "bairro": "Sertãozinho",
            "cidade": "Pedralva",
            "estado": "MG",
            "cep": "22000-000"
        }
    ]
    return jsonify(clientes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)