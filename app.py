from bottle import Bottle
from config import Config

class App:
    def __init__(self):
        self.bottle = Bottle()
        self.config = Config()

    def setup_routes(self):
        # Importe os controllers
        from controllers import campeonato_controller, user_controller
        
        # Monte as rotas
        self.bottle.mount('/campeonato', campeonato_controller.create_campeonato_routes())
        self.bottle.mount('/users', user_controller.user_routes)
        
        # Rota raiz
        @self.bottle.route('/')
        def home():
            return """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Brasileirão 2025</title>
            </head>
            <body>
                <h1>Bem-vindo ao Sistema do Brasileirão 2025</h1>
                <ul>
                    <li><a href='/campeonato/rodada/1'>Simular Rodada</a></li>
                    <li><a href='/campeonato/time/1'>Ver Time</a></li>
                    <li><a href='/users'>Gerenciar Usuários</a></li>
                </ul>
            </body>
            </html>
            """

        print('✅ Rotas configuradas com sucesso!')

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