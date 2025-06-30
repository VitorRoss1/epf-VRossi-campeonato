
from bottle import request, redirect
from services.auth_service import AuthService
from .base_controller import BaseController

class AuthController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.auth_service = AuthService()
        self.setup_routes()
    
    def setup_routes(self):
        self.app.route('/login', method=['GET', 'POST'], callback=self.login)
        self.app.route('/register', method=['GET', 'POST'], callback=self.register)
        self.app.route('/logout', method='GET', callback=self.logout)
    
    def login(self):
        if request.method == 'POST':
            email = request.forms.get('email')
            password = request.forms.get('password')
            if self.auth_service.login(email, password):
                redirect('/campeonato')
            return self.render('auth/login', error='Credenciais inválidas')
        return self.render('auth/login')
    
    def register(self):
        if request.method == 'POST':
            name = request.forms.get('name')
            email = request.forms.get('email')
            password = request.forms.get('password')
            if self.auth_service.register(name, email, password):
                redirect('/login')
            return self.render('auth/register', error='Email já cadastrado')
        return self.render('auth/register')
    
    def logout(self):
        self.auth_service.logout()
        redirect('/login')