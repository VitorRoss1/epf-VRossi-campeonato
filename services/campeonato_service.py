import json
from models.time import Time  # ajuste o caminho conforme necessário
from models.jogador import JogadorGoleiro  
from models.jogador import JogadorLinha 

def _load_times(self):
    try:
        with open('data/times.json') as f:
            times_data = json.load(f)
            times = []
            
            for data in times_data:
                time = Time(
                    id=data['id'],
                    nome=data['nome'],
                    sigla=data['sigla'],
                    img_path=data['img_path'],
                    stats=data.get('stats')
                )
                
                # Carrega jogadores
                for jogador_data in data.get('jogadores', []):
                    if jogador_data.get('posicao') == 'Goleiro':
                        jogador = JogadorGoleiro(
                            id=jogador_data['id'],
                            nome=jogador_data['nome'],
                            numero=jogador_data['numero'],
                            id_time=data['id']
                        )
                    else:
                        jogador = JogadorLinha(
                            id=jogador_data['id'],
                            nome=jogador_data['nome'],
                            numero=jogador_data['numero'],
                            id_time=data['id'],
                            posicao=jogador_data.get('posicao', 'Linha')
                        )
                    
                    # Adiciona atributos extras se existirem
                    if 'idade' in jogador_data:
                        jogador.idade = jogador_data['idade']
                    if 'nacionalidade' in jogador_data:
                        jogador.nacionalidade = jogador_data['nacionalidade']
                    
                    time.add_jogador(jogador)
                
                times.append(time)
            return times
            
    except FileNotFoundError:
        return []