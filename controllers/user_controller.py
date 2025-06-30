from bottle import Bottle, request, redirect, response
from services.user_service import UserService
from models.user import UserModel

user_service = UserService()
user_model = UserModel()

# App para rotas de usuário
user_app = Bottle()

# App para rotas de autenticação
auth_app = Bottle()

@user_app.route('/')
@user_service.login_required
def list_users():
    users = user_model.get_all()
    return {
        'template': 'user/list.tpl',
        'data': {
            'users': users,
            'user_service': user_service
        }
    }

@user_app.route('/add', method=['GET', 'POST'])
@user_service.login_required
def add_user():
    if request.method == 'POST':
        try:
            user_service.create_user(
                request.forms.get('name'),
                request.forms.get('email'),
                request.forms.get('password')
            )
            return redirect('/users')
        except ValueError as e:
            return {
                'template': 'user/form.tpl',
                'data': {
                    'user': None,
                    'error': str(e),
                    'action': '/users/add'
                }
            }
    
    return {
        'template': 'user/form.tpl',
        'data': {
            'user': None,
            'action': '/users/add'
        }
    }

@user_app.route('/edit/<user_id:int>', method=['GET', 'POST'])
@user_service.login_required
def edit_user(user_id):
    user = user_service.get_user_by_id(user_id)
    if not user:
        return redirect('/users')
    
    if request.method == 'POST':
        try:
            user_service.update_user(
                user_id,
                request.forms.get('name'),
                request.forms.get('email'),
                request.forms.get('password')
            )
            return redirect('/users')
        except ValueError as e:
            return {
                'template': 'user/form.tpl',
                'data': {
                    'user': user,
                    'error': str(e),
                    'action': f'/users/edit/{user_id}'
                }
            }
    
    return {
        'template': 'user/form.tpl',
        'data': {
            'user': user,
            'action': f'/users/edit/{user_id}'
        }
    }

@user_app.route('/delete/<user_id:int>', method='POST'])
@user_service.login_required
def delete_user(user_id):
    if user_service.delete_user(user_id):
        return redirect('/users')
    return "Erro ao excluir usuário"

@auth_app.route('/login', method=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = user_service.authenticate(
            request.forms.get('email'),
            request.forms.get('password')
        )
        if user:
            response.set_cookie('user_id', str(user['id']))
            return redirect('/campeonato')
        return {
            'template': 'auth/login.tpl',
            'data': {'error': 'Email ou senha inválidos'}
        }
    
    return {
        'template': 'auth/login.tpl',
        'data': {}
    }

@auth_app.route('/register', method=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            user_service.create_user(
                request.forms.get('name'),
                request.forms.get('email'),
                request.forms.get('password')
            )
            return redirect('/auth/login')
        except ValueError as e:
            return {
                'template': 'auth/register.tpl',
                'data': {'error': str(e)}
            }
    
    return {
        'template': 'auth/register.tpl',
        'data': {}
    }

@auth_app.route('/logout')
def logout():
    response.delete_cookie('user_id')
    return redirect('/auth/login')

# Rota protegida de exemplo
@user_app.route('/protected')
@user_service.login_required
def protected_route():
    current_user = user_service.get_current_user()
    return {
        'template': 'protected.tpl',
        'data': {
            'message': f'Área protegida - Bem-vindo, {current_user["name"]}!'
        }
    }
