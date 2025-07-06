class Time:
    def __init__(self, id, nome, sigla, img_path, stats=None):
        self.id = id
        self.nome = nome
        self.sigla = sigla
        self.img_path = img_path
        self._stats = stats or { #ENCAPSULAMENTO _PRIVATE
            "vitorias": 0,
            "derrotas": 0,
            "empates": 0,
            "gols_pro": 0,
            "gols_contra": 0,
            "Pontos": 0
        }
        self._jogadores = []  #2 jogadores destaques(CRAQUES)

    def add_jogador(self, jogador):
     self._jogadores.append(jogador)

    def Saldo_Gols(self):
     return self._stats["gols_pro"] - self._stats["gols_contra"]

    @property #METODO Q PODE SER CHAMADO COMO ATRIBUTO
    def getJogadores(self):
        return self._jogadores 
    
