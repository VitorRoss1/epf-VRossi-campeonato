# generate_fixtures.py
import json
import itertools
import os

# IDs dos times (AJUSTE ESTA LISTA para ter EXATAMENTE os IDs dos seus 20 times do times.json)
# Por exemplo: Se você tem 20 times com IDs de 1 a 20, use:
TIMES_IDS = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20
]

def generate_brazilian_league_fixtures(team_ids):
    fixtures = []
    
    n_teams = len(team_ids)
    if n_teams % 2 != 0:
        team_ids.append('BYE') # Adiciona um "time" dummy se o número for ímpar (para o algoritmo)

    schedule = []
    # Gerar o schedule do primeiro turno (19 rodadas para 20 times)
    # Algoritmo Round-Robin
    temp_teams = list(team_ids)
    fixed_team = temp_teams.pop(0) # Fixa o primeiro time

    for _ in range(n_teams - 1): # n-1 rodadas em um turno
        round_matches = []
        
        # Jogo com o time fixo
        if fixed_team != 'BYE' and temp_teams[-1] != 'BYE':
            round_matches.append((fixed_team, temp_teams[-1]))
        
        # Outros jogos
        for i in range(len(temp_teams) // 2):
            if temp_teams[i] != 'BYE' and temp_teams[len(temp_teams) - 2 - i] != 'BYE':
                round_matches.append((temp_teams[i], temp_teams[len(temp_teams) - 2 - i]))

        schedule.append(round_matches)
        
        # Rotacionar os times (exceto o fixo)
        last_team = temp_teams.pop()
        temp_teams.insert(0, last_team)

    # Agora, distribuir em rodadas de ida e volta
    final_fixtures = []
    current_match_id = 1
    
    # Gerar Turno (Rodadas 1 a 19, se n_teams=20)
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

    # Gerar Returno (Rodadas 20 a 38, se n_teams=20)
    for i, rnd_matches in enumerate(schedule):
        rodada_num = (n_teams - 1) + (i + 1) # Começa a partir da rodada 20
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
os.makedirs(os.path.dirname(output_file), exist_ok=True) # Garante que a pasta 'data' exista
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(all_matches, f, indent=4, ensure_ascii=False)

print(f"Geradas {len(all_matches)} partidas e salvas em '{output_file}'")