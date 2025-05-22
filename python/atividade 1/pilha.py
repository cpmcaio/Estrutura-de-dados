from no import Node

class LinkedStack:
    def __init__(self):
        self.__top = None
        self.__tamanho = 0

    @property
    def topo(self):
        if self.__top is not None:
            return self.__top.dado
        return None 

    @property
    def tamanho(self):
        return self.__tamanho

    def push(self, novo_dado):
        no = Node(novo_dado)
        no.prox = self.__top
        self.__top = no
        self.__tamanho += 1

    def pop(self):
        if self.__top is not None:
            removido = self.__top.dado
            self.__top = self.__top.prox
            self.__tamanho -= 1
            return removido
        return None

    def __str__(self):
        elementos = []
        atual = self.__top
        while atual:
            elementos.append(str(atual.dado))
            atual = atual.prox
        return "Topo -> " + " -> ".join(elementos) + " -> None"


#teste
p = LinkedStack()

print("Pilha inicial:", p)
print("Inserindo elementos:")
p.push(10)
print(p)
p.push(20)
print(p)
p.push(30)
print(p)

print(f"Tamanho: {p.tamanho}")  
print(f"Topo: {p.topo}")       

print("\nRemovendo elementos:")
print("Removido:", p.pop())  
print(p)
print("Removido:", p.pop())  
print(p)
print("Removido:", p.pop())  
print(p)

print("Tentando remover de pilha vazia:")
print("Removido:", p.pop())
print(p)
