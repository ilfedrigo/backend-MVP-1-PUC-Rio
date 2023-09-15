from flask_restful import Resource

class LivrosResource(Resource):
    def get(self):
        """
        Obter a lista de livros.
        ---
        responses:
          200:
            description: Lista de livros.
        """
        # Sua lógica para listar livros aqui
        pass

    def post(self):
        """
        Cadastrar um novo livro.
        ---
        parameters:
          - name: titulo
            in: formData
            type: string
            required: true
          - name: autor
            in: formData
            type: string
            required: true
          - name: comentario
            in: formData
            type: string
            required: false
        responses:
          201:
            description: Livro cadastrado com sucesso.
          400:
            description: Dados inválidos.
        """
        # Sua lógica para cadastrar um livro aqui
        pass