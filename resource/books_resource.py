from flask_restful import Resource, reqparse
from database import connect_db

class GetBooksResource(Resource):
    def get(self):
        """
        ---
        tags:
          - Books
        description: Returns a list of all books
        responses:
          200:
            description: List of books returned successfully
            schema:
              type: object
              properties:
                books:
                  type: array
                  items:
                    type: object
                    properties:
                      id:
                        type: integer
                        description: The unique ID of the book
                      title:
                        type: string
                        description: The title of the book
                      author:
                        type: string
                        description: The author of the book
                      comment:
                        type: string
                        description: A comment about the book
        """
        with connect_db() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM books")
            books = cursor.fetchall()
        return {"books": [dict(id=id, title=title, author=author, comment=comment) for (id, title, author, comment) in books]}, 200

class AddBookResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', required=True, help="The 'title' field is required")
    parser.add_argument('author', required=True, help="The 'author' field is required")
    parser.add_argument('comment', required=False)

    def post(self):
        """
        ---
        tags:
          - Books
        description: Adds a new book to the list
        parameters:
          - in: body
            name: body
            schema:
              type: object
              required:
                - title
                - author
              properties:
                title:
                  type: string
                author:
                  type: string
                comment:
                  type: string
        responses:
          201:
            description: Book added successfully
        """
        args = self.parser.parse_args()
        with connect_db() as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO books (title, author, comment) VALUES (?, ?, ?)", 
                           (args['title'], args['author'], args.get('comment', '')))
            connection.commit()
        return {"message": "Book added successfully"}, 201

class DeleteBookResource(Resource):
    def delete(self, book_id):
        """
        ---
        tags:
          - Books
        description: Deletes a book by its ID
        parameters:
          - in: path
            name: book_id
            type: integer
            required: true
            description: ID of the book to be deleted
        responses:
          200:
            description: Book deleted successfully
          404:
            description: Book not found
        """
        with connect_db() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
            book = cursor.fetchone()

            if book is None:
                return {"message": "Book not found"}, 404

            cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
            connection.commit()
        return {"message": f"Book with ID {book_id} deleted successfully"}, 200