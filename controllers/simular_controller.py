# controllers/simular_controller.py

from bottle import Bottle, request, redirect, template
from services.campeonato_service import CampeonatoService
from services.user_service import UserService
from models.time import Time
from models.partida import Partida

simular_app = Bottle()
campeonato_service = CampeonatoService() # Instância de CampeonatoService
user_service = UserService()

@simular_app.route('/')
@simular_app.route('/<rodada:int>')
def simular_rodada(rodada=1):
    partidas_rodada = campeonato_service.get_partidas_rodada(rodada)
    max_rodada = campeonato_service.get_current_rodada()
    if not max_rodada:
        max_rodada = 1

    return template(
        'simular/simular_rodada.tpl',
        rodada_atual=rodada,
        partidas=partidas_rodada,
        max_rodada=max_rodada,
        user_service=user_service
    )

@simular_app.route('/enviar_placares_simulacao', method='POST')
def enviar_placares_simulacao():
    rodada_submetida = int(request.forms.get('rodada_atual'))
    
    simulated_teams_stats = {}
    for team in campeonato_service.times:
        simulated_teams_stats[team.id] = team.stats.copy()

    temp_teams = {team.id: Time(id=team.id, nome=team.nome, sigla=team.sigla, img_path=team.img_path, stats=simulated_teams_stats[team.id]) for team in campeonato_service.times}

    partidas_submetidas = campeonato_service.get_partidas_rodada(rodada_submetida)
    
    simulated_partidas = []
    for partida_original in partidas_submetidas:
        temp_partida = Partida(
            id=partida_original.id,
            rodada=partida_original.rodada,
            casa=temp_teams[partida_original.casa.id],
            fora=temp_teams[partida_original.fora.id]
        )
        casa_gols = int(request.forms.get(f'casa_{partida_original.id}'))
        fora_gols = int(request.forms.get(f'fora_{partida_original.id}'))
        temp_partida.definir_placar(casa_gols, fora_gols)
        simulated_partidas.append(temp_partida)

    simulated_tabela = sorted(
        list(temp_teams.values()),
        key=lambda t: (t.stats["Pontos"], t.stats["vitorias"], t.Saldo_Gols(), t.stats["gols_pro"]),
        reverse=True
    )

    # CORREÇÃO AQUI: Passe campeonato_service ao template
    return template(
        'simular/resultado_simulacao.tpl',
        rodada_simulada=rodada_submetida,
        simulated_tabela=simulated_tabela,
        simulated_partidas=simulated_partidas,
        user_service=user_service,
        campeonato_service=campeonato_service 
    )