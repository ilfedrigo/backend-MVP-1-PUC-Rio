from sqlalchemy import Column, String, Integer
from  model import Base


class Livro(Base):
    __tablename__ = 'livros'

    id = Column("pk_livros", Integer, primary_key=True)
    titulo = Column(String(140), unique=True)
    autor = Column(String(140), unique=False)
    comentario = Column(String(360), unique=True)
    
    def __init__(self, titulo:str, autor:str, comentario:str):
 
        """
        Cria um Livro com 3 argumentos:
            titulo: título do livro
            autor: autor da obra
            comentario: anotações pessoais sobre a leitura
        """
        self.titulo = titulo
        self.autor = autor
        self.comentario = comentario