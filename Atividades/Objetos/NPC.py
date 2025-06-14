import random
from Objetos.Sala import Sala
from Objetos.HistoricoAcoes import historico

class NPC:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def atacar(self, jogador):
        dano = random.randint(1, 6)
        if dano == 6:
            print("Acerto Crítico!")
            dano = 10
        print(f"{self.nome} causou {dano} de dano!")
        historico.registrar(f"{self.nome} atacou {jogador.nome} e causou {dano} de dano.")
        jogador.vida -= dano
        return dano
    
    def curar(self):
        quantidade_cura = random.randint(0, 2)
        self.vida += quantidade_cura
        print(f"{self.nome} curou {quantidade_cura}")
        historico.registrar(f"{self.nome} curou {quantidade_cura} pontos de vida.")
        return quantidade_cura

    def opcoes_ataque(self, jogador):
        escolha = random.choice(["1", "2"])
        if escolha == "1":
            self.atacar(jogador)
        elif escolha == "2":
            self.curar()

    def compra(self, jogador, inimigo):

        print(f"Você tem {jogador.ouro} de ouro.")
        print(f"1. Banana - 10 de ouro")
        print(f"2. Poção de viagem temporal - 20 de ouro")
        print(f"3. Sair da loja")
        compra = input("Escolha uma opção: ")
        if compra == "1":
            if jogador.ouro >= 10:
                jogador.pocoes_vida += 1
                jogador.ouro -= 10
                print(f"{self.nome} diz: 'Você comprou uma banana!'")
                historico.registrar(f"{jogador.nome} comprou uma banana por 10 de ouro.")
            elif jogador.ouro < 10:
                print("Você não tem ouro suficiente!")
                self.compra(jogador, inimigo)
        elif compra == "2":
            if jogador.ouro > 20:
                jogador.pocoes_tempo += 1
                jogador.ouro -= 20
                print(f"{self.nome} - Use essa belezinha com cuidado!")
                historico.registrar(f"{jogador.nome} comprou uma poção de viagem temporal por 20 de ouro.")
            if jogador.ouro < 20:
                print("Você não tem ouro suficiente!")
                self.compra(jogador, inimigo)
        elif compra == "3":
            print(f"{self.nome} - Que pena, mas caso você mude de ideia, continuo aqui.")
            self.opcoes_dialogo_vendedor(jogador, inimigo)
        else:
            print("Escolha inválida. Tente novamente.")
            self.opcoes_dialogo_vendedor(jogador, inimigo)

