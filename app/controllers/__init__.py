from flask import render_template, request
from app import models

produto = models.produtos
usuarios = models.usuarios
produto.criar_tabela()
usuarios.criar_tabela()



def init_app(app):
    @app.route('/')
    def index():
        dados = models.produtos.selecionar_todos_produtos()
        return render_template('index.html',dados=dados)
        
    @app.route('/produto/<string:id>')
    def produto(id):
        dados = models.produtos.selecionar_produto(int(id))
        print(produto)
        return render_template('produto.html',dados=dados)
    
    @app.route('/teste')
    def todos():
        
        return dados