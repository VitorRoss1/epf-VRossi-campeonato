class Time:
    def __init__(self, id, nome, sigla, img_path, stats=None):
        self.id = id
        self.nome = nome
        self.sigla = sigla
        self.img_path = img_path
        self.stats = stats or {
            "vitorias": 0,
            "derrotas": 0,
            "empates": 0,
            "gols_pro": 0,
            "gols_contra": 0,
            "Pontos": 0
        }
        self._jogadores = []  #2 jogadores destaques

    def add_jogador(self, jogador):
     self._jogadores.append(jogador)

    def Saldo_Gols(self):
     return self.stats["gols_pro"] - self.stats["gols_contra"]


    @property
    def getJogadores(self):
        return self._jogadores
    
