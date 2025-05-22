from fila import LinkedQueue
from pilha import LinkedStack

# Teste da Fila
print("=== TESTE DA FILA ===")
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

# Teste da Pilha
print("\n\n=== TESTE DA PILHA ===")
pilha = LinkedStack()
print("Pilha vazia:", pilha)

pilha.push(10)
pilha.push(20)
pilha.push(30)
print("\nApós empilhar 3 elementos:")
print(pilha)

print("\nTopo:", pilha.topo)
print("Tamanho:", pilha.tamanho)

removido = pilha.pop()
print("\nElemento removido:", removido)
print("Pilha após pop:")
print(pilha)