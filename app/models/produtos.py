from app.models import db
from app.models.categorias import categorias

class produtos():

    def criar():
        sql = "CREATE TABLE IF NOT EXISTS 'produtos' (id INTEGER PRIMARY KEY AUTOINCREMENT,nome varchar[30] NOT NULL,preco float[7,2] NOT NULL,foto varchar[100] NOT NULL,cat_fk INTEGER NOT NULL,FOREIGN KEY (cat_fk) REFERENCES categorias(cat_id));"
        db.sql(sql,'create')
        
    def inserir(nome,preco,foto,cat):
        sql=f"INSERT INTO produtos (rowid,nome,preco,foto,cat_fk) VALUES (NULL,'{nome}','{preco}','{foto}','{cat}');"
        db.sql(sql,'insert')
        
    def selecionar_tudo():
        sql= "SELECT * FROM produtos;"
        return db.sql(sql,'select')
        
    def selecionar_categoria(cat):
        cat_id = categorias.selecionar(cat)
        sql= f"SELECT * FROM produtos WHERE cat_fk={cat_id};"
        return db.sql(sql,'select')
        
    def selecionar_produto(id):
        sql= f"SELECT * FROM produtos WHERE id={id};"
        return db.sql(sql,'select')
        
    def atualizar(id,nome,preco,foto,cat_fk):
        sql= f"UPDATE produtos SET nome='{nome}',preco='{preco}',foto='{foto}',cat_fk='{cat_fk}' WHERE id={id};"
        db.sql(sql,'update')
        
    def deletar(id):
        sql= f"DELETE FROM produtos where id={id};"
        return db.sql(sql,'delete')