from flask import Flask, jsonify, request
from flask_restful import Api
from flasgger import Swagger
from flask_cors import CORS
import sqlite3

app = Flask (__name__)
api = Api(app)

app.config['SWAGGER'] = {
    'title': 'API-MVP',
    'uiversion': 3,
}
Swagger(app)
CORS(app)

DATABASE = 'livros.db'

def conectar_bd():
    return sqlite3.connect(DATABASE)

def criar_tabela():
    with conectar_bd() as conexao:
        cursor = conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                comentario TEXT
            )
        ''')
        conexao.commit()

@app.route('/buscar-livros', methods=['GET'])
def listar_livros():
    with conectar_bd() as conexao:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM livros')
        colunas = [desc[0] for desc in cursor.description]
        livros = [dict(zip(colunas, livro)) for livro in cursor.fetchall()]
    return jsonify({"livros": livros})

@app.route('/adicionar-livros', methods=['POST'])
def adicionar_livro():
    data = request.get_json()
    if not data:
        return jsonify({"message": "Dados inválidos"}), 400

    if 'titulo' not in data or 'autor' not in data:
        return jsonify({"message": "Campos 'titulo' e 'autor' são obrigatórios"}), 400

    titulo = data.get('titulo')
    autor = data.get('autor')
    comentario = data.get('comentario', '')

    with conectar_bd() as conexao:
        cursor = conexao.cursor()
        cursor.execute('INSERT INTO livros (titulo, autor, comentario) VALUES (?, ?, ?)', (titulo, autor, comentario))
        conexao.commit()
    
    return jsonify({"message": "Livro adicionado com sucesso"}), 201

@app.route('/excluir-livro/<int:livro_id>', methods=['DELETE'])
def deletar_livro(livro_id):
    with conectar_bd() as conexao:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM livros WHERE id = ?', (livro_id,))
        livro = cursor.fetchone()

        if livro is None:
            return jsonify({"mensagem": "Livro não encontrado"}), 404

        cursor.execute('DELETE FROM livros WHERE id = ?', (livro_id,))
        conexao.commit()

    return jsonify({"mensagem": f"Livro com ID {livro_id} foi excluído com sucesso"}), 200

@app.route('/api/doc')
def swagger_ui():
    return swagger.ui()

if __name__ == "__main__":
    criar_tabela()
    app.run()