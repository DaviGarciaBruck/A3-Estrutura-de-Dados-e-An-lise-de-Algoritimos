import random
from Objetos.HistoricoAcoes import historico

class Jogador:
    
    def __init__(self, nome, vida, pocoes_vida, pocoes_tempo, ouro):
        self.nome = nome
        self.vida = vida
        self.pocoes_vida = pocoes_vida
        self.pocoes_tempo = pocoes_tempo
        self.ouro = ouro
        self.buff_ataque = 0

    def get_estado(self):
        return (self.vida, self.pocoes_vida)

    def set_estado(self, estado):
        self.vida, self.pocoes_vida = estado

    def atacar_inimigo(self, inimigo):
        dano = random.randint(1, 6)
        if dano == 6:
            print("Acerto crítico!")
            dano = 10

        if self.buff_ataque == 1:
            dano += 2

        print(f"{self.nome} causou {dano} de dano!")
        historico.registrar(f"{self.nome} atacou {inimigo.nome} e causou {dano} de dano.")

        if inimigo.bloqueio >= dano:
            dano = 0
            inimigo.bloqueio = 0
        else:
            inimigo.vida -= dano
        return dano
    
    def atacar_npc(self, inimigo):
        dano = random.randint(1, 6)
        if dano == 6:
            print("Acerto crítico!")
            dano = 10

        if self.buff_ataque == 1:
            dano += 2

        print(f"{self.nome} causou {dano} de dano!")
        historico.registrar(f"{self.nome} atacou {inimigo.nome} e causou {dano} de dano.")
        inimigo.vida -= dano
        return dano

    def curar(self):
        if self.pocoes_vida >= 1:
            if self.vida >= 30:
                print("Você já está com a vida cheia!")
                return 0
            else:
                quantidade_cura = random.randint(1, 20)
                self.vida += quantidade_cura
                self.pocoes_vida -= 1
                print(f"{self.nome} curou {quantidade_cura}")
                historico.registrar(f"{self.nome} comeu uma banana e curou {quantidade_cura} pontos de vida.")
                return quantidade_cura
                
        else:
            print("Você não tem nenhuma banana")

    def opcoes_inimigo(self, inimigo, pilha_estado):
        print(f"{self.nome} - Vida: {self.vida}, Bananas: {self.pocoes_vida}, Poções de viagem temporal: {self.pocoes_tempo}, Ouro: {self.ouro}")
        print(f"{inimigo.nome} - Vida: {inimigo.vida}, Bloqueio: {inimigo.bloqueio}")
        print("1. Atacar")
        print("2. Curar")
        print("3. Voltar ação")
        escolha = input("Escolha uma opção: ")
        print("--------------------------------------------------------")
        if escolha == "1":
            pilha_estado.empilha(self.get_estado())
            self.atacar_inimigo(inimigo)
            return "acao"
        elif escolha == "2":
            pilha_estado.empilha(self.get_estado())
            self.curar()
            return "acao"
        elif escolha == "3":
            if self.pocoes_tempo > 0:
                if not pilha_estado.esta_vazia():
                    self.pocoes_tempo -= 1
                    estado_anterior = pilha_estado.desempilha()
                    self.set_estado(estado_anterior)
                    print("Ação desfeita! Estado anterior restaurado.")
                    historico.registrar(f"{self.nome} usou uma poção de viagem temporal para desfazer a última ação.")
                    return "desfez"
                else:
                    print("Não há ação anterior para desfazer.")
                    return self.opcoes_inimigo(inimigo, pilha_estado)
            else:
                print("Você não tem poções de viagem temporal!")
                return self.opcoes_inimigo(inimigo, pilha_estado)
        else:
            print("Escolha inválida. Tente novamente.")
            return self.opcoes_inimigo(inimigo, pilha_estado)
        
    def opcoes_npc(self, inimigo, pilha_estado):
        print(f"{self.nome} - Vida: {self.vida}, Bananas: {self.pocoes_vida}, Poções de viagem temporal: {self.pocoes_tempo}, Ouro: {self.ouro}")
        print(f"{inimigo.nome} - Vida: {inimigo.vida}")
        print("1. Atacar")
        print("2. Curar")
        print("3. Voltar ação")
        escolha = input("Escolha uma opção: ")
        print("--------------------------------------------------------")
        if escolha == "1":
            pilha_estado.empilha(self.get_estado())
            self.atacar_npc(inimigo)
            return "acao"
        elif escolha == "2":
            pilha_estado.empilha(self.get_estado())
            self.curar()
            return "acao"
        elif escolha == "3":
            if self.pocoes_tempo > 0:
                if not pilha_estado.esta_vazia():
                    self.pocoes_tempo -= 1
                    estado_anterior = pilha_estado.desempilha()
                    self.set_estado(estado_anterior)
                    print("Ação desfeita! Estado anterior restaurado.")
                    historico.registrar(f"{self.nome} usou uma poção de viagem temporal para desfazer a última ação.")
                    return "desfez"
                else:
                    print("Não há ação anterior para desfazer.")
                    return self.opcoes_npc(inimigo, pilha_estado)
            else:
                print("Você não tem poções de viagem temporal!")
                return self.opcoes_npc(inimigo, pilha_estado)
        else:
            print("Escolha inválida. Tente novamente.")
            return self.opcoes_npc(inimigo, pilha_estado)