from TAD.Lista import ListaSimples

class HistoricoAcoes:
    def __init__(self):
        self.acoes = ListaSimples()

    def registrar(self, descricao):
        self.acoes.insere_ultimo(descricao)

    def mostrar(self):
        atual = self.acoes.primeiro
        print("Histórico de ações:")
        i = 1
        while atual is not None:
            print(f"{i}. {atual.valor}")
            atual = atual.proximo
            i += 1

#historico global
historico = HistoricoAcoes()