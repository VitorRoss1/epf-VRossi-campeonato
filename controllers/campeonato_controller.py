from bottle import template, request 
from .base_controller import BaseController
from models.time import Time
from models.partida import Partida
from services.data_loader import load_times, load_partidas_darodada

class CampeonatoController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/campeonato/rodada/<rodada_numero>', callback=self.display_rodada)
        self.app.route('/campeonato/enviar-placares', method='POST', callback=self.enviar_placares)
        self.app.route('/campeonato/time/<time_id>', callback=self.display_time)

    def display_rodada(self, rodada_numero):
        partidas = load_partidas_darodada(int(rodada_numero))
        return self.render('rodada_partidas', 
                         partidas=partidas, 
                         rodada=rodada_numero)

    def enviar_placares(self):
        rodada_numero = int(request.forms.get('rodada'))
        partidas = load_partidas_darodada(rodada_numero)

        for partida in partidas:
            casa_gols = int(request.forms.get(f'casa_{partida.id}'))
            fora_gols = int(request.forms.get(f'fora_{partida.id}'))
            partida.definir_placar(casa_gols, fora_gols)

        times = load_times()
        return self.render('tabela_classificacao', times=times)

    def display_time(self, time_id):
        time = next(t for t in load_times() if t.id == int(time_id))
        return self.render('elenco_time', time=time)