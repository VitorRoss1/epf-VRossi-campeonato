class Time:
    def __init__(self, id: int, nome: str, sigla: str):
        self.id = id
        self.nome = nome
        self.sigla = sigla
        self._jogadores = []
        self._pontos = 0  # encapsulamentos

    def add_jogador(self, jogador):
        if len(self._jogadores) < 11:
            self._jogadores.append(jogador)
            return True
        return False

    def add_pontos(self, pontos):
        if pontos > 0:
            self._pontos += pontos

    # getters
    @property
    def getJogadores(self):
        return self._jogadores.copy()

    @property
    def getPontos(self):
        return self._pontos
    
