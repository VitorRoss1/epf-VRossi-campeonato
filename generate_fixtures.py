import json
import itertools

# IDs dos times (extraídos do seu times.json)
# CERTIFIQUE-SE DE QUE ESTES IDs CORRESPONDAM AOS SEUS TIMES REAIS
# E QUE VOCÊ TENHA EXATAMENTE 20 TIMES NO SEU times.json
TIMES_IDS = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20
]

def generate_brazilian_league_fixtures(team_ids):
    fixtures = []
    partida_id_counter = 1

    # Fase de Turno
    rodada_atual = 1
    for i, home_team_id in enumerate(team_ids):
        for away_team_id in team_ids:
            if home_team_id != away_team_id:
                # Simulamos um "sorteio" simples para criar rodadas balanceadas
                # Isso é uma simplificação. Um algoritmo real de tabela é mais complexo.
                # Para um campeonato de 38 rodadas, o ideal seria ter 19 jogos em casa e 19 fora para cada time.
                # Aqui, estamos apenas garantindo que todos joguem contra todos duas vezes.
                
                # Para simplificar o agrupamento em rodadas, vamos criar todas as partidas e depois distribuí-las.
                fixtures.append({
                    "id": partida_id_counter,
                    "rodada": 0, # Temporariamente 0, será ajustado depois
                    "casa_id": home_team_id,
                    "fora_id": away_team_id,
                    "casa_placar": None,
                    "fora_placar": None
                })
                partida_id_counter += 1

    # Vamos tentar distribuir em rodadas de 10 jogos
    # Para 20 times, cada rodada tem 10 jogos (20 times / 2 times por jogo)
    # Total de jogos por turno: 20 * 19 = 380 jogos (turno e returno)
    # Turno: 190 jogos
    # Returno: 190 jogos

    all_matches_generated = []
    # Gerar partidas de ida (todos contra todos uma vez)
    match_pairs = list(itertools.permutations(team_ids, 2)) # Gera todas as combinações de 2 times (A vs B e B vs A)
    
    # Criar um dicionário para controlar os confrontos já gerados em um turno
    # para garantir que cada time jogue com cada outro apenas uma vez por turno como mandante/visitante
    
    # Implementação de algoritmo round-robin simples para gerar rodadas
    # Este é um algoritmo básico e pode não seguir todas as regras da CBF, mas gera 380 partidas.
    
    # Lista de todos os times para o agendamento
    n_teams = len(team_ids)
    if n_teams % 2 != 0:
        team_ids.append('BYE') # Adiciona um "time" dummy se o número for ímpar

    schedule = []
    for _ in range(n_teams - 1): # n-1 rodadas em um turno
        round_matches = []
        teams_to_schedule = list(team_ids)
        
        # O time fixo na primeira posição
        fixed_team = teams_to_schedule.pop(0)
        
        # Distribuir os outros times
        top_half = teams_to_schedule[:len(teams_to_schedule)//2]
        bottom_half = teams_to_schedule[len(teams_to_schedule)//2:]
        bottom_half.reverse() # Inverte a metade inferior para o confronto

        # Adiciona o jogo com o time fixo
        if fixed_team != 'BYE' and bottom_half[0] != 'BYE':
            round_matches.append((fixed_team, bottom_half[0]))
        
        # Adiciona os outros jogos
        for i in range(len(top_half)):
            if top_half[i] != 'BYE' and bottom_half[i+1] != 'BYE': # bottom_half[0] já foi usado
                 round_matches.append((top_half[i], bottom_half[i+1]))

        schedule.append(round_matches)
        
        # Rotaciona os times (exceto o fixo)
        last_of_bottom = teams_to_schedule.pop()
        first_of_top = teams_to_schedule.pop(0)
        teams_to_schedule.insert(0, last_of_bottom)
        teams_to_schedule.append(first_of_top)
        teams_to_schedule.insert(0, fixed_team) # Coloca o time fixo de volta na primeira posição para a próxima iteração

    # Agora, mapear para as rodadas do Brasileirão (38 rodadas, 19 turnos/19 returnos)
    final_fixtures = []
    current_match_id = 1
    
    # Gerar Turno (Rodadas 1 a 19)
    for i, rnd_matches in enumerate(schedule):
        rodada_num = i + 1
        for team1, team2 in rnd_matches:
            final_fixtures.append({
                "id": current_match_id,
                "rodada": rodada_num,
                "casa_id": team1,
                "fora_id": team2,
                "casa_placar": None,
                "fora_placar": None
            })
            current_match_id += 1

    # Gerar Returno (Rodadas 20 a 38)
    for i, rnd_matches in enumerate(schedule):
        rodada_num = (n_teams - 1) + (i + 1) # Começa da rodada 20
        for team1, team2 in rnd_matches:
            # Inverte os times para o returno
            final_fixtures.append({
                "id": current_match_id,
                "rodada": rodada_num,
                "casa_id": team2, # Fora no turno vira Casa no returno
                "fora_id": team1, # Casa no turno vira Fora no returno
                "casa_placar": None,
                "fora_placar": None
            })
            current_match_id += 1
            
    # Filtra partidas com "BYE" se tivermos adicionado um time dummy
    return [match for match in final_fixtures if 'BYE' not in [match['casa_id'], match['fora_id']]]


# Gerar as partidas
all_matches = generate_brazilian_league_fixtures(TIMES_IDS)

# Salvar no arquivo JSON
output_file = 'data/partidas.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(all_matches, f, indent=4, ensure_ascii=False)

print(f"Geradas {len(all_matches)} partidas e salvas em '{output_file}'")