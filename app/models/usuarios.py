from app.models import db

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