class Jogador:
    def __init__(self,id:int,nome:str,numero:int, id_time:int = int):
        self.id = id
        self.nome = nome
        self.numero = numero
        
        #herança
        class JogadorLinha(Jogador):
         def __init__(self, id: int, nome: str, numero: int):
          super().__init__(id, nome, numero)
          self.posicao = "Linha"

        class JogadorGoleiro(Jogador):
         def __init__(self, id: int, nome: str, numero: int):
          super().__init__(id, nome, numero)
          self.posicao = "Goleiro"



