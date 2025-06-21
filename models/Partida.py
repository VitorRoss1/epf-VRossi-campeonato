class Partida:
    def __init__(self,rodada:int,casa:Time,Fora:Time):
        self.rodada = rodada
        self.casa = casa
        self.fora = Fora
        self.placar = None

        def definir_placar(self,casa_gols:int,fora_gols:int):
            self.placar = (casa_gols, fora_gols)
            
            if casa_gols > fora_gols:
                self.casa.add_pontos(3)
            elif casa_gols < fora_gols:
                self.fora.add_pontos(3)
            else:
                self.casa.add_pontos(1)
                self.fora.add_pontos(1)

                ##