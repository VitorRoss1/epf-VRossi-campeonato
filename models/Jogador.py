# models/jogador.py
class Jogador:
    def __init__(self, id: int, nome: str, numero: int, id_time: int):
        self.id = id
        self.nome = nome
        self.numero = numero
        self.id_time = id_time

class JogadorLinha(Jogador):
    def __init__(self, id: int, nome: str, numero: int, id_time: int, posicao: str):
        super().__init__(id, nome, numero, id_time)
        self.posicao = posicao  # Atacante, Meio-campista, Zagueiro, etc.

class JogadorGoleiro(Jogador):
    def __init__(self, id: int, nome: str, numero: int, id_time: int):
        super().__init__(id, nome, numero, id_time)
        self.posicao = "Goleiro"



