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
        
        self.casa._stats["gols_pro"] += casa_gols
        self.casa._stats["gols_contra"] += fora_gols

        self.fora._stats["gols_pro"] += fora_gols
        self.fora._stats["gols_contra"] += casa_gols

        if casa_gols > fora_gols: #Casa VENCE
            self.casa._stats["vitorias"] += 1
            self.casa._stats["Pontos"] += 3
            self.fora._stats["derrotas"] += 1
        elif fora_gols > casa_gols: #Fora VENCE
            self.fora._stats["vitorias"] += 1
            self.fora._stats["Pontos"] += 3
            self.casa._stats["derrotas"] += 1
        else: #Empate
            self.casa._stats["empates"] += 1
            self.fora._stats["empates"] += 1
            self.casa._stats["Pontos"] += 1
            self.fora._stats["Pontos"] += 1