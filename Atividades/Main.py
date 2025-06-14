from Objetos.Jogador import Jogador
from Objetos.Inimigo import Inimigo
from Objetos.NPC import NPC
from Objetos.Sala import Sala
from Objetos.HistoricoAcoes import historico


def main():

    jogar_novamente = True

    while jogar_novamente:
        # Criação de NPCs
        npc1 = NPC("Gorila", 20)
        npc2 = NPC("Babuíno", 20)
        npc3 = NPC("Mico-leão-dourado", 20)
        npc4 = NPC("Macaco-prego", 20)
        npc5 = NPC("Macaco-aranha", 20)

        # Criação de inimigos
        inimigo1 = Inimigo("Orc", 25)
        inimigo2 = Inimigo("Goblin", 10)
        inimigo3 = Inimigo("Goblin", 10)
        inimigo4 = Inimigo("Goblin", 10)
        inimigo5 = Inimigo("Dragão", 30)
        inimigo6 = Inimigo("Troll", 22)
        inimigo7 = Inimigo("Esqueleto", 15)

        # Criação da sala
        sala = Sala()

    
        # Jogo
        print("--------------------------------------------------------")
        print("Ao ser amaldiçoado por uma bruxa coruja com fome eterna, você entra em uma masmorra a procura da banana dourada com esperança de desfazer a maldição.")
        print("--------------------------------------------------------")
        input("Pressione enter para continuar...")
        print("--------------------------------------------------------")
        print("Bem-vindo a masmorra do bananal.")
        print("--------------------------------------------------------")
        input("Pressione enter para continuar...")
        print("--------------------------------------------------------")
        nome_jogador = input("Digite o nome do seu personagem: ")
        jogador = Jogador(nome_jogador, 30, 0, 0, 0)

        print("========================================================")
        print(f"Ao se aproximar da primeira sala, você se depara com um esqueleto!")        
        sala.sala(jogador, inimigo7, npc1)
        if jogador.vida > 0:
            print("========================================================")
            print(f"Ao entrar na segunda sala, você encontra um troll!")
            sala.sala(jogador, inimigo6, npc2)
        if jogador.vida > 0:
            print("========================================================")
            print(f"Ao entrar na terceira sala, você é surpreendido por um grupo de goblins!")
            sala.sala_com_fila(jogador, [inimigo2, inimigo3, inimigo4], npc3)
        if jogador.vida > 0:
            print("========================================================")
            print(f"Ao entrar na quarta sala, você vê um orc!")
            sala.sala(jogador, inimigo1, npc4)
        if jogador.vida > 0:
            print("========================================================")
            print(f"Finalmente, ao entrar na última sala, você se assusta com um gigantesco dragão!")
            sala.sala(jogador, inimigo5, npc5)

        if jogador.vida > 0:
            print("--------------------------------------------------------")
            print(f"Ao chegar no final da masmorra, você encontra a banana dourada. Ao comê-la, você sente que a maldição foi desfeita.")
            print(f"{jogador.nome} venceu o jogo com {jogador.vida} de vida restante!")
            historico.registrar(f"{jogador.nome} venceu o jogo.")
            print("Deseja jogar novamente? (s/n)")
            resposta = input().lower()
            jogar_novamente = resposta == 's'
        else:
            print("--------------------------------------------------------")
            print(f"{jogador.nome} foi derrotado! Fim de jogo.")
            historico.registrar(f"{jogador.nome} foi derrotado")
            print("--------------------------------------------------------")
            print(f"deseja reiniciar o jogo? (s/n)")
            resposta = input().lower()
            jogar_novamente = resposta == 's'
            
        if not jogar_novamente:
            print("Obrigado por jogar! Gostaria de ver o histórico de ações? (s/n)")
            resposta = input().lower()
            if resposta == 's':
                print("--------------------------------------------------------")
                historico.mostrar()
                input("Pressione Enter para sair.")
                break
            else:
                input("Pressione Enter para sair.")
                break


if __name__ == "__main__":
    main()
    