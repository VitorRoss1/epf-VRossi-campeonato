# services/campeonato_service.py
from models.time import Time
from models.partida import Partida
import json

class CampeonatoService:
    def __init__(self):
        self.times = self._load_times()
        self.partidas = self._load_partidas()
    
    def _load_times(self):
        try:
            with open('data/times.json') as f:
                times_data = json.load(f)
                return [
                    Time(
                        id=data['id'],
                        nome=data['nome'],
                        sigla=data['sigla'],
                        img_path=data['img_path'],
                        stats=data.get('stats', {
                            "vitorias": 0,
                            "derrotas": 0,
                            "empates": 0,
                            "gols_pro": 0,
                            "gols_contra": 0,
                            "Pontos": 0
                        })
                    ) 
                    for data in times_data
                ]
        except FileNotFoundError:
            return []
    
    def _load_partidas(self):
        try:
            with open('data/partidas.json') as f:
                partidas_data = json.load(f)
                partidas = []
                for data in partidas_data:
                    casa = next(t for t in self.times if t.id == data['casa_id'])
                    fora = next(t for t in self.times if t.id == data['fora_id'])
                    partida = Partida(
                        id=data['id'],
                        rodada=data['rodada'],
                        casa=casa,
                        fora=fora
                    )
                    if 'casa_placar' in data and 'fora_placar' in data:
                        partida.definir_placar(data['casa_placar'], data['fora_placar'])
                    partidas.append(partida)
                return partidas
        except FileNotFoundError:
            return []
    
    def _save_times(self):
        with open('data/times.json', 'w') as f:
            json.dump([{
                'id': t.id,
                'nome': t.nome,
                'sigla': t.sigla,
                'img_path': t.img_path,
                'stats': t.stats
            } for t in self.times], f, indent=4)
    
    def get_tabela(self):
        return sorted(self.times, key=lambda t: (-t.stats['Pontos'], -t.Saldo_Gols()))
    
    def get_partidas_rodada(self, rodada):
        return [p for p in self.partidas if p.rodada == rodada]
    
    def definir_placar(self, partida_id, casa_gols, fora_gols):
        partida = next(p for p in self.partidas if p.id == partida_id)
        partida.definir_placar(casa_gols, fora_gols)
        self._save_times()
    
    def get_time(self, time_id):
        return next(t for t in self.times if t.id == time_id)