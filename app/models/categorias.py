from app.models import db

class categorias():
    def criar():
        sql = "CREATE TABLE IF NOT EXISTS 'categorias' (cat_id INTEGER PRIMARY KEY AUTOINCREMENT,categoria varchar[30] NOT NULL);"
        db.sql(sql,'create')
    def inserir(nome):
        sql = f"INSERT INTO categorias (rowid,categoria) VALUES (NULL,'{nome}');"
        db.sql(sql,'insert')
    def selecionar(categoria):
        sql= f"SELECT cat_id FROM categorias WHERE categoria='{categoria}';"
        return db.sql(sql,'select')