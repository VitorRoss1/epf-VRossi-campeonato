# models/time.py
class Time:
    def __init__(self, id: int, nome: str, sigla: str, img_path: str, stats: dict = None):
        self.id = id
        self.nome = nome
        self.sigla = sigla
        self.img_path = img_path
        self._jogadores = []  # Encapsulamento
        self.stats = stats or {
            "vitorias": 0,
            "derrotas": 0,
            "empates": 0,
            "gols_pro": 0,
            "gols_contra": 0,
            "Pontos": 0
        }

    def add_jogador(self, jogador):
        if len(self._jogadores) < 11:
            self._jogadores.append(jogador)
            return True
        return False

    def Saldo_Gols(self):
        return self.stats["gols_pro"] - self.stats["gols_contra"]

    @property
    def getJogadores(self):
        return self._jogadores.copy()

    
