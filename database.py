import sqlite3

def conectar_bd():
    return sqlite3.connect('database.db')

def inicializar_bd():
    with conectar_bd() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            comentario TEXT
        )
        """)
        conexao.commit()

if __name__ == '__main__':
    inicializar_bd()