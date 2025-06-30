
# controllers/user_controller.py
from bottle import Bottle, request, redirect, abort
from services.user_service import UserService
from utils.auth import login_required, admin_required

user_routes = Bottle()
user_service = UserService()

@user_routes.route('/')
@login_required
@admin_required
def list_users():
    """Lista todos os usuários do sistema"""
    users = user_service.get_all_users()
    return {
        'template': 'users.tpl',
        'data': {
            'users': users,
            'title': 'Gerenciamento de Usuários'
        }
    }

@user_routes.route('/add', method=['GET', 'POST'])
@login_required
@admin_required
def add_user():
    """Adiciona um novo usuário"""
    if request.method == 'GET':
        return {
            'template': 'user_form.tpl',
            'data': {
                'title': 'Adicionar Usuário',
                'action': '/users/add',
                'user': None
            }
        }
    
    # Processar POST
    name = request.forms.get('name')
    email = request.forms.get('email')
    password = request.forms.get('password')
    is_admin = request.forms.get('is_admin') == 'on'
    
    try:
        user_service.create_user(name, email, password, is_admin)
        return redirect('/users')
    except ValueError as e:
        return {
            'template': 'user_form.tpl',
            'data': {
                'title': 'Adicionar Usuário',
                'action': '/users/add',
                'user': None,
                'error': str(e)
            }
        }

@user_routes.route('/edit/<user_id:int>', method=['GET', 'POST'])
@login_required
@admin_required
def edit_user(user_id):
    """Edita um usuário existente"""
    user = user_service.get_user_by_id(user_id)
    if not user:
        abort(404, "Usuário não encontrado")
    
    if request.method == 'GET':
        return {
            'template': 'user_form.tpl',
            'data': {
                'title': 'Editar Usuário',
                'action': f'/users/edit/{user_id}',
                'user': user
            }
        }
    
    # Processar POST
    name = request.forms.get('name')
    email = request.forms.get('email')
    password = request.forms.get('password')
    is_admin = request.forms.get('is_admin') == 'on'
    
    try:
        user_service.update_user(user_id, name, email, password, is_admin)
        return redirect('/users')
    except ValueError as e:
        return {
            'template': 'user_form.tpl',
            'data': {
                'title': 'Editar Usuário',
                'action': f'/users/edit/{user_id}',
                'user': user,
                'error': str(e)
            }
        }

@user_routes.route('/delete/<user_id:int>', method='POST'])
@login_required
@admin_required
def delete_user(user_id):
    """Remove um usuário"""
    if not user_service.delete_user(user_id):
        abort(404, "Usuário não encontrado")
    return redirect('/users')

@user_routes.route('/profile', method=['GET', 'POST'])
@login_required
def user_profile():
    """Perfil do usuário logado"""
    user = user_service.get_current_user(request)
    
    if request.method == 'GET':
        return {
            'template': 'profile.tpl',
            'data': {
                'title': 'Meu Perfil',
                'user': user
            }
        }
    
    # Processar POST
    name = request.forms.get('name')
    email = request.forms.get('email')
    current_password = request.forms.get('current_password')
    new_password = request.forms.get('new_password')
    
    try:
        user_service.update_profile(
            user.id,
            name,
            email,
            current_password,
            new_password
        )
        return redirect('/users/profile')
    except ValueError as e:
        return {
            'template': 'profile.tpl',
            'data': {
                'title': 'Meu Perfil',
                'user': user,
                'error': str(e)
            }
        }