class Partida:
    def __init__(self, id, rodada, casa, fora):
        self.id = id
        self.rodada = rodada
        self.casa = casa
        self.fora = fora
        self.casa_placar = None
        self.fora_placar = None

    def definir_placar(self, casa_gols, fora_gols):
        self.casa_placar = casa_gols
        self.fora_placar = fora_gols
        
        # CORREÇÃO DEFINITIVA: Lógica de atualização de estatísticas (sem inversão)
        # Atualiza estatísticas para o time da CASA
        self.casa.stats["gols_pro"] += casa_gols
        self.casa.stats["gols_contra"] += fora_gols

        # Atualiza estatísticas para o time de FORA
        self.fora.stats["gols_pro"] += fora_gols
        self.fora.stats["gols_contra"] += casa_gols

        if casa_gols > fora_gols: # Casa VENCE
            self.casa.stats["vitorias"] += 1
            self.casa.stats["Pontos"] += 3
            self.fora.stats["derrotas"] += 1
        elif fora_gols > casa_gols: # Fora VENCE
            self.fora.stats["vitorias"] += 1
            self.fora.stats["Pontos"] += 3
            self.casa.stats["derrotas"] += 1
        else: # Empate
            self.casa.stats["empates"] += 1
            self.fora.stats["empates"] += 1
            self.casa.stats["Pontos"] += 1
            self.fora.stats["Pontos"] += 1