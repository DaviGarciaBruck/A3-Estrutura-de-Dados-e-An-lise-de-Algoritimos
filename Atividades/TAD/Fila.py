class Elemento:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def esta_vazia(self):
        return self.inicio is None

    def insere(self, v):
        novo = Elemento(v)
        if self.esta_vazia():
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo

    def remove(self):
        if self.esta_vazia():
            print("Fila vazia")
        v = self.inicio.valor
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        return v

    def frente(self):
        if self.esta_vazia():
            print("Fila vazia")
            return None
        return self.inicio.valor

    def tamanho(self):
        tam = 0
        aux = self.inicio
        while aux is not None:
            tam += 1
            aux = aux.proximo
        return tam