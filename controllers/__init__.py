# controllers/__init__.py
from .user_controller import user_routes
from .campeonato_controller import create_campeonato_routes

__all__ = ['user_routes', 'create_campeonato_routes']
