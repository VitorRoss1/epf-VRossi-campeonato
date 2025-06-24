from bottle import Bottle
from config import Config

class App:
    def __init__(self):
        self.bottle = Bottle()
        self.config = Config()

    def setup_routes(self):
        # Importe explicitamente cada controller
        from controllers.campeonato_controller import campeonato_routes
        from controllers.user_controller import user_routes
        
        # Monte as rotas com prefixos
        self.bottle.mount('/campeonato', campeonato_routes)
        self.bottle.mount('/users', user_routes)
        
        # Rota raiz para teste
        @self.bottle.route('/')
        def home():
            return """
            <h1>Sistema do Brasileirão</h1>
            <a href='/campeonato/rodada/1'>Ver Rodada 1</a>
            """

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
