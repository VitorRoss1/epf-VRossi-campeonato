import os 
from bottle import Bottle, redirect, static_file, TEMPLATES 
from config import Config
from controllers.campeonato_controller import campeonato_app
from controllers.user_controller import user_app, auth_app
from controllers.simular_controller import simular_app

class App:
    def __init__(self):
        self.bottle = Bottle()
        self.config = Config()
        self.setup_routes()
        TEMPLATES.clear() # Limpa o cache de templates do Bottle (útil em desenvolvimento)

    def setup_routes(self):
        self.bottle.mount('/campeonato', campeonato_app)
        self.bottle.mount('/users', user_app)
        self.bottle.mount('/auth', auth_app)
        self.bottle.mount('/simular', simular_app)
        
        # Rota para servir arquivos estáticos (sem os prints de debug)
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
            reloader=self.config.RELOADER,
            # Passe explicitamente o template_path para o run method (como lista)
            template_path=[self.config.TEMPLATE_PATH] 
        )

def create_app():
    return App()