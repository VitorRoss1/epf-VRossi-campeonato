import json
import os
from models.time import Time
from models.jogador import JogadorGoleiro, JogadorLinha
from models.partida import Partida

class CampeonatoService:
    def __init__(self):
        # Carrega os times, mas suas stats serão zeradas e recalculadas.
        self.times = self._load_times()
        self._times_by_id = {time.id: time for time in self.times}

        # Carrega as partidas com os placares brutos salvos (sem aplicar stats ainda).
        self.partidas = self._load_partidas_raw()
        self._partidas_by_id = {partida.id: partida for partida in self.partidas}

        # CRÍTICO: Após carregar tudo, aplica TODOS os placares salvos para construir as estatísticas acumuladas.
        self._apply_saved_placares()

    def _load_times(self):
        try:
            os.makedirs('data', exist_ok=True) 
            with open('data/times.json') as f:
                times_data = json.load(f)
                times = []
                for data in times_data:
                    # Ao carregar, as estatísticas são inicializadas como ZERO.
                    # Elas serão preenchidas corretamente por _apply_saved_placares.
                    initial_stats = {
                        "vitorias": 0,
                        "derrotas": 0,
                        "empates": 0,
                        "gols_pro": 0,
                        "gols_contra": 0,
                        "Pontos": 0
                    }
                    time = Time(
                        id=data['id'],
                        nome=data['nome'],
                        sigla=data['sigla'],
                        img_path=data['img_path'],
                        stats=initial_stats # GARANTE que as stats começam zeradas ao carregar
                    )
                    
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

    # Carrega partidas e seus placares brutos, sem aplicar estatísticas aos times ainda.
    def _load_partidas_raw(self):
        try:
            os.makedirs('data', exist_ok=True)
            with open('data/partidas.json') as f:
                partidas_data = json.load(f)
                partidas = []
                for data in partidas_data:
                    casa_time = self.get_time(data['casa_id'])
                    fora_time = self.get_time(data['fora_id'])
                    if casa_time and fora_time:
                        partida = Partida(
                            id=data['id'],
                            rodada=data['rodada'],
                            casa=casa_time,
                            fora=fora_time
                        )
                        # Apenas armazena os placares lidos do JSON
                        partida.casa_placar = data.get('casa_placar')
                        partida.fora_placar = data.get('fora_placar')
                        partidas.append(partida)
                return partidas
        except FileNotFoundError:
            print("Arquivo 'data/partidas.json' não encontrado. Retornando lista vazia.")
            return []
        except json.JSONDecodeError:
            print("Erro ao decodificar 'data/partidas.json'. Verifique a sintaxe JSON.")
            return []

    # Recalcula e aplica as estatísticas de todos os placares salvos.
    def _apply_saved_placares(self):
        # Garante que as estatísticas dos times estejam zeradas antes de recalculá-las
        for time in self.times:
            time.stats = {
                "vitorias": 0,
                "derrotas": 0,
                "empates": 0,
                "gols_pro": 0,
                "gols_contra": 0,
                "Pontos": 0
            }

        # Agora, itera sobre as partidas e aplica os placares para atualizar as estatísticas
        # É crucial processar as partidas em ordem de rodada/ID para garantir o acúmulo correto.
        sorted_partidas = sorted(self.partidas, key=lambda p: (p.rodada, p.id))
        for partida in sorted_partidas:
            if partida.casa_placar is not None and partida.fora_placar is not None:
                # Chama definir_placar para re-aplicar as estatísticas aos times associados
                partida.definir_placar(int(partida.casa_placar), int(partida.fora_placar))


    def _save_partidas(self):
        # Salva o estado atual dos placares das partidas de volta ao arquivo JSON
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
        
        # Após salvar os placares das partidas, salva as estatísticas dos times atualizadas
        self._save_times()

    def _save_times(self):
        # Salva as estatísticas ATUAIS dos times no arquivo JSON
        data_to_save = []
        for time in self.times:
            time_data = {
                "id": time.id,
                "nome": time.nome,
                "sigla": time.sigla,
                "img_path": time.img_path,
                "stats": time.stats, # Salva as stats acumuladas
                "jogadores": [] 
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
        # Retorna os times ordenados pela pontuação, vitórias, saldo de gols e gols pro
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
            self._save_partidas() # Salva o estado atual dos placares e dos times no JSON
            return True
        return False
    
    def get_current_rodada(self):
        if not self.partidas:
            return 0
        return max(p.rodada for p in self.partidas)