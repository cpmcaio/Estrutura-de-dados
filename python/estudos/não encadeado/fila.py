class Pilha:
    def __init__(self):
        self.itens =[]
        
    def push(self, item):
        self.itens.append(item)
        
    def pop(self):
        if not self.vazia():
            return self.itens.pop()
        else:
            print('pilha vazia')
            return None