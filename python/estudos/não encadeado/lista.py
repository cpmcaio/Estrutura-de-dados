class Lista:
    def __init__ (self):
        self.lista = []
    
    def adicionar(self, valor):
        self.lista.append(valor)
    
    def remover(self, valor):
        if valor in self.lista:
            self.lista.remove(valor)
        else:
            print("Valor não encontrado na lista.")

    def vazia(self):
        if len(self.lista) == 0:
            return True
        else:
            return False
    
    def tamanho(self):
        return len(self.lista)
    
    def __str__(self):
        return str(self.lista)

    def soma(self):
        if self.vazia():
            return 0
        else:
            soma=0
            for i in range(len(self.lista)):
                soma += self.lista[i]
            return soma 