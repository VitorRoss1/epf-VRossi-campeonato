from models.user import UserModel
from bottle import request, response
import json

class UserService:
    def __init__(self):
        self.user_model = UserModel()
    
    def authenticate(self, email, password):
        user = self.user_model.get_by_email(email)
        if user and user['password'] == password:
            return user
        return None
    
    def login_required(self, f):
        def wrapper(*args, **kwargs):
            if not self.get_current_user():
                response.status = 401
                return "Acesso não autorizado"
            return f(*args, **kwargs)
        return wrapper
    
    def get_all_users(self):
        return self.user_model.get_all()
    
    def get_user_by_id(self, user_id):
        return self.user_model.get_by_id(user_id)
    
    def get_current_user(self):
        user_id = request.get_cookie('user_id')
        if user_id:
            return self.get_user_by_id(int(user_id))
        return None
    
    def create_user(self, name, email, password):
        if self.user_model.get_by_email(email):
            raise ValueError("Email já cadastrado")
        
        new_id = max([u['id'] for u in self.user_model.get_all()], default=0) + 1
        user = {
            'id': new_id,
            'name': name,
            'email': email,
            'password': password
        }
        self.user_model.add_user(user)
        return user
    
    def update_user(self, user_id, name=None, email=None, password=None):
        user = self.get_user_by_id(user_id)
        if not user:
            return False
        
        if name:
            user['name'] = name
        if email:
            user['email'] = email
        if password:
            user['password'] = password
        
        self.user_model._save()
        return True
    
    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            self.user_model.users.remove(user)
            self.user_model._save()
            return True
        return False