#fazer mais desse método para os outros npcs
    def opcoes_dialogo_musico(self, jogador, inimigo):
        print(f"Após derrotar {inimigo.nome}, você encontra um macaco com roupas rasgadas tocando um violão desafinado.")
        print("--------------------------------------------------------")
        print(f"{self.nome} - Sinta o ritmo da floresta.")
        print("1. - Uau, essa música é... diferente. Nunca ouvi nada assim. Muito criativa!")
        print("2. - Sinceramente, isso está horrível. Acho que seu violão está desafinado.")
        print("3. Ignorar.")
        escolha = input("Escolha uma opção: ")
        print("--------------------------------------------------------")
        if escolha == "1":
            print(f"({self.nome} te chama de mentiroso e vai embora.)")
            historico.registrar(f"{jogador.nome} mentiu para {self.nome}.")
        elif escolha == "2":
            print(f"{self.nome} - Realmente, eu não faço ideia de como toca um violão, toma essa banana em troca da sua sinceridade.")
            jogador.pocoes_vida += 1
            historico.registrar(f"{jogador.nome} foi sincero com {self.nome} e recebeu uma banana em troca.")
        elif escolha == "3":
            print(f"Você ignorou {self.nome}.")
            historico.registrar(f"{jogador.nome} ignorou {self.nome}.")
        else:
            print("Escolha inválida. Tente novamente.")
            self.opcoes_dialogo_musico(jogador, inimigo)

    def opcoes_dialogo_vendedor(self, jogador, inimigo):
        print(f"Após derrotar {inimigo.nome}, você encontra um macaco com uma mochila gigante.")
        print("--------------------------------------------------------")
        print(f"{self.nome} - Ei, ei! Chega mais, parceiro! Tenho coisas únicas, direto das florestas do norte!")
        print("1. - Uau, isso aqui parece bem... raro. Nem sei se estou à altura para levar algo tão valioso.")
        print("2. - Isso tudo parece sucata. Quem é que compraria esse monte de tralha?")
        print("3. Comprar.")
        print("4. Ignorar.")
        escolha = input("Escolha uma opção: ")
        print("--------------------------------------------------------")
        if escolha == "1":
            print(f"{self.nome} parece ter ficado extremamente feliz com seu comentário.")
            print(f"{self.nome} - Ah, você entende de classe! Leva isso aqui, um brinde do nosso primeiro encontro!")
            print(f"{self.nome} te entrega um fraco azul escrito 'poção de tempo'")
            jogador.pocoes_tempo += 1
            historico.registrar(f"{jogador.nome} elogiou os itens de {self.nome} e lhe ofereceu uma poção de viagem temporal.")
        elif escolha == "3":
            print(f"Você escolheu comprar algo com {self.nome}.")
            historico.registrar(f"{jogador.nome} escolheu comprar algo com {self.nome}.")
            self.compra(jogador, inimigo)
        elif escolha == "2":
            print(f"{self.nome} - Tralha?! Você vai ver o que essa 'tralha' faz voando na sua cabeça!")
            historico.registrar(f"{jogador.nome} foi grosseiro com {self.nome} e ele decidiu atacar.")
            Sala().lutar_npc(jogador, self)
        elif escolha == "4":
            print(f"Você ignorou {self.nome}.")
            historico.registrar(f"{jogador.nome} ignorou {self.nome}.")
        else:
            print("Escolha inválida. Tente novamente.")
            self.opcoes_dialogo_vendedor(jogador, inimigo)

    def opcoes_dialogo_chef(self, jogador, inimigo):
        print(f"Após derrotar {inimigo.nome}, você encontra um macaco vestindo um avental e um chapéu de chef.")
        print("--------------------------------------------------------")
        print(f"{self.nome} - Ei, você, preciso que prove esse prato para mim e me diga o que acha.")
        print("1. - Nossa, essa é a melhor refeição que eu já comi na minha vida.")
        print("2. - Hum, acho que um molho de banana combinaria muito com esse prato.")
        print("3. Ignorar.")
        escolha = input("Escolha uma opção: ")
        print("--------------------------------------------------------")
        if escolha == "1":
            print(f"{self.nome} - Eu não tenho tempo para bajulação, se você não me der algo construtivo, então você é inútil para mim.")
            historico.registrar(f"{jogador.nome} tentou bajular {self.nome}, porém não obteve sucesso.")
        elif escolha == "2":
            print(f"{self.nome} - MOLHO DE BANANA? Isso nem existe! Espera, isso é genial, um molho de banana! Tome isso, camarada.")
            print(f"{self.nome} te entregou 3 bananas como agradecimento.")
            jogador.pocoes_vida += 3
            historico.registrar(f"{jogador.nome} fez uma sugestão para {self.nome} e ele te entregou algumas bananas como agradecimento.")
        elif escolha == "3":
            print(f"Você ignorou {self.nome}.")
            historico.registrar(f"{jogador.nome} ignorou {self.nome}.")
        else:
            print("Escolha inválida. Tente novamente.")
            self.opcoes_dialogo_chef(jogador, inimigo)

    def opcoes_dialogo_guerreiro(self, jogador, inimigo):
        print(f"Após derrotar {inimigo.nome}, você encontra um macaco de armadura batendo em uma árvore.")
        print("--------------------------------------------------------")
        print(f"{self.nome} - Você parece corajoso... mas coragem de verdade se mostra em batalha, não com papo.")
        print("1. - Cai dentro.")
        print("2. - Espere um segundo, eu não desejo batalhar com ninguém.")
        print("3. Ignorar.")
        escolha = input("Escolha uma opção: ")
        print("--------------------------------------------------------")
        
        if escolha == "2":
            print(f"{self.nome} parece ter ficado decepcionado com a sua escolha.")
            print(f"{self.nome} - hmpf, você não passa de um covarde.")
            print(f"{self.nome} guarda a sua espada e vai embora.")
            historico.registrar(f"{jogador.nome} decepcionou {self.nome}.")
        elif escolha == "1":
            print(f"{self.nome} - Haha é isso aí.")
            historico.registrar(f"{jogador.nome} aceitou o desafio de {self.nome}.")
            Sala().lutar_npc(jogador, self)
            if jogador.vida > 0:
                jogador.buff_ataque = 1
                print(f"{jogador.nome} recebeu um aumento no dano dado a partir de agora.")
        elif escolha == "3":
            print(f"Você ignorou {self.nome}.")
            historico.registrar(f"{jogador.nome} ignorou {self.nome}.")
        else:
            print("Escolha inválida. Tente novamente.")
            self.opcoes_dialogo_guerreiro(jogador, inimigo)

    def opcoes_dialogo_estranho(self, jogador, inimigo):
        print(f"Após derrotar {inimigo.nome}, você encontra um macaco bem-vestido, usando uma cartola e parece estar lhe esperando.")
        print("--------------------------------------------------------")
        print(f"{self.nome} - Boa tarde, parceiro, você viu aquela fruta estranha lá no topo da árvore? Dizem que tem poder...")
        print("1. (Subir na árvore e pegar a fruta.)")
        print("2. - Nem a pau que eu vou pegar esse treco.")
        print("3. Ignorar.")
        escolha = input("Escolha uma opção: ")
        print("--------------------------------------------------------")
        if escolha == "1":
            print(f"{jogador.nome} pegou a fruta do topo da árvore, ao comê-la sente uma grande dor no peito.")
            print(f"Ao se virar, {jogador.nome} não vê ninguém ao seu redor.")
            jogador.vida -= 10 
            historico.registrar(f"{jogador.nome} pegou a fruta de {self.nome} e nunca mais o viu.")
        elif escolha == "2":
            print(f"Ao se virar para falar com {self.nome}, {jogador.nome} não o encontra.")
            print(f"Ao olhar no chão, {jogador.nome} encontra uma banana.")
            jogador.pocoes_vida += 1
            historico.registrar(f"{jogador.nome} negou pegar a fruta e {self.nome} desapareceu.")
        elif escolha == "3":
            print(f"Você ignorou {self.nome}.")
            historico.registrar(f"{jogador.nome} ignorou {self.nome}.")
        else:
            print("Escolha inválida. Tente novamente.")
            self.opcoes_dialogo_estranho(jogador, inimigo)