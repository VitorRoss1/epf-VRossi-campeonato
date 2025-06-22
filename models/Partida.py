class Partida:
    def __init__(self,rodada:int,casa:Time,fora:Time,casa_placar:int,):
        self.rodada = rodada
        self.casa = casa
        self.fora = fora
        self.casa_placar = None
        self.fora_placar = None

        def definir_placar(self,casa_gols:int,fora_gols:int):
            self.casa_placar = casa
            self.fora_placar = fora
            
            self.casa.stats["gols_pro"] += casa
            self.casa.stats["gols_contra"] += fora
            self.fora.stats["gols_pro"] += fora
            self.fora.stats["gols_contra"] += casa

            if casa > fora:
                self.casa.stats["vitorias"] += 1
                self.casa.stats["pontos"] += 3
                self.fora.stats["derrotas"] += 1

            elif casa < fora:
                self.fora.stats["vitorias"] += 1
                self.fora.stats["pontos"] += 3
                self.casa.stats["derrotas"] += 1

            else:
                self.casa.stats["empates"] += 1
                self.fora.stats["empates"] += 1
                self.casa.stats["pontos"] += 1
                self.fora.stats["pontos"] += 1