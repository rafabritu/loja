import sqlite3

db = sqlite3.connect('loja.db',check_same_thread=False)

def sql(querry,operacao):
    if(operacao=='select'):
        cursor = db.cursor()
        cursor.execute(querry)
        dados = cursor.fetchall()
        cursor.close()
        return dados
    if(operacao=='create' or operacao=='insert' or operacao=='update' or operacao=='delete'):
        cursor = db.cursor()
        cursor.execute(querry)
        db.commit()
        cursor.close()
        return "Operação realizada com sucesso"