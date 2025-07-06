from bottle import Bottle, request, redirect, template
from services.campeonato_service import CampeonatoService
from services.user_service import UserService

#instanciando
campeonato_app = Bottle()
campeonato_service = CampeonatoService()
user_service = UserService()

#Rota principal:tabela de classificação.
@campeonato_app.route('/')
def tabela():
    times = campeonato_service.get_tabela()
    return template('campeonato/tabela.tpl', times=times, user_service=user_service)

#Rota para rodada específica
@campeonato_app.route('/rodada/<rodada:int>')
def rodada(rodada):
    partidas = campeonato_service.get_partidas_rodada(rodada)
    return template('campeonato/rodada.tpl', rodada=rodada, partidas=partidas, user_service=user_service)

#Rota para detalhes do time(jogadores destaques).
@campeonato_app.route('/time/<time_id:int>')
def time(time_id):
    time = campeonato_service.get_time(time_id)
    return template(
        'campeonato/time.tpl',
        time=time,
        user_service=user_service,
        rodada=campeonato_service.get_current_rodada()
    )