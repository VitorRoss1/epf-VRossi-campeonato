
from bottle import Bottle, request, redirect, response, template
from services.user_service import UserService
from models.user import UserModel 

user_service = UserService() # Instância global

user_app = Bottle()
auth_app = Bottle()

# --- Rotas relacionadas a usuários ---
@user_app.route('/')
@user_service.login_required
def list_users():
    users = user_service.get_all_users()
    # CORREÇÃO: Passe user_service aqui
    return template('user/list.tpl', users=users, user_service=user_service) 

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
            # CORREÇÃO: Passe user_service aqui
            return template(
                'user/form.tpl',
                user=None,
                error=str(e),
                action='/users/add',
                user_service=user_service # Adicionado
            )
    # CORREÇÃO: Passe user_service aqui
    return template(
        'user/form.tpl',
        user=None,
        action='/users/add',
        user_service=user_service # Adicionado
    )

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
            # CORREÇÃO: Passe user_service aqui
            return template(
                'user/form.tpl',
                user=user,
                error=str(e),
                action=f'/users/edit/{user_id}',
                user_service=user_service # Adicionado
            )
    # CORREÇÃO: Passe user_service aqui
    return template(
        'user/form.tpl',
        user=user,
        action=f'/users/edit/{user_id}',
        user_service=user_service # Adicionado
    )

@user_app.route('/delete/<user_id:int>', method='POST')
@user_service.login_required
def delete_user(user_id):
    if user_service.delete_user(user_id):
        return redirect('/users')
    return "Erro ao excluir usuário"

# --- Rotas de Autenticação ---
@auth_app.route('/login', method=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = user_service.authenticate(
            request.forms.get('email'),
            request.forms.get('password')
        )
        if user:
            response.set_cookie('user_id', str(user['id']), path='/')
            return redirect('/campeonato')
        
        # CORREÇÃO: Passe user_service aqui
        return template('auth/login.tpl', error='Email ou senha inválidos', user_service=user_service)
    
    # CORREÇÃO: Passe user_service aqui
    return template('auth/login.tpl', error=None, user_service=user_service)

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
            # CORREÇÃO: Passe user_service aqui
            return template('auth/register.tpl', error=str(e), user_service=user_service)
    
    # CORREÇÃO: Passe user_service aqui
    return template('auth/register.tpl', error=None, user_service=user_service)

@auth_app.route('/logout')
def logout():
    response.delete_cookie('user_id', path='/')
    return redirect('/auth/login')

# --- Exemplo de rota protegida ---
@user_app.route('/protected')
@user_service.login_required
def protected_route():
    current_user = user_service.get_current_user()
    # CORREÇÃO: Passe user_service aqui
    return template(
        'protected.tpl',
        message=f'Área protegida - Bem-vindo, {current_user["name"]}!',
        user_service=user_service # Adicionado
    )