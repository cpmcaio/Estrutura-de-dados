class Node:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

    def __str__(self):
        return str(self.dado)

class Lista: 
    def __init__(self):
        self.head = None
        self.tamanho = 0

    def inserir(self, novo_dado, index):
        if index > self.tamanho or index < 0:
            print('posição inválida')
            return
        
        novo_no = Node(novo_dado)
        print(novo_no)

        if index == 0:
            novo_no.prox = self.head
            self.head = novo_no
        else:
            atual = self.head
            for i in range(index - 1):
                atual = atual.prox
            novo_no.prox = atual.prox
            atual.prox = novo_no
        self.tamanho += 1
        
    def vazia(self):
        return self.head is None

    def remover(self, index):
        if index < 0 or index >= self.tamanho:
            raise IndexError('índice inválido')
        if self.vazia():
            print("Lista vazia")
            return
        if index == 0:
            self.head = self.head.prox
        else:
            atual = self.head
            for i in range(index - 1):
                atual = atual.prox
            atual.prox = atual.prox.prox
        self.tamanho -= 1

    def exibir(self):
        y = []
        q = self.head
        while q is not None:
            y.append(str(q.dado))
            q = q.prox
        return y

    def buscar_tds(self, dado_procurado):
        if self.vazia():
            return "lista vazia"
        q = self.head
        ocorrencias = []
        while q is not None:
            if q.dado == dado_procurado:
                ocorrencias.append(str(q.dado))
            q = q.prox
        if not ocorrencias:
            return "não há ocorrências"
        return ocorrencias


# Testando
minha_lista = Lista()
minha_lista.inserir("ian", 0)
minha_lista.inserir("davi", 1)
minha_lista.inserir("ian", 1)
minha_lista.inserir("davi", 1)

print(minha_lista.exibir())          # ['ian', 'davi', 'ian', 'davi']
print(minha_lista.buscar_tds('ian')) # ['ian', 'ian']