f# controllers/campeonato_controller.py
from bottle import request, redirect
from services.campeonato_service import CampeonatoService
from .base_controller import BaseController

class CampeonatoController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.campeonato_service = CampeonatoService()
        self.setup_routes()
    
    def setup_routes(self):
        self.app.route('/campeonato', method='GET', callback=self.tabela)
        self.app.route('/campeonato/rodada/<rodada:int>', method='GET', callback=self.rodada)
        self.app.route('/campeonato/enviar-placares', method='POST', callback=self.enviar_placares)
        self.app.route('/campeonato/time/<time_id:int>', method='GET', callback=self.time)
    
    def tabela(self):
        if not self.auth_service.is_authenticated():
            redirect('/login')
        times = self.campeonato_service.get_tabela()
        return self.render('campeonato/tabela', times=times)
    
    def rodada(self, rodada):
        if not self.auth_service.is_authenticated():
            redirect('/login')
        partidas = self.campeonato_service.get_partidas_rodada(rodada)
        return self.render('campeonato/rodada', rodada=rodada, partidas=partidas)
    
    def enviar_placares(self):
        rodada = int(request.forms.get('rodada'))
        for partida in self.campeonato_service.get_partidas_rodada(rodada):
            casa_gols = int(request.forms.get(f'casa_{partida.id}'))
            fora_gols = int(request.forms.get(f'fora_{partida.id}'))
            self.campeonato_service.definir_placar(partida.id, casa_gols, fora_gols)
        redirect('/campeonato')
    
    def time(self, time_id):
        if not self.auth_service.is_authenticated():
            redirect('/login')
        time = self.campeonato_service.get_time(time_id)
        return self.render('campeonato/time', time=time)