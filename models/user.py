import json
import os

class User:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

class UserModel:
    FILE_PATH = 'data/users.json'
    
    def __init__(self):
        self.users = self._load()
    
    def _load(self):
        # Garante que o diretório 'data' exista
        os.makedirs(os.path.dirname(self.FILE_PATH), exist_ok=True)
        if not os.path.exists(self.FILE_PATH):
            # Cria o arquivo com uma lista vazia se ele não existir
            with open(self.FILE_PATH, 'w') as f:
                json.dump([], f)
            return []
        with open(self.FILE_PATH) as f:
            return json.load(f)
    
    def _save(self):
        with open(self.FILE_PATH, 'w') as f:
            json.dump(self.users, f, indent=4)
    
    #getters
    def get_all(self):
        return self.users
    
    def get_by_id(self, user_id):
        # Garante que user_id seja integer para comparação correta
        return next((u for u in self.users if u['id'] == user_id), None)
    
    def get_by_email(self, email):
        return next((u for u in self.users if u['email'] == email), None)
    
    def add_user(self, user):
        self.users.append(user)
        self._save()