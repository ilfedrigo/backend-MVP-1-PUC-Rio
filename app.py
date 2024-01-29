from flask import Flask, send_from_directory
from flask_restful import Api
from flask_cors import CORS
from flasgger import Swagger
from resource.book_resource import GetBooksResource, AddBookResource, DeleteBookResource
import os

app = Flask(__name__)
api = Api(app)
CORS(app)
swagger = Swagger(app)

@app.route('/')
def home():
    return send_from_directory(os.path.abspath('../frontend-MVP-1-PUC-Rio'), 'index.html')

@app.route('/frontend-MVP-1-PUC-Rio/<path:path>')
def serve_frontend(path):
    return send_from_directory(os.path.abspath('../frontend-MVP-1-PUC-Rio'), path)

api.add_resource(GetBooksResource, '/books', endpoint='books')
api.add_resource(AddBookResource, '/books/add', endpoint='add_book')
api.add_resource(DeleteBookResource, '/books/delete/<int:book_id>', endpoint='delete_book')

if __name__ == '__main__':
    app.run(debug=True)
