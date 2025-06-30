from bottle import Bottle
from config import Config
from controllers import campeonato_controller, user_controller

class App:
    def __init__(self):
        self.bottle = Bottle()
        self.config = Config()
        self.setup_routes()

    def setup_routes(self):
        self.bottle.mount('/campeonato', campeonato_controller.campeonato_app)
        self.bottle.mount('/users', user_controller.user_app)
        self.bottle.mount('/auth', user_controller.auth_app)
        
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