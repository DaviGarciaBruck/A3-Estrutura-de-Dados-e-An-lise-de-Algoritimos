class Elemento:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaSimples:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.atual = None

    def esta_vazio(self):
        return self.primeiro is None

    def comprimento(self):
        comp = 0
        self.atual = self.primeiro
        while self.atual is not None:
            comp += 1
            self.atual = self.atual.proximo
        return comp

    def insere_primeiro(self, v):
        novo = Elemento(v)
        if self.esta_vazio():
            self.primeiro = novo
            self.ultimo = novo
            self.atual = novo
        else:
            novo.proximo = self.primeiro
            self.primeiro = novo

    def insere_ultimo(self, v):
        novo = Elemento(v)
        if self.esta_vazio():
            self.primeiro = novo
            self.ultimo = novo
            self.atual = novo
        else:
            self.ultimo.proximo = novo
            self.ultimo = novo

    def move_para_posicao(self, pos):
        self.atual = self.primeiro
        for _ in range(pos):
            if self.atual is not None:
                self.atual = self.atual.proximo

    def insere_na_posicao(self, v, pos):
        novo = Elemento(v)
        self.move_para_posicao(pos)
        novo.proximo = self.atual.proximo
        self.atual.proximo = novo

    def primeiro_elemento(self):
        return self.primeiro.valor

    def ultimo_elemento(self):
        return self.ultimo.valor

    def elemento_na_posicao(self, pos):
        self.move_para_posicao(pos)
        return self.atual.valor

    def busca_elemento(self, v):
        cont = 0
        self.atual = self.primeiro
        while self.atual is not None and self.atual.valor != v:
            self.atual = self.atual.proximo
            cont += 1
        if self.atual is not None:
            return cont
        return -1

    def remove_primeiro(self):
        if self.primeiro is not None:
            self.primeiro = self.primeiro.proximo

    def remove_ultimo(self):
        pos = self.comprimento() - 1
        self.move_para_posicao(pos)
        self.atual.proximo = None
        self.ultimo = self.atual

    def remove_elemento(self, v):
        pos = self.busca_elemento(v)
        if pos > -1:
            temp = self.atual.proximo
            pos = pos - 1
            self.move_para_posicao(pos)
            self.atual.proximo = temp

    def remove_na_posicao(self, pos):
        self.move_para_posicao(pos)
        temp = self.atual.proximo
        pos = pos - 1
        self.move_para_posicao(pos)
        self.atual.proximo = temp