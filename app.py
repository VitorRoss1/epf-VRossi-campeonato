from bottle import Bottle, redirect, static_file
from config import Config

# Importar as aplicações de outros módulos para montar
from controllers.campeonato_controller import campeonato_app
from controllers.user_controller import user_app, auth_app

class App:
    def __init__(self):
        self.bottle = Bottle()
        self.config = Config()
        self.setup_routes()

    def setup_routes(self):
        # Monta as aplicações Bottle de outros arquivos
        self.bottle.mount('/campeonato', campeonato_app)
        self.bottle.mount('/users', user_app)
        self.bottle.mount('/auth', auth_app)
        
        @self.bottle.route('/static/<filepath:path>') 
        def serve_static(filepath):
            return static_file(filepath, root=self.config.STATIC_PATH)
        
        @self.bottle.route('/')
        def home():
            return redirect('/campeonato')

    def run(self):
        self.bottle.run(
            host=self.config.HOST,
            port=self.config.PORT,
            debug=self.config.DEBUG,
            reloader=self.config.RELOADER
        )

def create_app():
    return App()