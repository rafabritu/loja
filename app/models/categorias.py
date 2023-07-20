from app.models import db

class categorias():
    def criar_tabela():
        cursor = db.cursor()
        sql = "CREATE TABLE IF NOT EXISTS 'categorias' (cat_id INTEGER PRIMARY KEY AUTOINCREMENT,categoria varchar[30] NOT NULL);"
        cursor.execute(sql)
        cursor.close()
    def cadastrar_categoria(nome):
        cursor = db.cursor()
        sql = f"INSERT INTO categorias (rowid,categoria) VALUES (NULL,'{nome}');"
        cursor.execute(sql)
        db.commit()
        cursor.close()