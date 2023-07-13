import sqlite3

db = sqlite3.connect('loja.db',check_same_thread=False)

class usuarios():
    def criar_tabela():
        cursor = db.cursor()
        sql = "CREATE TABLE IF NOT EXISTS 'usuarios' (id int AUTO_INCREMENT,nome varchar[50],email varchar[50],telefone int[11],senha varchar[15],PRIMARY KEY(id));"
        cursor.execute(sql)
        cursor.close()
    def cadastrar_usuario(nome,email,telefone,senha):
        cursor = db.cursor()
        sql= f"INSERT INTO usuarios (nome,email,telefone,senha) values ({nome},{email},{telefone},{senha});"
        cursor.execute(sql)
        cursor.close()
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
class produtos():
    def criar_tabela():
        cursor = db.cursor()
        sql = "CREATE TABLE IF NOT EXISTS 'produtos' (id INTEGER PRIMARY KEY AUTOINCREMENT,nome varchar[30] NOT NULL,preco float[7,2] NOT NULL,foto varchar[100] NOT NULL,cat_fk INTEGER NOT NULL,FOREIGN KEY (cat_fk) REFERENCES categorias(cat_id));"
        cursor.execute(sql)
        cursor.close()
    def cadastrar_produto(nome,preco,foto,cat):
        cursor = db.cursor()
        sql=f"INSERT INTO produtos (rowid,nome,preco,foto,cat_fk) VALUES (NULL,'{nome}','{preco}','{foto}','{cat}');"
        cursor.execute(sql)
        db.commit()
        cursor.close()
    def selecionar_todos_produtos():
        cursor = db.cursor()
        sql= "SELECT * FROM produtos;"
        cursor.execute(sql)
        dados = cursor.fetchall()
        cursor.close()
        return dados
        
    def selecionar_categoria(cat_id):
        cursor = db.cursor()
        sql= f"SELECT * FROM produtos WHERE cat_fk={cat_id};"
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