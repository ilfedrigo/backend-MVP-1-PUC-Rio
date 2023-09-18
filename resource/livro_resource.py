from flask_restful import Resource, reqparse
from database import conectar_bd

class ConsultarLivrosResource(Resource):
    def get(self):
        """
        ---
        tags:
          - Livros
        descriptions: Retorna uma lista de todos os livros
        responses:
          200:
            description: Lista de livros foi retornada com sucesso
            schema:
              type: object
              properties:
                livros:
                  type: array
                  items:
                    type: object
                    properties:
                      id:
                        type: integer
                        description: O ID único do livro
                      titulo:
                        type: string
                        description: O título do livro
                      autor:
                        type: string
                        description: O autor do livro
                      comentario:
                        type: string
                        description: Um comentário sobre o livro
        """
        with conectar_bd() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM livros")
            livros = cursor.fetchall()
        return {"livros": [dict(id=id, titulo=titulo, autor=autor, comentario=comentario) for (id, titulo, autor, comentario) in livros]}, 200

class AdicionarLivroResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('titulo', required=True, help="O campo 'titulo' é obrigatório")
    parser.add_argument('autor', required=True, help="O campo 'autor' é obrigatório")
    parser.add_argument('comentario', required=False)

    def post(self):
        """
        ---
        tags:
          - Livros
        descriptions: Adiciona um novo livro à lista
        parameters:
          - in: body
            name: body
            schema:
              type: object
              required:
                - titulo
                - autor
              properties:
                titulo:
                  type: string
                autor:
                  type: string
                comentario:
                  type: string
        responses:
          201:
            description: Livro adicionado com sucesso
        """
        args = self.parser.parse_args()
        with conectar_bd() as conexao:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO livros (titulo, autor, comentario) VALUES (?, ?, ?)", 
                           (args['titulo'], args['autor'], args.get('comentario', '')))
            conexao.commit()
        return {"message": "Livro adicionado com sucesso"}, 201

class DeletarLivroResource(Resource):
    def delete(self, livro_id):
        """
        ---
        tags:
          - Livros
        descriptions: Exclui um livro pelo seu ID
        parameters:
          - in: path
            name: livro_id
            type: integer
            required: true
            description: ID do livro a ser excluído
        responses:
          200:
            description: Livro foi excluído com sucesso
          404:
            description: Livro não encontrado
        """
        with conectar_bd() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM livros WHERE id = ?", (livro_id,))
            livro = cursor.fetchone()

            if livro is None:
                return {"mensagem": "Livro não encontrado"}, 404

            cursor.execute("DELETE FROM livros WHERE id = ?", (livro_id,))
            conexao.commit()
        return {"mensagem": f"Livro com ID {livro_id} foi excluído com sucesso"}, 200