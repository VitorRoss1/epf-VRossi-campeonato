import json
import os
from models.time import Time
from models.jogador import JogadorGoleiro, JogadorLinha
from models.partida import Partida

class CampeonatoService:
    def __init__(self):
        self.times = self._load_times()
        self._times_by_id = {time.id: time for time in self.times}

        self.partidas = self._load_partidas()
        self._partidas_by_id = {partida.id: partida for partida in self.partidas}


        # Mapeia times por ID para acesso rápido
        self._times_by_id = {time.id: time for time in self.times}
        # Mapeia partidas por ID para acesso rápido
        self._partidas_by_id = {partida.id: partida for partida in self.partidas}


    def _load_times(self):
        try:
            
            os.makedirs('data', exist_ok=True) # Garante que data existe
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
                    
                    # Carrega jogadores destaque
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
                        
                        time.add_jogador(jogador)
                    
                    times.append(time)
                return times
                
        except FileNotFoundError:
            print("Arquivo 'data/times.json' não encontrado. Retornando lista vazia.")
            return []
        except json.JSONDecodeError:
            print("Erro ao decodificar 'data/times.json'. Verifique a sintaxe JSON.")
            return []

    def _load_partidas(self):
        try:
            
            os.makedirs('data', exist_ok=True)
            with open('data/partidas.json') as f:
                partidas_data = json.load(f)
                partidas = []
                for data in partidas_data:
                    casa_time = self.get_time(data['casa_id'])
                    fora_time = self.get_time(data['fora_id'])
                    if casa_time and fora_time: # Garante que os times existam antes de criar a partida
                        partida = Partida(
                            id=data['id'],
                            rodada=data['rodada'],
                            casa=casa_time,
                            fora=fora_time
                        )
                        # Se já houver placares no JSON, carrega
                        # Tratar placares como 0 se forem None
                        casa_placar = data.get('casa_placar')
                        fora_placar = data.get('fora_placar')

                        if casa_placar is not None and fora_placar is not None: #Só chamo definir placar se os dois nao forem None 
                            partida.definir_placar(int(casa_placar), int(fora_placar)) # Garante que sejam ints

                        partidas.append(partida)
                return partidas
        except FileNotFoundError:
            print("Arquivo 'data/partidas.json' não encontrado. Retornando lista vazia.")
            return []
        except json.JSONDecodeError:
            print("Erro ao decodificar 'data/partidas.json'. Verifique a sintaxe JSON.")
            return []

    def _save_partidas(self):
        # Salva o estado atual dos placares das partidas de volta ao arquivo
        data_to_save = []
        for partida in self.partidas:
            data_to_save.append({
                "id": partida.id,
                "rodada": partida.rodada,
                "casa_id": partida.casa.id,
                "fora_id": partida.fora.id,
                "casa_placar": partida.casa_placar,
                "fora_placar": partida.fora_placar
            })
        with open('data/partidas.json', 'w') as f:
            json.dump(data_to_save, f, indent=4)
        
        # Salva também as stats dos times, pois eles são atualizados
        self._save_times()

    def _save_times(self):
        data_to_save = []
        for time in self.times:
            time_data = {
                "id": time.id,
                "nome": time.nome,
                "sigla": time.sigla,
                "img_path": time.img_path,
                "stats": time.stats,
                "jogadores": [] # Salva apenas o ID e nome dos jogadores, ou adicione todos os atributos tlvz
            }
            for jogador in time.getJogadores:
                jogador_data = {
                    "id": jogador.id,
                    "nome": jogador.nome,
                    "numero": jogador.numero,
                    "posicao": jogador.posicao,
                }
                time_data['jogadores'].append(jogador_data)
            data_to_save.append(time_data)

        with open('data/times.json', 'w') as f:
            json.dump(data_to_save, f, indent=4)


    def get_tabela(self):
        #retorna os times ordenados pela pontuação, vitórias, saldo de gols e gols pro
        return sorted(
            self.times,
            key=lambda t: (t.stats["Pontos"], t.stats["vitorias"], t.Saldo_Gols(), t.stats["gols_pro"]),
            reverse=True
        )

    def get_partidas_rodada(self, rodada):
        return [p for p in self.partidas if p.rodada == rodada]

    def get_time(self, time_id):
        return self._times_by_id.get(time_id)

    def definir_placar(self, partida_id, casa_gols, fora_gols):
        partida = self._partidas_by_id.get(partida_id)
        if partida:
            partida.definir_placar(casa_gols, fora_gols)
            self._save_partidas() # Salva o estado atual dos placares e times
            return True
        return False
    
    def get_current_rodada(self):
        # Determina a rodada atual com base nas partidas existentes
        if not self.partidas:
            return 0
        return max(p.rodada for p in self.partidas)