from bottle import Bottle, static_file, template, redirect

class BaseController:
    def __init__(self, app):
        self.app = app
        self._setup_base_routes()

    def _setup_base_routes(self):
        """Rotas básicas comuns a todos controllers"""
        self.app.route('/static/<filename:path>', callback=self.serve_static)

    def serve_static(self, filename):
        return static_file(filename, root='./static')

    def render(self, template_name, **context):
        """Renderiza templates com layout padrão"""
        return template(template_name, **context)

    def redirect(self, path):
        """Redirecionamento padrão"""
        return redirect(path)