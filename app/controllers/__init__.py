from flask import render_template
from app import models

produto = models.produtos
usuarios = models.usuarios
produto.criar_tabela()
usuarios.criar_tabela()
produto.cadastrar_produto("Smartphone Samsung Galaxy A54 5G 128GB Preto","1010,99","../static/img/57298902-1600-auto.webp")
produto.cadastrar_produto("Smartphone Samsung Galaxy M54 5G 256GB Prata 8GB Ram","1887,94","..\static\img\m54.webp")

dados = models.produtos.selecionar_todos_produtos()

def init_app(app):
    @app.route('/')
    def index():
        return render_template('index.html',dados=dados)
        
    @app.route('/produto')
    def produto():
        return render_template('produto.html')
    
    @app.route('/teste')
    def todos():
        return dados