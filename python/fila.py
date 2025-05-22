from no import Node
class LinkedQueue:
    def __init__(self):
        self.__frente = None
        self.__tras = None
        self.__tamanho = 0

    @property
    def frente(self):
        return self.__frente.dado if self.__frente else None

    @property
    def tamanho(self):
        return self.__tamanho

    def enqueue(self, dado):
        novo_no = Node(dado)
        if self.__tras:
            self.__tras.prox = novo_no
        self.__tras = novo_no
        if self.__frente is None:
            self.__frente = novo_no
        self.__tamanho += 1

    def dequeue(self):
        if self.__frente is None:
            return None
        removido = self.__frente.dado
        self.__frente = self.__frente.prox
        if self.__frente is None:
            self.__tras = None
        self.__tamanho -= 1
        return removido

    def __str__(self):
        elementos = []
        atual = self.__frente
        while atual:
            elementos.append(str(atual.dado))
            atual = atual.prox
        return "Frente -> " + " -> ".join(elementos) + " -> None"

fila = LinkedQueue()
print("Fila vazia:", fila)

fila.enqueue("Primeiro")
fila.enqueue("Segundo")
print("\nApós enfileirar 2 elementos:")
print(fila)

print("\nFront:", fila.frente)
print("Tamanho:", fila.tamanho)

removido = fila.dequeue()
print("\nElemento removido:", removido)
print("Fila após dequeue:")
print(fila)