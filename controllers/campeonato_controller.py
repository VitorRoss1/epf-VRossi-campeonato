from bottle import Bottle, request, redirect, template
from services.campeonato_service import CampeonatoService
from services.user_service import UserService

campeonato_app = Bottle()
campeonato_service = CampeonatoService()
user_service = UserService()

@campeonato_app.route('/')
def tabela():
    times = campeonato_service.get_tabela()
    return template('campeonato/tabela.tpl', times=times, user_service=user_service)

@campeonato_app.route('/rodada/<rodada:int>')
def rodada(rodada):
    partidas = campeonato_service.get_partidas_rodada(rodada)
    # A view 'rodada.tpl' não terá mais o botão de salvar placares.
    # Ela será apenas para visualização.
    return template('campeonato/rodada.tpl', rodada=rodada, partidas=partidas, user_service=user_service)

# ROTA /enviar-placares FOI REMOVIDA DAQUI.
# A submissão de placares para o campeonato real será feita SOMENTE pela rota de simulação.


@campeonato_app.route('/time/<time_id:int>')
def time(time_id):
    time = campeonato_service.get_time(time_id)
    return template(
        'campeonato/time.tpl',
        time=time,
        user_service=user_service,
        rodada=campeonato_service.get_current_rodada()
    )