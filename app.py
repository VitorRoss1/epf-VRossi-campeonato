from bottle import Bottle
from config import Config

class App:
    def __init__(self):
        self.bottle = Bottle()
        self.config = Config()

    def setup_routes(self):
        # Importe ambos os controllers
        from controllers.user_controller import user_routes
        from controllers.campeonato_controller import campeonato_routes
        
        # Monte as rotas
        self.bottle.mount('/users', user_routes)
        self.bottle.mount('/campeonato', campeonato_routes)
        
        # Rota raiz
        @self.bottle.route('/')
        def home():
            return """
            <h1>Brasileirão 2025</h1>
            <ul>
                <li><a href='/campeonato/rodada/1'>Simular Rodada</a></li>
                <li><a href='/users'>Gerenciar Usuários</a></li>
            </ul>
            """

        print('🚀 Rotas inicializadas com sucesso!')

    def run(self):
        self.setup_routes()
        self.bottle.run(
            host=self.config.HOST,
            port=self.config.PORT,
            debug=self.config.DEBUG,
            reloader=self.config.RELOADER
        )

def create_app():
    return App()