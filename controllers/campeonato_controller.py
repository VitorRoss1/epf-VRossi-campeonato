# controllers/campeonato_controller.py

from bottle import Bottle, request, redirect, template
from services.campeonato_service import CampeonatoService
from services.user_service import UserService

# user_service já está instanciado aqui, apenas certifique-se de passá-lo
campeonato_app = Bottle()
campeonato_service = CampeonatoService()
user_service = UserService() # A instância já existe e está correta

@campeonato_app.route('/')
def tabela():
    times = campeonato_service.get_tabela()
    # CORREÇÃO: Passe user_service aqui
    return template('campeonato/tabela.tpl', times=times, user_service=user_service)

@campeonato_app.route('/rodada/<rodada:int>')
def rodada(rodada):
    partidas = campeonato_service.get_partidas_rodada(rodada)
    # CORREÇÃO: Passe user_service aqui
    return template('campeonato/rodada.tpl', rodada=rodada, partidas=partidas, user_service=user_service)

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
    # CORREÇÃO: Passe user_service aqui
    return template(
        'campeonato/time.tpl',
        time=time,
        user_service=user_service, # Adicionado
        rodada=campeonato_service.get_current_rodada()
    )