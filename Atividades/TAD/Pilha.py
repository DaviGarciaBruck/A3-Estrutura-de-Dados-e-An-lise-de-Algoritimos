class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class PilhaDinamica:
    def __init__(self):
        self.topo = None

    def esta_vazia(self):
        return self.topo is None

    def empilha(self, v):
        novo = No(v)
        novo.proximo = self.topo
        self.topo = novo

    def desempilha(self):
        if self.topo is None:
            raise IndexError("A pilha está vazia")
        ret_val = self.topo.valor
        self.topo = self.topo.proximo
        return ret_val