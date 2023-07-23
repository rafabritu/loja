from flask import render_template, request,redirect
from app.models import *
# usuarios.criar_tabela()
# usuarios.cadastrar_usuario('Rafael',"rafael@techstore.com",'3198989898','123456')
# from werkzeug.utils import secure_filename
# categorias.cadastrar_categoria("Celulares")
# categorias.cadastrar_categoria("Games")
# produto.cadastrar_produto('Samsung Galaxy A54 5G 5G Dual SIM 128 GB branco 8 GB RAM','1979,59','..\static\img\m54.webp',1)
# produto.cadastrar_produto('Apple iPhone 12 128gb Original Vitrine - Branco','3499,40','..\static\img\D_NQ_NP_778290-MLB51921000774_102022-O.webp',1)
# produto.cadastrar_produto('Cadeira Gamer Tgt Heron Tc, Preto E Vermelho, Tgt-hrtc-br01','439,89','..\static\img\cadgamer.webp',2)
# produto.cadastrar_produto('Microsoft Xbox Series S 512GB Standard cor branco','1999,00','..\static\img\eirueie.webp',2)

def init_app(app):
    @app.route('/')
    def index():
        dados = produtos.selecionar_tudo()
        return render_template('index.html',dados=dados)
    
    @app.route('/Admin')
    def admin():
        dados = produtos.selecionar_tudo()
        return render_template('admin.html',dados=dados)
    
    @app.route('/Admin/cadastrar/produto/')
    def cadastro_produto():
        return render_template('pcadastro.html')
    
    @app.route('/Admin/produto/cadastrar/confirm', methods=["POST"])
    def cadastro_confirm():
        nome = request.form.get('nome')
        preco = request.form.get('preco')
        file = request.files['foto']
        destino = f"{app.config['UPLOAD_FOLDER']}/{file.filename}"
        file.save(destino)
        cat_fk = request.form.get('cat_fk')
        diretorio = f"../static/upload/{file.filename}"
        produtos.inserir(nome,preco,diretorio,cat_fk)
        return redirect('/Admin')
    @app.route('/Admin/edit/produto/<string:id>')
    def produto_edit(id):
        dados = produtos.selecionar_produto(int(id))
        return render_template('produto_edit.html',dados=dados)     
    @app.route('/Admin/edit/produto/', methods=["POST"])
    def submit():
        id = request.form.get('id')
        nome = request.form.get('nome')
        preco = request.form.get('preco')
        file = request.files['foto']
        destino = f"{app.config['UPLOAD_FOLDER']}/{file.filename}"
        file.save(destino)
        cat_fk = request.form.get('cat_fk')
        diretorio = f"../static/upload/{file.filename}"
        produtos.atualizar(id,nome,preco,diretorio,cat_fk)
        return redirect('/Admin')
    @app.route('/Admin/delete/produto/<string:id>')
    def produto_delete(id):
        produtos.deletar(id)
        return redirect('/Admin')
        
    @app.route('/<string:page>')
    def categoria(page):
        dados = produtos.selecionar_categoria(page)
        return render_template('index.html',dados=dados)
    @app.route('/produto/<string:id>')
    def produto(id):
        dados = produtos.selecionar_produto(int(id))
        print(produto)
        return render_template('produto.html',dados=dados)
    # @app.route('/teste')
    # def todos():   
    #     return dados
    @app.route('/login')
    def login():
        return render_template('login.html')
    @app.route('/login/auth',methods=["POST"])
    def auth():
        email = request.form.get('usuario')
        senha = request.form.get('senha')
        try:
            user = usuarios.recuperar_usuario(email)
        except:
            print("Erro no banco")
        else:
            if(user==[]):
                return render_template('login.html',erro=1,msg='Usuario não encontrado')
            elif(email == user[0][2] and senha==user[0][4]):
                return redirect('/Admin')
            else:
                return render_template('login.html',erro=1,msg='Senha incorreta')
