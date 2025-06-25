import json
from models.time import Time
from models.partida import Partida

def load_times():
    try:
        with open('data/times.json') as f:
            times_data = json.load(f)
            return [
                Time(
                    id=data['id'],
                    nome=data['nome'],
                    sigla=data['sigla'],
                    img_path=data['img_path'],
                    stats=data.get('stats')  # Passa os stats se existirem
                ) 
                for data in times_data
            ]
    except FileNotFoundError:
        return []

def load_partidas_darodada(rodada: int):
    try:
        with open('data/partidas.json') as f:
            return [
                Partida(
                    id=data['id'],
                    rodada=data['rodada'],
                    casa_id=data['casa_id'],
                    fora_id=data['fora_id']
                )
                for data in json.load(f) 
                if data['rodada'] == rodada
            ]
    except FileNotFoundError:
        return []
    