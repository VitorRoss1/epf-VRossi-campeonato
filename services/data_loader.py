import json
from models.time import Time
from models.partida import Partida

def load_times():
    try:
        with open('data/times.json') as f:
            return [Time(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []

def load_partidas_darodada(rodada: int):
    try:
        with open('data/partidas.json') as f:
            return [
                Partida(**data) 
                for data in json.load(f) 
                if data['rodada'] == rodada
            ]
    except FileNotFoundError:
        return []
    