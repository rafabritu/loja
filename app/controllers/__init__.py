from flask import render_template, request
from app import models

produto = models.produtos
usuarios = models.usuarios
categorias = models.categorias
categorias.criar_tabela()
produto.criar_tabela()
usuarios.criar_tabela()
# categorias.cadastrar_categoria("Celulares")
# categorias.cadastrar_categoria("Games")
# produto.cadastrar_produto('Samsung Galaxy A54 5G 5G Dual SIM 128 GB branco 8 GB RAM','1979,59','..\static\img\m54.webp',1)
# produto.cadastrar_produto('Apple iPhone 12 128gb Original Vitrine - Branco','3499,40','..\static\img\D_NQ_NP_778290-MLB51921000774_102022-O.webp',1)
# produto.cadastrar_produto('Cadeira Gamer Tgt Heron Tc, Preto E Vermelho, Tgt-hrtc-br01','439,89','..\static\img\cadgamer.webp',2)
# produto.cadastrar_produto('Microsoft Xbox Series S 512GB Standard cor branco','1999,00','..\static\img\eirueie.webp',2)
def init_app(app):
    @app.route('/')
    def index():
        dados = models.produtos.selecionar_todos_produtos()
        return render_template('index.html',dados=dados)
        
    @app.route('/Categoria/<string:page>')
    def categoria(page):
        dados = models.produtos.selecionar_categoria(page)
        return render_template('index.html',dados=dados)
        
    @app.route('/produto/<string:id>')
    def produto(id):
        dados = models.produtos.selecionar_produto(int(id))
        print(produto)
        return render_template('produto.html',dados=dados)
    
    # @app.route('/teste')
    # def todos():   
    #     return dados