import random
from TAD.Pilha import PilhaDinamica
from TAD.Fila import Fila

class Sala:
    def lutar_inimigo(self, jogador, inimigo):
        pilha_estado = PilhaDinamica()
        while jogador.vida > 0 and inimigo.vida > 0:
            print("--------------------------------------------------------")
            resultado = jogador.opcoes_inimigo(inimigo, pilha_estado)
            if resultado == "acao":
                if inimigo.vida > 0:
                    inimigo.opcoes(jogador)
            if jogador.vida <= 0:
                break
            elif inimigo.vida <= 0:
                ouro_ganho = random.randint(1, 10)
                jogador.ouro += ouro_ganho
                print(f"{inimigo.nome} foi derrotado! Você ganhou {ouro_ganho} de ouro!")
                break

    def lutar_npc(self, jogador, npc):
        pilha_estado = PilhaDinamica()
        while jogador.vida > 0 and npc.vida > 0:
            print("--------------------------------------------------------")
            resultado = jogador.opcoes_npc(npc, pilha_estado)
            if resultado == "acao":
                if npc.vida > 0:
                    npc.opcoes_ataque(jogador)
            if jogador.vida <= 0:
                break
            elif npc.vida <= 0:
                ouro_ganho = random.randint(1, 10)
                jogador.ouro += ouro_ganho
                print(f"{npc.nome} foi derrotado! Você roubou {ouro_ganho} de ouro!")
                break

    def encontro_aleatorio(self, jogador, npc, inimigo):
        print("--------------------------------------------------------")
        if jogador.vida <= 0:
            return
        else:
            escolha = random.choice(["1", "2", "3", "4"])
            if escolha == "1":
                print(f"Após derrotar o {inimigo.nome}, você encontra algo que chama sua atenção.")
                jogador.pocoes_vida += 1
                print(f"{jogador.nome} encontrou uma banana! Total de bananas: {jogador.pocoes_vida}")

            elif escolha == "2":
                escolha = random.choice(["1", "2", "3", "4", "5"])
                if escolha == "1":
                    npc.opcoes_dialogo_musico(jogador, inimigo)
                elif escolha == "2":
                    npc.opcoes_dialogo_vendedor(jogador, inimigo)
                elif escolha == "3":
                    npc.opcoes_dialogo_chef(jogador, inimigo)
                elif escolha == "4":
                    npc.opcoes_dialogo_guerreiro(jogador, inimigo)
                elif escolha == "5":
                    npc.opcoes_dialogo_estranho(jogador, inimigo)      

            elif escolha == "3":
                print(f"Após derrotar o {inimigo.nome}, você encontra algo que chama sua atenção.")
                jogador.pocoes_tempo += 1
                print(f"{jogador.nome} encontrou uma poção de viagem temporal! Total de poções: {jogador.pocoes_tempo}")    

            else:
                print(f"Você encontrou uma pedra em um formato engraçado.")
            print("--------------------------------------------------------")
            pausa = input("Pressione Enter para continuar...")

    def sala(self, jogador, inimigo, npc):
        if jogador.vida <= 0:
            return
        else:
            self.lutar_inimigo(jogador, inimigo)
            if jogador.vida <= 0:
                return
            else:
                self.encontro_aleatorio(jogador, npc, inimigo)

    def sala_com_fila(self, jogador, lista_inimigos, npc):
        fila_inimigos = Fila()
        for inimigo in lista_inimigos:
            fila_inimigos.insere(inimigo)
        while not fila_inimigos.esta_vazia() and jogador.vida > 0:
            inimigo_atual = fila_inimigos.remove()
            self.lutar_inimigo(jogador, inimigo_atual)
            if jogador.vida <= 0:
                return
        if jogador.vida > 0:
            self.encontro_aleatorio(jogador, npc, inimigo)