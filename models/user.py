import json
import os

class UserModel:
    FILE_PATH = 'data/users.json'
    
    def __init__(self):
        self.users = self._load()
    
    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH) as f:
            return json.load(f)
    
    def _save(self):
        with open(self.FILE_PATH, 'w') as f:
            json.dump(self.users, f, indent=4)
    
    def get_all(self):
        return self.users
    
    def get_by_id(self, user_id):
        return next((u for u in self.users if u['id'] == user_id), None)
    
    def get_by_email(self, email):
        return next((u for u in self.users if u['email'] == email), None)
    
    def add_user(self, user):
        self.users.append(user)
        self._save()