class Jogador:
    def __init__(self, id, nome, numero, id_time):
        self.id = id
        self.nome = nome
        self.numero = numero
        self.id_time = id_time

class JogadorLinha(Jogador):  #herança de Jogador
    def __init__(self, id, nome, numero, id_time, posicao):
        super().__init__(id, nome, numero, id_time)
        self.posicao = posicao

class JogadorGoleiro(Jogador):
    def __init__(self, id, nome, numero, id_time):
        super().__init__(id, nome, numero, id_time)
        self.posicao = "Goleiro"



