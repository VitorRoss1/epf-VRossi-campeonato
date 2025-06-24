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
        """Configura todas as rotas do campeonato"""
        self.app.route('/rodada/<rodada_numero>', callback=self.display_rodada)
        self.app.route('/enviar-placares', method='POST', callback=self.enviar_placares)
        self.app.route('/time/<time_id>', callback=self.display_time)

    def display_rodada(self, rodada_numero):
        """Exibe os jogos de uma rodada específica"""
        partidas = load_partidas_darodada(int(rodada_numero))
        return self.render('rodada_partidas',
                         partidas=partidas,
                         rodada=rodada_numero)

    def enviar_placares(self):
        """Processa os placares enviados pelo formulário"""
        rodada_numero = int(request.forms.get('rodada'))
        partidas = load_partidas_darodada(rodada_numero)

        for partida in partidas:
            casa_gols = int(request.forms.get(f'casa_{partida.id}'))
            fora_gols = int(request.forms.get(f'fora_{partida.id}'))
            partida.definir_placar(casa_gols, fora_gols)

        times = load_times()
        return self.render('tabela_classificacao', 
                         times=sorted(times, 
                                    key=lambda t: (-t.stats['Pontos'], 
                                                 -t.Saldo_Gols())))

    def display_time(self, time_id):
        """Exibe o elenco de um time específico"""
        time = next(t for t in load_times() if t.id == int(time_id))
        return self.render('elenco_time', 
                         time=time,
                         jogadores=time.getJogadores)

def create_campeonato_routes():
    from bottle import Bottle
    routes = Bottle()
    CampeonatoController(routes)
    return routes