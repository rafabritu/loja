from flask import render_template

def init_app(App):
    @App.route('/')
    def index():
        return render_template('index.html')
        
    @App.route('/produto')
    def produto():
        return render_template('produto.html')