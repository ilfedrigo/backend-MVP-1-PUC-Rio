from flask import Flask, jsonify
app = Flask (__name__)

@app.route('/livros', methods=['GET'])
def listar_livros():
    livros = [
        {"titulo": "Livro", "autor": "Autor", "comentario": "Comentário"},
    ]
    return jsonify({"livros": livros})

if __name__ == "__main__":
    app.run()