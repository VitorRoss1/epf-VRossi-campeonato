from models.time import Time

class Partida:
    def __init__(self,id:int, rodada: int, casa_id:int, fora_id:int):  # Use aspas para forward reference
        self.rodada = rodada
        self.casa_id = casa_id
        self.fora_id = fora_id
        self.casa_placar = None
        self.fora_placar = None

    def definir_placar(self, casa_gols: int, fora_gols: int):
        self.casa_placar = casa_gols  
        self.fora_placar = fora_gols  
        
        self.casa.stats["gols_pro"] += casa_gols
        self.casa.stats["gols_contra"] += fora_gols
        self.fora.stats["gols_pro"] += fora_gols
        self.fora.stats["gols_contra"] += casa_gols

        if casa_gols > fora_gols:
            self.casa.stats["vitorias"] += 1
            self.casa.stats["Pontos"] += 3  # Consistente com maiúscula
            self.fora.stats["derrotas"] += 1
        elif casa_gols < fora_gols:
            self.fora.stats["vitorias"] += 1
            self.fora.stats["Pontos"] += 3  
            self.casa.stats["derrotas"] += 1
        else:
            self.casa.stats["empates"] += 1
            self.fora.stats["empates"] += 1
            self.casa.stats["Pontos"] += 1 
            self.fora.stats["Pontos"] += 1  