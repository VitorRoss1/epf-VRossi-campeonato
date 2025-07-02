from bottle import Bottle, request, redirect
from services.campeonato_service import CampeonatoService
from services.user_service import UserService

campeonato_app = Bottle()
campeonato_service = CampeonatoService()
user_service = UserService()

@campeonato_app.route('/')
def tabela():
    times = campeonato_service.get_tabela()
    return {
        'template': 'campeonato/tabela.tpl',
        'data': {
            'times': times,
            'user_service': user_service
        }
    }

@campeonato_app.route('/rodada/<rodada:int>')
def rodada(rodada):
    partidas = campeonato_service.get_partidas_rodada(rodada)
    return {
        'template': 'campeonato/rodada.tpl',
        'data': {
            'rodada': rodada,
            'partidas': partidas,
            'user_service': user_service
        }
    }

@campeonato_app.route('/enviar-placares', method='POST')
@user_service.login_required
def enviar_placares():
    rodada = int(request.forms.get('rodada'))
    for partida in campeonato_service.get_partidas_rodada(rodada):
        casa_gols = int(request.forms.get(f'casa_{partida.id}'))
        fora_gols = int(request.forms.get(f'fora_{partida.id}'))
        campeonato_service.definir_placar(partida.id, casa_gols, fora_gols)
    return redirect(f'/campeonato/rodada/{rodada}')

@campeonato_app.route('/time/<time_id:int>')
def time(time_id):
    time = campeonato_service.get_time(time_id)
    return {
        'template': 'campeonato/time.tpl',
        'data': {
            'time': time,
            'user_service': user_service,
            'rodada': campeonato_service.get_current_rodada() ##
        }
    }