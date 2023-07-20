from app.models.db import db

class categorias():
    def criar():
        cursor = db.cursor()
        sql = "CREATE TABLE IF NOT EXISTS 'categorias' (cat_id INTEGER PRIMARY KEY AUTOINCREMENT,categoria varchar[30] NOT NULL);"
        cursor.execute(sql)
        cursor.close()
    def inserir(nome):
        cursor = db.cursor()
        sql = f"INSERT INTO categorias (rowid,categoria) VALUES (NULL,'{nome}');"
        cursor.execute(sql)
        db.commit()
        cursor.close()
    def selecionar(categoria):
        cursor = db.cursor()
        sql= f"SELECT cat_id FROM categorias WHERE categoria='{categoria}';"
        cursor.execute(sql)
        dados = cursor.fetchall()
        cursor.close()
        return dados