from app.models.db import db
from app.models.categorias import categorias

class produtos():

    def criar():
        cursor = db.cursor()
        sql = "CREATE TABLE IF NOT EXISTS 'produtos' (id INTEGER PRIMARY KEY AUTOINCREMENT,nome varchar[30] NOT NULL,preco float[7,2] NOT NULL,foto varchar[100] NOT NULL,cat_fk INTEGER NOT NULL,FOREIGN KEY (cat_fk) REFERENCES categorias(cat_id));"
        cursor.execute(sql)
        cursor.close()
    def inserir(nome,preco,foto,cat):
        cursor = db.cursor()
        sql=f"INSERT INTO produtos (rowid,nome,preco,foto,cat_fk) VALUES (NULL,'{nome}','{preco}','{foto}','{cat}');"
        cursor.execute(sql)
        db.commit()
        cursor.close()
    def selecionar_tudo():
        cursor = db.cursor()
        sql= "SELECT * FROM produtos;"
        cursor.execute(sql)
        dados = cursor.fetchall()
        cursor.close()
        return dados
        
    def selecionar_categoria(cat):
        cursor = db.cursor()
        cat_id = categorias.selecionar(cat)
        sql= f"SELECT * FROM produtos WHERE cat_fk={cat_id[0][0]};"
        cursor.execute(sql)
        dados = cursor.fetchall()
        cursor.close()
        return dados
        
    def selecionar_produto(id):
        cursor = db.cursor()
        sql= f"SELECT * FROM produtos WHERE id={id};"
        cursor.execute(sql)
        dados = cursor.fetchall()
        cursor.close()
        return dados
    def atualizar(id,nome,preco,foto,cat_fk):
        cursor = db.cursor()
        sql= f"UPDATE produtos SET nome='{nome}',preco={preco},foto='{foto}',cat_fk={cat_fk} where id={id};"
        cursor.execute(sql)
        dados = cursor.fetchall()
        cursor.close()
        return dados
    def deletar(id):
        cursor = db.cursor()
        sql= f"DELETE FROM produtos where id={id};"
        cursor.execute(sql)
        dados = cursor.fetchall()
        cursor.close()
        return dados