from bottle import Bottle, request, redirect, response
from services.user_service import UserService

user_routes = Bottle()
user_service = UserService()

# Rotas Públicas
@user_routes.route('/login', method=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.forms.get('email')
        password = request.forms.get('password')
        user = user_service.authenticate(email, password)
        
        if user:
            response.set_cookie('user_id', str(user['id']))
            return redirect('/')
        return {'error': 'Email ou senha inválidos'}
    
    return {
        'template': 'auth/login.tpl',
        'data': {
            'title': 'Login'
        }
    }

@user_routes.route('/register', method=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            user_service.create_user(
                request.forms.get('name'),
                request.forms.get('email'),
                request.forms.get('password')
            )
            return redirect('/login')
        except ValueError as e:
            return {
                'template': 'auth/register.tpl',
                'data': {
                    'title': 'Registro',
                    'error': str(e)
                }
            }
    
    return {
        'template': 'auth/register.tpl',
        'data': {
            'title': 'Registro'
        }
    }

@user_routes.route('/logout')
def logout():
    response.delete_cookie('user_id')
    return redirect('/')

# Rotas Protegidas
@user_routes.route('/profile')
@user_service.login_required
def profile():
    user = user_service.get_current_user()
    return {
        'template': 'user/profile.tpl',
        'data': {
            'title': 'Meu Perfil',
            'user': user
        }
    }

@user_routes.route('/users')
@user_service.login_required
def list_users():
    users = user_service.get_all_users()
    return {
        'template': 'user/list.tpl',
        'data': {
            'title': 'Todos os Usuários',
            'users': users,
            'current_user': user_service.get_current_user()
        }
    }

# Rota protegida de exemplo
@user_routes.route('/admin')
@user_service.login_required
def admin_area():
    return {
        'template': 'user/admin.tpl',
        'data': {
            'title': 'Área Administrativa',
            'user': user_service.get_current_user()
        }
    }
