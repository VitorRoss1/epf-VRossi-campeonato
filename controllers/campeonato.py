from bottle import route, template, request
from seervices.data_loader import load_times, load_partidas_darodada
from services.table_calculator import calculate_table

@route('/rodada/<rodada_numero>')
def display_rodada(rodada_numero):
 partidas = load_partidas_darodada(int(rodada_numero))
 return template('rodada_partidas', partidas=partidas, rodada=rodada_numero)
    
@route('/enviar-placares', method='POST')
def enviar_placares():
 rodada_numero = int(request.forms.get('Rodada'))
 partidas = load_partidas_darodada(rodada_numero)

 for partida in partidas:
     casa_placar = int(request.forms.get(f'casa_placar_{partida.id}'))
     fora_placar = int(request.forms.get(f'fora_placar_{partida.id}'))
     partida.definir_placar(casa_placar, fora_placar)

#atualizar a tabela
 times= load_times()
 tabela = calculate_table(times)
 return template('tabela de clasificacao', tabela=tabela, rodada=rodada_numero)

@route('/time/<time_id>')
def display_time(time_id):
  time = next(t for t in load_times() if t.id == int(time_id))
  return template('tabela_classificacao', time=time)