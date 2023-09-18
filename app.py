from flask import Flask, send_from_directory
from flask_restful import Api
from flask_cors import CORS
from flasgger import Swagger
from resource.livro_resource import ConsultarLivrosResource, AdicionarLivroResource, DeletarLivroResource
import os

app = Flask(__name__)
api = Api(app)
CORS(app)
swagger = Swagger(app)

@app.route('/')
def home():
    return send_from_directory(os.path.abspath('../frontend-mvp'), 'index.html')

@app.route('/frontend-mvp/<path:path>')
def serve_frontend(path):
    return send_from_directory(os.path.abspath('../frontend-mvp'), path)

api.add_resource(ConsultarLivrosResource, '/livros', endpoint='livros')
api.add_resource(AdicionarLivroResource, '/livros/adicionar', endpoint='adicionar_livro')
api.add_resource(DeletarLivroResource, '/livros/deletar/<int:livro_id>', endpoint='deletar_livro')

if __name__ == '__main__':
    app.run(debug=True)