from app.models import db
class usuarios():
    def criar_tabela():
        sql = "CREATE TABLE IF NOT EXISTS 'usuarios' (id INTEGER PRIMARY KEY AUTOINCREMENT,nome varchar[50],email varchar[50],telefone int[11],senha varchar[15]);"
        db.sql(sql,'create')
    def cadastrar_usuario(nome,email,telefone,senha):
        sql= f"INSERT INTO usuarios (rowid,nome,email,telefone,senha) values (NULL,'{nome}','{email}','{telefone}','{senha}');"
        db.sql(sql,'insert')
    def recuperar_usuario(email):
        querry=f"SELECT * from usuarios WHERE email='{email}'"
        return db.sql(querry,'select')
    def alterar(id,nome,email,telefone,senha):
        querry = f"UPDATE usuarios SET nome='{nome}',email='{email}',telefone='{telefone}',senha='{senha}' WHERE id={id};"
        db.sql(querry,'update')