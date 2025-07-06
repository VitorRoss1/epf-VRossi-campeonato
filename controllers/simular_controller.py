from bottle import Bottle, request, redirect, template
from services.campeonato_service import CampeonatoService
from services.user_service import UserService

simular_app = Bottle()
campeonato_service = CampeonatoService() # Instância do serviço
user_service = UserService()

#Rota para dar placares das partidas 
@simular_app.route('/')
@simular_app.route('/<rodada:int>')
def simular_rodada(rodada=1):
    partidas_rodada = campeonato_service.get_partidas_rodada(rodada)
    max_rodada = campeonato_service.get_current_rodada()
    if not max_rodada:
        max_rodada = 1

    return template( # Renderiza 'simular_rodada.tpl' com os dados da rodada
        'simular/simular_rodada.tpl',
        rodada_atual=rodada,
        partidas=partidas_rodada,  #partidas da rodada
        max_rodada=max_rodada,    #rodada máxima (atual)
        user_service=user_service
    )

#Rota para enviar os placares da simulação
@simular_app.route('/enviar_placares_simulacao', method='POST')
def enviar_placares_simulacao():
    rodada_submetida = int(request.forms.get('rodada_atual'))
    
    partidas_rodada = campeonato_service.get_partidas_rodada(rodada_submetida)
    for partida in partidas_rodada:
        casa_gols = int(request.forms.get(f'casa_{partida.id}')) # captura gols da casa do formulário
        fora_gols = int(request.forms.get(f'fora_{partida.id}'))
        #CRÍTICO: Chama o definir_placar do serviço, que atualiza em memória, salva no JSON e RECARREGA o serviço
        campeonato_service.definir_placar(partida.id, casa_gols, fora_gols) 
    
    return redirect(f'/campeonato') #retorna para a tela principal