import random
from Objetos.HistoricoAcoes import historico


class Inimigo:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.bloqueio = 0

    def atacar(self, jogador):
        dano = random.randint(1, 8)
        print(f"{self.nome} causou {dano} de dano!")
        historico.registrar(f"{self.nome} atacou {jogador.nome} e causou {dano} de dano.")
        jogador.vida -= dano
        return dano

    #def curar(self):
        quantidade_cura = random.randint(1, 10)
        self.vida += quantidade_cura
        print(f"{self.nome} curou {quantidade_cura}")
        historico.registrar(f"{self.nome} curou {quantidade_cura} pontos de vida.")
        return quantidade_cura

    def bloquear(self):
        quantidade_bloqueio = random.randint(1, 6)
        self.bloqueio = quantidade_bloqueio
        print(f"{self.nome} criou um bloqueio de {quantidade_bloqueio} de dano.")
        historico.registrar(f"{self.nome} bloqueou {quantidade_bloqueio}")


    def opcoes(self, jogador):
        escolha = random.choice(["1", "2"])
        if escolha == "1":
            self.atacar(jogador)
        elif escolha == "2":
            self.bloquear()